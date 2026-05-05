from flask import render_template, request, redirect, Blueprint
from routes.utils import role_required

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route('/appointments', methods=['GET', 'POST'])
@role_required('receptionist')
def appointments():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()

    cur.execute("SELECT * FROM doctors")
    doctors = cur.fetchall()

    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        appointment_date = request.form['date']

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
            INSERT INTO appointments (patient_id, doctor_id, appointment_date)
            VALUES (%s, %s, %s)
        """, (patient_id, doctor_id, appointment_date))

        mysql.connection.commit()

        return redirect('/appointments')

    return render_template('appointments.html', patients=patients, doctors=doctors)