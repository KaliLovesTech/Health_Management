from django import forms
from .models import Meal, Workout, Expense

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'