import requests

from django.contrib.auth import get_user_model, login
from django.conf import settings
from django.shortcuts import redirect


from .models import Profile


UserModel = get_user_model()


def login_with_github(request):
    client_id = settings.GITHUB_CLIENT_ID
    redirect_url = settings.GITHUB_CALLBACK_URL
    url = "https://github.com/login/oauth/authorize?client_id=%s&redirect_uri=%s&scope=read:user"
    return redirect(url % (client_id, redirect_url))


# https://wayhome25.github.io/django/2017/05/18/django-auth/
def github_callback(request):
    code = request.GET.get("code", None)
    client_id = settings.GITHUB_CLIENT_ID
    client_secret = settings.GITHUB_CLIENT_SECRET
    token_request = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
        headers={"Accept": "application/json"},
    )
    token_json = token_request.json()
    access_token = token_json.get("access_token")
    profile_request = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {access_token}",
            "Accept": "application/json",
        },
    )
    profile_json = profile_request.json()
    username = profile_json.get('login', None)
    if username is not None:
        name = profile_json.get('name', '')
        email = profile_json.get("email")
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = UserModel(username=username)
            user.first_name = name
            user.email = email
            user.save()
            user.profile.login_type = Profile.GITHUB
            user.save()
        login(request, user)
        if not user.profile.agree_with_private:
            return redirect('/join')
    return redirect('/')
