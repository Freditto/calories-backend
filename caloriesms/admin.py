from django.contrib import admin
from .models import *

# Register your models here.
x = [Profile, Goal, BmiGoal, Bmi, BaseLineActivity, DailyMealRecord, Food, FoodDailyMealRecord, Feedback]
for d in x:
    admin.site.register(d)
