# Health Facility Appointment and Queue Management System

##  Project Description

The Health Facility Appointment and Queue Management System is a web-based healthcare management solution developed to improve efficiency in hospitals and clinics by automating patient registration, appointment scheduling, queue handling, and consultation management.

The system reduces long waiting times, improves patient flow, minimizes paperwork, and enhances communication between patients, receptionists, and doctors.

The project was developed using:

* Python Flask
* MySQL
* HTML
* CSS
* Bootstrap
* Jinja2 Templates

---

#  Objectives

## Main Objective

To develop a web-based system that automates appointment booking and queue management processes in healthcare facilities.

---

## Specific Objectives

* To allow patients to register online
* To allow patients to book appointments
* To allow receptionists to manage walk-in patients
* To automate queue number generation
* To allow doctors to manage consultations
* To improve patient flow visibility
* To reduce congestion and waiting time

---

#  System Features

## Authentication Module

* User login
* Password hashing
* Session management
* Role-based access control

---

## Patient Management

* Patient self-registration
* Receptionist patient registration
* View patient records
* Store patient profiles securely

---

## Appointment Management

* Appointment booking
* Online patient appointment booking
* Receptionist appointment scheduling
* Prevent double booking
* Doctor assignment

---

## Queue Management

* Generate queue numbers
* Patient check-in
* Queue tracking
* Call next patient
* Queue status updates

---

## Consultation Management

* Doctor consultation dashboard
* Consultation notes
* Diagnosis records
* Treatment management

---

## Dashboard Management

### Receptionist Dashboard

* Register patients
* Manage queue
* Book appointments

### Doctor Dashboard

* View patient queue
* Manage consultations

### Patient Dashboard

* Book appointments
* View appointments
* Logout

---

#  Technologies Used

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend programming |
| Flask      | Web framework       |
| MySQL      | Database management |
| HTML       | Frontend structure  |
| CSS        | Styling             |
| Bootstrap  | Responsive design   |
| Jinja2     | Dynamic templates   |

---

#  Project Structure

```text id="u4m8zr"
Health-Facility-Appointment-Queue-System/
│
├── app2.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── health_system_db.sql
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
│   ├── patient_register.html
│   ├── patient_dashboard.html
│   ├── appointments.html
│   ├── queue.html
│   ├── doctor_dashboard.html
│   └── reception_dashboard.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── screenshots/
```

---

#  Database Tables

The system uses the following tables:

* users
* doctors
* receptionists
* patients
* appointments
* queue
* consultations

---

#  Installation Guide

## Step 1 — Clone Repository

```bash id="z7m3qc"
git clone https://github.com/your-username/health-facility-system.git
```

---

## Step 2 — Open Project

```bash id="r2k8tw"
cd health-facility-system
```

---

## Step 3 — Create Virtual Environment

```bash id="x5n1pv"
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### Windows

```bash id="m9q4yr"
venv\Scripts\activate
```

### Linux/Mac

```bash id="p4t7ws"
source venv/bin/activate
```

---

## Step 5 — Install Dependencies

```bash id="v1m8qx"
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

## Create Database

```sql id="f6r2kn"
CREATE DATABASE health_system_db;
```

---

## Import SQL Dump

Import:

```text id="d8x5pt"
health_system_db.sql
```

using:

* MySQL Workbench
* phpMyAdmin
* Query Browser

---

# Configure Database Connection

Open:

```text id="j3w7rm"
config.py
```

Update:

```python id="u7m1vc"
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "health_system_db"
```

---

# Running The System

Run:

```bash id="q5x9nt"
python app2.py
```

---

# Access System

Open browser:

```text id="h1v4mq"
http://127.0.0.1:5000/login
```

---

# User Roles

| Role         | Responsibilities                          |
| ------------ | ----------------------------------------- |
| Admin        | System management                         |
| Receptionist | Patient registration and queue management |
| Doctor       | Consultation management                   |
| Patient      | Appointment booking                       |

---

# Security Features

* Password hashing
* Session management
* Role-based access control
* Duplicate prevention
* SQL injection prevention

---

# Screenshots

The repository includes screenshots for:

* Login page
* Patient registration
* Appointment booking
* Queue management
* Doctor dashboard
* Reception dashboard
* Patient dashboard

---

# Future Improvements

* SMS notifications
* Email reminders
* Mobile application
* Online payment integration
* AI queue prediction
* Report analytics
* Telemedicine support

---

# Software Engineering Concepts Applied

* Agile Development Methodology
* Modular Architecture
* Role-Based Access Control
* Database Normalization
* MVC Design Principles
* UML System Design

---

# Developed By

**Musa Galiwango**

Academic Software Engineering Project

---

# License

This project is intended for academic and educational purposes only.
