from flask import render_template, request, redirect, Blueprint
from routes.utils import role_required

patient_bp = Blueprint("patient", __name__)

@patient_bp.route('/register', methods=['GET', 'POST'])
@role_required('receptionist')
def register_patient():

    from app2 import mysql

    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        emergency_contact = request.form['emergency_contact']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM patients WHERE phone=%s",
            (phone,)
        )

        existing_patient = cur.fetchone()

        if existing_patient:
            cur.close()

            return render_template(
                'register_patient.html',
                error="Patient with this phone number already exists"
            )


        cur.execute(
            """
            INSERT INTO patients(
                first_name,
                last_name,
                gender,
                date_of_birth,
                phone,
                email,
                address,
                emergency_contact
            )
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                first_name,
                last_name,
                gender,
                date_of_birth,
                phone,
                email,
                address,
                emergency_contact
            )
        )

        mysql.connection.commit()

        cur.close()

        return redirect('/reception/dashboard')

    return render_template('register.html')