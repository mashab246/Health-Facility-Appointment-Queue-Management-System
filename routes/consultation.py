from flask import render_template, request, redirect, Blueprint
from routes.utils import role_required

consultation_bp = Blueprint("consultation", __name__)

@consultation_bp.route('/consult/<int:queue_id>')
@role_required('doctor')
def start_consultation(queue_id):
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("""
        UPDATE queue SET status='in_progress'
        WHERE queue_id=%s
    """, (queue_id,))

    mysql.connection.commit()

    return redirect(f'/consult/{queue_id}/form')


@consultation_bp.route('/consult/<int:queue_id>/form', methods=['GET', 'POST'])
def consultation_form(queue_id):
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT queue.queue_id, patients.patient_id, patients.first_name,
       patients.last_name
        FROM queue
        JOIN patients ON queue.patient_id = patients.patient_id
        WHERE queue.queue_id = %s
    """, (queue_id,))

    data = cur.fetchone()

    if request.method == 'POST':
        notes = request.form['notes']
        doctor_id = 1

        cur.execute("""
            INSERT INTO consultations (patient_id, doctor_id, consultation_notes)
            VALUES (%s, %s, %s)
        """, (data[1], doctor_id, notes))

        cur.execute("""
            UPDATE queue SET status='done'
            WHERE queue_id=%s
        """, (queue_id,))

        mysql.connection.commit()

        return redirect('/queue')

    return render_template('consultation.html', patient=data)