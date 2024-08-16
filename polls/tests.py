from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Admin, Student, Poll, Option, Vote

class VotingAppTests(APITestCase):

    def setUp(self):
        # Set up the admin user
        self.admin_user = User.objects.create_superuser(username='Xclusive', password='@Akolade12')
        self.admin = Admin.objects.create(user=self.admin_user)
        
        # Set up a student
        self.student = Student.objects.create(student_id='S1234', name='Test Student', email='student@test.com')
        
        # Set up a poll with timezone-aware datetimes
        self.poll = Poll.objects.create(
            title="Test Poll",
            description="This is a test poll",
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=6),
            created_by=self.admin
        )
        
        # Set up options
        self.option1 = Option.objects.create(poll=self.poll, option_text="Option 1")
        self.option2 = Option.objects.create(poll=self.poll, option_text="Option 2")
        
        # Set up the API client
        self.client = APIClient()

    def test_admin_login(self):
        # Test admin login
        url = reverse('admin-login')
        response = self.client.post(url, {'username': 'Xclusive', 'password': '@Akolade12'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['message'], 'Admin Authenticated')  # Corrected message
        self.assertEqual(response.data['message'].strip(), 'Admin Authenticated')


    def test_poll_creation(self):
        # Test poll creation (requires authentication as admin)
        self.client.login(username='Xclusive', password='@Akolade12')
        url = reverse('poll-create')
        data = {
            'title': 'NACOS 2024',
            'description': 'NACOS FUD CHAPTER ELECTION',
            'start_date': timezone.now(),
            'end_date': timezone.now() + timezone.timedelta(days=5),
            'created_by': self.admin.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'NACOS 2024')

    def test_poll_list(self):
        # Test poll listing
        url = reverse('poll-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One poll in the list
        self.assertEqual(response.data[0]['title'], 'Test Poll')

    def test_poll_detail(self):
        # Test poll detail (requires authentication)
        self.client.login(username='Xclusive', password='@Akolade12')
        url = reverse('poll-detail', args=[self.poll.id])
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Poll')

    def test_student_login(self):
        # Test student login
        url = reverse('student-login')
        response = self.client.post(url, {'student_id': 'S1234'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Student Authenticated')

    def test_vote_creation(self):
        # Test vote creation
        url = reverse('vote-create')
        data = {
            'student_id': 'S1234',
            'option_id': self.option1.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Vote recorded')

    def test_poll_results(self):
        # Test real-time vote count display
        Vote.objects.create(student=self.student, option=self.option1)
        url = reverse('poll-results', args=[self.poll.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['poll'], 'Test Poll')
        self.assertEqual(response.data['results']['Option 1'], 1)  # One vote for Option 1
        self.assertEqual(response.data['results']['Option 2'], 0)  # Zero votes for Option 2
