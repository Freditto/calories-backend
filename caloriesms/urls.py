from .views import *
from django.urls import path
app_name = 'caloriesms'

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('goal', GoalView.as_view()),
    path('baseline-activity', BaselineActivityView.as_view()),
    path('bmi', BmiView.as_view()),
    path('feedback', FeedbackView.as_view()),
    path('daily-meal-record', DailyMealRecordView.as_view()),
    path('food', FoodView.as_view()),
    path('food-daily-meal-record', FoodDailyMealRecordView.as_view()),
    path('recommendation-calories', GetRecommendationCaloriesView.as_view()),
    path('recommendation-exercise', GetRecommendationExerciseView.as_view()),
]
