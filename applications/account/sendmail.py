from django.core.mail import send_mail


def send_confirmation_email(code,email):
    full_link = f'http://localhost:8000/acoount/activate/{code}'
    send_mail('hello',full_link,[email])