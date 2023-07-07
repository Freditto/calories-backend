from .views import *
from .tosavedata import *
from django.urls import path
app_name = 'caloriesms'

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('update-profile', UpdateProfileView),
    path('goal', GoalView.as_view()),
    path('baseline-activity', BaselineActivityView.as_view()),
    path('bmi', BmiView.as_view()),
    path('feedback', FeedbackView.as_view()),
    path('daily-meal-record', DailyMealRecordView.as_view()),
    path('food', FoodView.as_view()),
    path('daily-food', DailyFoodView),
    path('food-daily-meal-record', DailyFoodGetView),
    path('delete-food-daily-meal-record', DeleteToDayFoodsView),
    path('daily-food-get/<int:user_id>/<slug:day>', DailyCaloriesGetView),
    # path('food-daily-meal-record', FoodDailyMealRecordView.as_view()),
    path('food-daily-meal-record', FoodDailyMealRecordView.as_view()),
    path('recommendation-calories', GetRecommendationCaloriesView.as_view()),
    path('recommendation-exercise', GetRecommendationExerciseView.as_view()),
    path('get-updated-profile/<int:user_id>', GetProfileOnly),
    # path('demo', demo)
]
