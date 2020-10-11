from django.urls import path
from django.views.generic.base import TemplateView
from .views import SignUpView, login


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
 #   path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('login/', login, name="login"),
]
