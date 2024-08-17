
---

# **Voting System with NFT Integration**

This project is a simple voting system built with Django. The system allows admins to create polls, students to vote on these polls, and integrates NFT representation of votes on the Solana blockchain.

## **Models Overview**

### **1. Admin**

The `Admin` model represents the administrators of the system, who can create and manage polls. It is linked to Django's built-in `User` model through a one-to-one relationship.

- **Fields:**
  - `user`: A one-to-one relationship with Django's `User` model.
  - `is_admin`: A boolean field that indicates if the user is an admin.

- **Methods:**
  - `__str__()`: Returns the username of the associated user.

### **2. Student**

The `Student` model represents the students who participate in polls. Each student has a unique student ID and email.

- **Fields:**
  - `student_id`: A unique identifier for the student.
  - `name`: The full name of the student.
  - `email`: The student's email address, which must be unique.

- **Methods:**
  - `__str__()`: Returns the name of the student.

### **3. Poll**

The `Poll` model represents a poll created by an admin. Each poll has a title, description, start and end dates, and is associated with an admin.

- **Fields:**
  - `title`: The title of the poll.
  - `description`: A detailed description of the poll.
  - `start_date`: The start date and time of the poll.
  - `end_date`: The end date and time of the poll.
  - `created_by`: A foreign key linking the poll to an admin.

- **Methods:**
  - `__str__()`: Returns the title of the poll.

### **4. Option**

The `Option` model represents the choices available in a poll. Each option is associated with a specific poll.

- **Fields:**
  - `poll`: A foreign key linking the option to a poll.
  - `option_text`: The text of the option.

- **Methods:**
  - `__str__()`: Returns the text of the option.

### **5. Vote**

The `Vote` model links a student to a chosen option in a poll. Each vote is timestamped.

- **Fields:**
  - `student`: A foreign key linking the vote to a student.
  - `option`: A foreign key linking the vote to an option.
  - `timestamp`: The date and time when the vote was cast.

- **Methods:**
  - `__str__()`: Returns a string indicating which student voted for which option.

### **6. NFT**

The `NFT` model represents a vote as an NFT on the Solana blockchain. Each NFT is linked to a vote and has a unique token address.

- **Fields:**
  - `vote`: A one-to-one relationship linking the NFT to a vote.
  - `token_address`: The unique address of the NFT token on the blockchain.
  - `minted_at`: The date and time when the NFT was minted.

- **Methods:**
  - `__str__()`: Returns a string indicating that the NFT represents a specific vote.

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Django 4.x
- SQLite (or any other preferred database)
- Git (for version control)

### **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Xclusive09/XVOTE
   cd XVOTE

   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## **Usage**

- **Admin Panel:** Accessible at `/admin/` to manage users, polls, and other data.
- **Polls:** Admins can create and manage polls, while students can participate in them.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Contributing**

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## **Contact**

For any questions or suggestions, please contact the project maintainer at [ibrahimabdulquddus51@gmail.com](mailto:ibrahimabdulquddus51@gmail.com).

---

You can modify the sections as needed based on your specific project details and requirements.