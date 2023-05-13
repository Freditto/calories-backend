from rest_framework import serializers
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated


class GoalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'name'
        ]


class GoalGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'id',
            'name'
        ]
        depth = 2


class BaseLineActivityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLineActivity
        fields = [
            'name'
        ]


class BaseLineActivityGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLineActivity
        fields = [
            'id',
            'name'
        ]
        depth = 2


class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'gender',
            'goal',
            'age',
            'height',
            'weight',
            'bmi',
            'dietary_restriction'
        ]


class ProfileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseLineActivity
        fields = [
            'id',
            'user',
            'gender',
            'goal',
            'age',
            'height',
            'weight',
            'bmi',
            'dietary_restriction'
        ]
        depth = 2


class BmiPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bmi
        fields = [
            'name',
            'max_range',
            'min_range'
        ]


class BmiGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bmi
        fields = [
            'id',
            'name',
            'max_range',
            'min_range'
        ]
        depth = 2


class BmiGoalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmiGoal
        fields = [
            'baseline_activity',
            'goal',
            'bmi',
            'calories'
        ]


class BmiGoalGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmiGoal
        fields = [
            'id',
            'baseline_activity',
            'goal',
            'bmi',
            'calories'
        ]
        depth = 2


class DailyMealRecordPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMealRecord
        fields = [
            'user',
            'date',
            'day',
            'total_calories'
        ]


class DailyMealRecordGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMealRecord
        fields = [
            'id',
            'user',
            'date',
            'day',
            'total_calories'
        ]
        depth = 2


class FoodPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'name',
            'food_type',
            'service_size',
            'calories',
            # 'is_vegetarian_food'
        ]


class FoodGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'food_type',
            'service_size',
            'calories',
            'is_vegetarian_food'
        ]
        depth = 2


class FoodDailyMealRecordPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDailyMealRecord
        fields = [
            'daily_meal_record',
            'food'
        ]


class FoodDailyMealRecordGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDailyMealRecord
        fields = [
            'id',
            'daily_meal_record',
            'food'
        ]
        depth = 2


class FeedbackPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'user',
            'feedback',
        ]


class FeedbackGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'id',
            'user',
            'feedback',
            'created_at'
        ]
        depth = 2


class ExerciseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'bmi'
        ]
        depth = 2

