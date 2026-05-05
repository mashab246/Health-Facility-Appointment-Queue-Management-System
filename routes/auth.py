from flask import render_template, request, redirect, session, Blueprint
from werkzeug.security import check_password_hash


auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register-user', methods=['GET', 'POST'])
def register_user():
    from app2 import app, mysql
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Validate role (important)
        if role not in ['doctor', 'receptionist']:
            return "Invalid role selected"

        from werkzeug.security import generate_password_hash
        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()

        # Check duplicate username
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cur.fetchone():
            return "Username already exists"

        cur.execute("""
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
        """, (username, hashed_password, role))

        mysql.connection.commit()

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