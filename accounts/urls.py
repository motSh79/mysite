from django.urls import path
from .views import signup_view, verify_view, login_view, verify_login_view, dashboard_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('verify/', verify_view, name='verify'),
    path('login/', login_view, name='login'),
    path('verify-login/', verify_login_view, name='verify-login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]