from django.shortcuts import render, redirect
from .models import Meal, Workout, Expense
from .forms import MealForm, WorkoutForm, ExpenseForm

def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'core/meal_list.html', {'meals': meals})

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'core/workout_list.html', {'workouts': workouts})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'core/expense_list.html', {'expenses': expenses})


def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'core/add_meal.html', {'form': form})

def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'core/add_workout.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'core/add_expense.html', {'form': form})