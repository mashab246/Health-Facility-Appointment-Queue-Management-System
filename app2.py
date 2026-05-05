from flask import Flask, render_template, session, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 'super_secret_key'

mysql = MySQL(app)

# Import routes
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.patient import patient_bp
from routes.appointment import appointment_bp
from routes.queue import queue_bp
from routes.consultation import consultation_bp

# Register them
app.register_blueprint(auth_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(queue_bp)
app.register_blueprint(consultation_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect('/login')

    role = session['role']

    if role == 'doctor':
        return redirect('/doctor/dashboard')
    elif role == 'receptionist':
        return redirect('/reception/dashboard')
    elif role == 'admin':
        return redirect('/admin/dashboard')

if __name__ == '__main__':
    app.run(debug=True)