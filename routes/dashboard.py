from flask import render_template, session, redirect, Blueprint
from routes.utils import role_required

dashboard_bp = Blueprint("dashboard", __name__)
@dashboard_bp.route('/doctor/dashboard')
@role_required('doctor')
def doctor_dashboard():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    # Patients waiting
    cur.execute("""
        SELECT queue.queue_id, patients.first_name,
       patients.last_name, queue.queue_number
        FROM queue
        JOIN patients ON queue.patient_id = patients.patient_id
        WHERE queue.status='waiting'
        ORDER BY queue.queue_number ASC
    """)
    queue = cur.fetchall()

    return render_template('doctor_dashboard.html', queue=queue)


@dashboard_bp.route('/reception/dashboard')
@role_required('receptionist')
def reception_dashboard():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    # Total patients
    cur.execute("SELECT COUNT(*) FROM patients")
    total_patients = cur.fetchone()[0]

    # Total appointments
    cur.execute("SELECT COUNT(*) FROM appointments")
    total_appointments = cur.fetchone()[0]

    # Queue count
    cur.execute("SELECT COUNT(*) FROM queue WHERE status='waiting'")
    waiting = cur.fetchone()[0]

    return render_template(
        'reception_dashboard.html',
        total_patients=total_patients,
        total_appointments=total_appointments,
        waiting=waiting
    )


@dashboard_bp.route('/admin/dashboard')
@role_required('admin')
def admin_dashboard():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    # Users count
    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    # Doctors count
    cur.execute("SELECT COUNT(*) FROM users WHERE role='doctor'")
    doctors = cur.fetchone()[0]

    # Receptionists count
    cur.execute("SELECT COUNT(*) FROM users WHERE role='receptionist'")
    receptionists = cur.fetchone()[0]

    return render_template(
        'admin_dashboard.html',
        users=users,
        doctors=doctors,
        receptionists=receptionists
    )
    
    
@dashboard_bp.route('/patient/dashboard')
@role_required('patient')
def patient_dashboard():

    return render_template(
        'patient_dashboard.html'
    )