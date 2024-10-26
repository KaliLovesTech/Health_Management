from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()
    ingredients = models.TextField(help_text="List of ingredients")

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    date = models.DateField(auto_now_add=True)
    exercise = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField(help_text="Weight used in the exercise")

    def __str__(self):
        return f"{self.exercise} on {self.date}"
    
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('grocery', 'Grocery'),
        ('dining_out', 'Dining Out'),
        ('other', 'Other'),
    ]

    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - ${self.amount} on {self.date}"