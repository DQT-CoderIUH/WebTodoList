from django.contrib import admin
from django.urls import path
from app.views import Home, Login, SignUp, add_todo, signout, delete_todo, change_todo



urlpatterns = [
    path('', Home , name= 'Home' ),
    path('login', Login, name= 'login'),
    path('signup', SignUp),
    path('add-todo', add_todo),
    path('delete-todo/<int:id>', delete_todo), 
    path('change-status/<int:id>/<str:status>', change_todo), 
    path('logout', signout),
]