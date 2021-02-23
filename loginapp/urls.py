from django.urls import path
from loginapp import views

app_name = 'loginapp'

urlpatterns = [
    path('signup/', views.sign_up,name='signup'),
    path('login/', views.login_page, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('profile/', views.profile, name= 'profile'),
    path('change-profile/', views.user_change, name= 'changeprofile'),
    path('password/', views.password_change, name= 'changepassword'),
    path('addprofilepicture/', views.add_profile_pic, name= 'addprofilepicture'),
    path('changeprofilepicture/', views.change_profile_pic, name= 'changeprofilepicture'),


]
