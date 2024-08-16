from django.urls import path
from .views import AdminLoginView, PollCreateView, PollListView, PollDetailView, StudentLoginView, VoteCreateView, PollResultsView

urlpatterns = [
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('polls/create/', PollCreateView.as_view(), name='poll-create'),
    path('polls/', PollListView.as_view(), name='poll-list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('student/login/', StudentLoginView.as_view(), name='student-login'),
    path('vote/', VoteCreateView.as_view(), name='vote-create'),
    path('polls/<int:poll_id>/results/', PollResultsView.as_view(), name='poll-results'),
]
