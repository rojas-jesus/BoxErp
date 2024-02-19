from django.contrib.auth.views import LoginView,LogoutView

from django.shortcuts import redirect

from config.settings import LOGIN_REDIRECT_URL

class LogInView(LoginView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)
