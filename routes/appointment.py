from flask import render_template, request, redirect, Blueprint, session
from routes.utils import role_required

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route('/appointments', methods=['GET', 'POST'])
@role_required(
    'receptionist',
    'patient'
)
def appointments():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()

    cur.execute("SELECT * FROM doctors")
    doctors = cur.fetchall()

    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        appointment_date = request.form['date']
        appointment_time = request.form['time']
        
        

        if session['role'] == 'patient':
            patient_id = session['patient_id']
        else:
            patient_id = request.form['patient_id']

        # Prevent double booking
        cur.execute("""
            SELECT * FROM appointments 
            WHERE doctor_id=%s AND appointment_date=%s
        """, (doctor_id, appointment_date))

        if cur.fetchone():
            return render_template(
                'appointments.html',
                patients=patients,
                doctors=doctors,
                error="Doctor is already booked for this date."
            )

        cur.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
            VALUES (%s, %s, %s, %s)
        """, (patient_id, doctor_id, appointment_date, appointment_time))

        mysql.connection.commit()

        return redirect('/appointments')

    return render_template('appointments.html', patients=patients, doctors=doctors)