#from functools import wraps

from flask import session, redirect

def role_required(*roles):

    def wrapper(func):

        def decorated_function(*args, **kwargs):

            if 'role' not in session:
                return redirect('/login')

            if session['role'] not in roles:
                return "Access Denied"

            return func(*args, **kwargs)

        decorated_function.__name__ = func.__name__

        return decorated_function

    return wrapper