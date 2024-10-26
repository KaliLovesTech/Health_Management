from django.urls import path
from . import views

urlpatterns = [
    path('meals/', views.meal_list, name='meal_list'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('add_expense/', views.add_expense, name='add_expense'),
]