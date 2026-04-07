 College Event Registration System

A web-based application built using HTML, CSS, Python Flask, and MySQL that allows students to register for college events and displays real-time registration count dynamically.

Project Overview

This project provides a simple and efficient solution for student event registration. Instead of manual registration, students can fill out an online form. The data is stored in a MySQL database, and the total number of registrations is displayed on the same page using SQL COUNT().

The project is developed as a local prototype and can be migrated to Google Cloud for scalability and real-world deployment.

 Features

* Student Registration Form
* Fields Included:

  * Full Name
  * Student ID
  * Email
  * Phone Number
  * Department (UIT, UID, USLM, UIM)
  * Year (1, 2, 3, 4)
  * Event Selection:

    * Seminar & Workshop (Day 1 - 12 April 2026)
    * Cultural Event (Day 2 - 13 April 2026)
    * Hackathon (Day 3 - 14 April 2026)
* Real-time Total Registration Count
* Clean and User-Friendly Interface

 Technologies Used

| Layer    | Technology     |
| -------- | -------------- |
| Frontend | HTML, CSS      |
| Backend  | Python (Flask) |
| Database | MySQL          |



 Project Structure

college-event-registration-system/
│
├── app.py
├── 
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── database/
    └── mysql




 Installation & Setup Guide
 Step 1: Clone the Repository

bash
git clone https://github.com/your-username/college-event-registration-system.git
cd college-event-registration-system


### Step 3: Setup MySQL Database

1. Open MySQL Command Line or MySQL Workbench
2. Run the following commands:

CREATE DATABASE college_events;

USE college_events;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    student_id VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    department VARCHAR(50),
    year VARCHAR(10),
    event_name VARCHAR(100)
);
Step 4: Configure Database Connection

Open `app.py` and update your MySQL password:

python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="college_events"
)


 Step 5: Run the Application

bash
python app.py

 Step 6: Open in Browser

 How the Application Works

1. User fills the registration form
2. Flask backend receives the data
3. Data is stored in MySQL database
4. SQL COUNT() calculates total registrations
5. Total count is displayed on the homepage

How I Built This Project

* Planned the structure and required features
* Designed the frontend form using HTML and CSS
* Developed backend using Flask to handle form submission
* Connected MySQL database for data storage
* Implemented SQL queries for inserting data and counting registrations
* Tested the application locally on localhost

---

Google Cloud Migration Plan

This application can be deployed on Google Cloud using:

| Local Component | Google Cloud Service |
| --------------- | -------------------- |
| Flask App       | Cloud Run            |
| MySQL Database  | Cloud SQL            |
| Frontend Files  | Cloud Storage        |

Benefits:

* Publicly accessible via URL
* Automatic scaling
* High reliability
* Serverless architecture (no server management)

Key Learnings

* Flask web development
* MySQL database integration
* Frontend and backend connection
* Basics of cloud computing

 Challenges Faced

* Database connection issues
* Handling form data
* Displaying dynamic registration count

 Future Enhancements

* Deploy on Google Cloud
* Add user authentication
* Email notification system
* Admin dashboard

.
