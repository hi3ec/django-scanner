from django.urls import path
from .views import home, dashboard,  tables

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('tables/', tables, name="tables"),
]