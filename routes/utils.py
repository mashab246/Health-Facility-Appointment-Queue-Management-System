from functools import wraps
from flask import session, redirect

def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if 'role' not in session:
                return redirect('/login')
            if session['role'] != role:
                return "Access denied"
            return f(*args, **kwargs)
        return wrapper
    return decorator