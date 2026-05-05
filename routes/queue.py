from flask import render_template, redirect, Blueprint
from routes.utils import role_required

queue_bp = Blueprint("queue", __name__)

@queue_bp.route('/checkin')
@role_required('receptionist')
def checkin_page():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()

    return render_template('checkin.html', patients=patients)

@queue_bp.route('/queue/add/<int:patient_id>')
def add_to_queue(patient_id):
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    # Prevent duplicate
    cur.execute("""
        SELECT * FROM queue 
        WHERE patient_id=%s AND status='waiting'
    """, (patient_id,))
    
    if cur.fetchone():
        return "Patient is already in the queue."

    # Generate queue number
    cur.execute("SELECT MAX(queue_number) FROM queue")
    last_number = cur.fetchone()[0]

    next_number = 1 if last_number is None else last_number + 1

    cur.execute("""
        INSERT INTO queue (patient_id, queue_number)
        VALUES (%s, %s)
    """, (patient_id, next_number))

    mysql.connection.commit()

    return redirect('/queue')


@queue_bp.route('/queue')
@role_required('receptionist')
def view_queue():
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT queue.queue_id, patients.name, queue.queue_number, queue.status
        FROM queue
        JOIN patients ON queue.patient_id = patients.patient_id
        ORDER BY queue.queue_number ASC
    """)

    queue = cur.fetchall()

    return render_template('queue.html', queue=queue)


@queue_bp.route('/queue/update/<int:queue_id>/<string:status>')
def update_queue(queue_id, status):
    from app2 import app, mysql
    cur = mysql.connection.cursor()

    cur.execute("""
        UPDATE queue SET status=%s WHERE queue_id=%s
    """, (status, queue_id))

    mysql.connection.commit()

    return redirect('/queue')