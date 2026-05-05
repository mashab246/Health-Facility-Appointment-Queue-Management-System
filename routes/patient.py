from flask import render_template, request, redirect, Blueprint
from routes.utils import role_required

patient_bp = Blueprint("patient", __name__)

@patient_bp.route('/register', methods=['GET', 'POST'])
@role_required('receptionist')
def register_patient():
    from app2 import app, mysql
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients(name, phone) VALUES(%s, %s)", (name, phone))
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('register.html')