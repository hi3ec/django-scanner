from django.urls import path
from .views import home, dashboard, login, tables

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login/', login, name="login"),
    path('tables/', tables, name="tables"),
]