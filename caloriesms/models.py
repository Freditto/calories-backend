from django.db import models
from authUser.models import User


# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'Goal'


class BaseLineActivity(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'Baseline_activity'


class Profile(models.Model):
    choice = (('male', 'male'), ('female', 'female'))
    dietary = (('vegetarian', 'vegetarian'), ('free', 'free'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=choice)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    age = models.IntegerField()
    baseline_activity = models.ForeignKey(BaseLineActivity, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.FloatField()
    dietary_restriction = models.CharField(max_length=20, choices=dietary)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        db_table = 'Profile'


class Bmi(models.Model):
    name = models.CharField(max_length=200)
    max_range = models.FloatField()
    min_range = models.FloatField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'Bmi'


class BmiGoal(models.Model):
    baseline_activity = models.ForeignKey(BaseLineActivity, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    bmi = models.ForeignKey(Bmi, on_delete=models.CASCADE)
    calories = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.calories}'

    class Meta:
        db_table = 'Bmi_goal'


class DailyMealRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    day = models.CharField(max_length=20)
    total_calories = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'{self.day}'

    class Meta:
        db_table = 'Daily_meal_record'


class Food(models.Model):
    # choice = (('Carbs', 'Carbs'), ('Protein', 'Protein'), ('Fat', 'Fat'))
    name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=200)
    service_size = models.CharField(max_length=200)
    calories = models.DecimalField(max_digits=10, decimal_places=0)
    is_vegetarian_food = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'Food'


class FoodDailyMealRecord(models.Model):
    daily_meal_record = models.ForeignKey(DailyMealRecord, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food.name}'

    class Meta:
        db_table = 'Food_daily_meal_record'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.feedback}'

    class Meta:
        db_table = 'Feedback'


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    calories_burned_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.DecimalField(max_digits=10, decimal_places=2)
    bmi = models.ForeignKey(Bmi, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'Exercise'
