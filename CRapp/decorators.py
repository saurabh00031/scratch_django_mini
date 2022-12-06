from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test




def police_required(function=None, name=REDIRECT_FIELD_NAME, login_url='sign_police'):
    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_police, login_url=login_url)
    if function:
        return actual_decorator(function)
    return actual_decorator



















    