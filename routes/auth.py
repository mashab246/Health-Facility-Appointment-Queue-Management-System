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

        if role not in ['doctor', 'receptionist']:
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
    from app2 import app, mysql
    # If already logged in → redirect based on role
    if 'user_id' in session:
        role = session.get('role')

        if role == 'doctor':
            return redirect('/doctor/dashboard')
        elif role == 'receptionist':
            return redirect('/reception/dashboard')
        elif role == 'admin':
            return redirect('/admin/dashboard')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = mysql.connection.cursor()
        cur.execute("SELECT user_id, username, password, role FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        # Check user + password
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[3]

            # 🔐 Role-based redirect
            if user[3] == 'doctor':
                return redirect('/doctor/dashboard')
            elif user[3] == 'receptionist':
                return redirect('/reception/dashboard')
            elif user[3] == 'admin':
                return redirect('/admin/dashboard')

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')