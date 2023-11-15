"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# we need to import views in order to handle django login and logout. The code below is the written so that can create the paths for our 
# login and logout page views
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from todo_list import views (planning to remove this later on as it dosent have any function i think)
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('todo_list.urls')), 
]

# django usually has a default directory where it looks for file. In the case of the login template file, 
# I am telling django where it should look into for the login template path. And I did that by setting the desired template path
# into the login as_view function.

# And in the case of the logout view, django has a default logout view but I dont want to use that(I cannot use that), as this will expose other users to our 
# admin login page. So I needed to tell the logout view that I am using a different template view just as I did with the login view.
 