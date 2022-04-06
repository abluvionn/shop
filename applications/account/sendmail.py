from django.core.mail import send_mail


def send_confirmation_email(code,email):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail('sugar mommy aibika sends u a massage',full_link,"sabyraibika@gmail.com", [email])
