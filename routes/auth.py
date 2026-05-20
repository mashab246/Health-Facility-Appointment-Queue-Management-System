from flask import render_template, request, redirect, session, Blueprint
from werkzeug.security import check_password_hash


auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register-user', methods=['GET', 'POST'])
def register_user():

    from werkzeug.security import generate_password_hash
    from app2 import mysql

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        if role not in ['doctor', 'receptionist', 'patient']:
            return "Invalid role selected"

        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s",
            (username,)
        )

        existing_user = cur.fetchone()

        if existing_user:
            cur.close()
            return render_template(
                'register_user.html',
                error="Username already exists"
            )

        cur.execute(
            """
            INSERT INTO users(username, password, role)
            VALUES(%s, %s, %s)
            """,
            (username, hashed_password, role)
        )

        mysql.connection.commit()

        user_id = cur.lastrowid

        if role == 'doctor':

            full_name = request.form['full_name']
            specialization = request.form['specialization']
            department = request.form['department']
            phone = request.form['phone']
            email = request.form['email']

            cur.execute(
                """
                INSERT INTO doctors(
                    user_id,
                    full_name,
                    specialization,
                    department,
                    phone,
                    email
                )
                VALUES(%s, %s, %s, %s, %s, %s)
                """,
                (
                    user_id,
                    full_name,
                    specialization,
                    department,
                    phone,
                    email
                )
            )

            mysql.connection.commit()


        elif role == 'receptionist':

            full_name = request.form['receptionist_name']
            phone = request.form['receptionist_phone']
            email = request.form['receptionist_email']
            shift_time = request.form['shift_time']

            cur.execute(
                """
                INSERT INTO receptionists(
                    user_id,
                    full_name,
                    phone,
                    email,
                    shift_time
                )
                VALUES(%s, %s, %s, %s, %s)
                """,
                (
                    user_id,
                    full_name,
                    phone,
                    email,
                    shift_time
                )
            )

            mysql.connection.commit()

        cur.close()

        return redirect('/login')

    return render_template('register_user.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    from app2 import mysql

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s",
            (username,)
        )

        user = cur.fetchone()

        cur.close()

        # Check if user exists
        if user:

            # user[2] = password column
            if check_password_hash(user[2], password):

                session['user_id'] = user[0]
                session['username'] = user[1]
                session['role'] = user[3]

                # Redirect based on role
                if user[3] == 'doctor':
                    return redirect('/doctor/dashboard')

                elif user[3] == 'receptionist':
                    return redirect('/reception/dashboard')

                elif user[3] == 'patient':
                    return redirect('/patient/dashboard')

                else:
                    return redirect('/')

            else:
                return render_template(
                    'login.html',
                    error='Invalid password'
                )

        else:
            return render_template(
                'login.html',
                error='User does not exist'
            )

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@auth_bp.route('/patient-register', methods=['GET', 'POST'])
def patient_register():

    from werkzeug.security import generate_password_hash
    from app2 import mysql

    if request.method == 'POST':

        # USER ACCOUNT DATA
        username = request.form['username']
        password = generate_password_hash(
            request.form['password']
        )

        role = 'patient'

        # PATIENT DATA
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        emergency_contact = request.form['emergency_contact']

        cur = mysql.connection.cursor()

        # CHECK DUPLICATE USERNAME
        cur.execute(
            "SELECT * FROM users WHERE username=%s",
            (username,)
        )

        if cur.fetchone():

            return render_template(
                'patient_register.html',
                error="Username already exists"
            )

        # CREATE USER ACCOUNT
        cur.execute("""
            INSERT INTO users(
                username,
                password,
                role
            )
            VALUES(%s, %s, %s)
        """, (
            username,
            password,
            role
        ))

        mysql.connection.commit()

        user_id = cur.lastrowid

        # CREATE PATIENT PROFILE
        cur.execute("""
            INSERT INTO patients(
                user_id,
                first_name,
                last_name,
                gender,
                date_of_birth,
                phone,
                email,
                address,
                emergency_contact
            )
            VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s
            )
        """, (
            user_id,
            first_name,
            last_name,
            gender,
            date_of_birth,
            phone,
            email,
            address,
            emergency_contact
        ))

        mysql.connection.commit()

        cur.close()

        return redirect('/login')

    return render_template('patient_register.html')

