Health Facility Appointment & Queue Management System

A web-based healthcare management system developed using Python Flask, MySQL, HTML, CSS, and Bootstrap to improve patient registration, appointment booking, queue management, and consultation workflows in healthcare facilities.


---

Project Overview

This system was developed to solve common problems faced in health facilities such as:

Long patient queues

Manual patient registration

Poor appointment tracking

Lack of queue visibility

Delays in consultation management

Inefficient patient flow


The system digitizes and automates healthcare appointment and queue management processes.


---

Features

Authentication & Authorization

User login system

Secure password hashing

Role-based access control

Doctor dashboard

Receptionist dashboard

Admin dashboard



---

Patient Management

Register patients

View patient records

Store patient details in MySQL database

Prevent duplicate patient registration



---

Appointment Management

Book appointments

Prevent double booking

Assign doctors

Schedule appointment dates and times



---

Queue Management

Patient check-in

Generate queue numbers

Track queue status

Call next patient

Prevent duplicate queue entries



---

Consultation Management

Doctor consultation interface

Record diagnosis and treatment notes

Update consultation status



---

Reporting

Daily appointments

Queue statistics

Patient records

Consultation reports



---

Technologies Used

Technology	Purpose

Python	Backend programming
Flask	Web framework
MySQL	Database
HTML	Frontend structure
CSS	Styling
Bootstrap	Responsive UI
Jinja2	Template rendering



---

Project Structure

Health Facility Appointment & Queue Management System/
│
├── app2.py
├── config.py
├── requirements.txt
├── README.md
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── patient.py
│   ├── appointment.py
│   ├── queue.py
│   └── consultation.py
│
├── templates/
│   ├── login.html
│   ├── register_user.html
│   ├── register_patient.html
│   ├── appointments.html
│   ├── queue.html
│   ├── doctor_dashboard.html
│   ├── reception_dashboard.html
│   └── admin_dashboard.html
│
├── static/
│   └── style.css
│
└── database/
    └── health_system_db.sql


---

Installation Guide

1. Clone Repository

git clone https://github.com/your-username/health-facility-system.git


---

2. Open Project Folder

cd health-facility-system


---

3. Create Virtual Environment

python -m venv venv


---

4. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate


---

5. Install Requirements

pip install -r requirements.txt


---

Database Setup

Create Database

CREATE DATABASE health_system_db;


---

Import SQL File

Import:

health_system_db.sql

into MySQL Workbench or phpMyAdmin.


---

Configure Database

Update config.py

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DB = "health_system_db"


---

Run The Application

python app2.py


---

Open In Browser

http://127.0.0.1:5000/login


---

User Roles

Role	Permissions

Admin	Full system access
Receptionist	Register patients, book appointments, manage queue
Doctor	View queue, manage consultations



---

Security Features

Password hashing

Session management

Role-based access

Duplicate validation

SQL injection prevention using parameterized queries



---

Database Tables

users

doctors

receptionists

patients

appointments

queue

consultations



---

Future Improvements

SMS notifications

Email reminders

Online patient portal

Mobile application

AI queue prediction

Analytics dashboard

PDF report generation

---

Developed By

Musa Galiwango

Software Engineering Project


---

License

This project is for academic and educational purposes.