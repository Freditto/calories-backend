from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializer import *
from .models import *
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

class ProfileView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serialized = ProfilePostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)

        return Response(serialized.errors)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Profile.objects.all()
        user = request.GET.get('user_id')
        serialized = ProfileGetSerializer(instance=queryset.filter(user=user), many=True)
        return Response(serialized.data)


class GoalView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Goal.objects.all()
        serialized = GoalGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class BaselineActivityView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = BaseLineActivity.objects.all()
        serialized = BaseLineActivityGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class BmiView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Bmi.objects.all()
        serialized = BmiGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class FeedbackView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serialized = FeedbackPostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.validated_data)

        return Response(serialized.errors)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Feedback.objects.all()
        serialized = FeedbackGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class DailyMealRecordView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serialized = DailyMealRecordPostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.validated_data)

        return Response(serialized.errors)

    # [
    # {
    #     "food": 1,
    #     "date": "12-12-2023",
    #     "day": "monday"
    # },
    # ]

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = DailyMealRecord.objects.all()
        serialized = DailyMealRecordGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class FoodView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serialized = FoodPostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.validated_data)

        return Response(serialized.errors)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Food.objects.all()
        serialized = FoodGetSerializer(instance=queryset, many=True)
        return Response(serialized.data)


class FoodDailyMealRecordView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serialized = FoodDailyMealRecordPostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.validated_data)

        return Response(serialized.errors)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = FoodDailyMealRecord.objects.all()
        queryset2 = DailyMealRecord.objects.all()
        user=request.GET.get('user')
        day=request.GET.get('day')
        dmr = queryset2.filter(day=day, user=user)
        serialized = FoodDailyMealRecordGetSerializer(instance=queryset.filter(id=dmr[0].id), many=True)
        return Response(serialized.data)


class GetRecommendationCaloriesView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = BmiGoal.objects.all()
        baseline_activity = request.GET.get('baseline_activity')
        goal = request.GET.get('goal')
        bmi = request.GET.get('bmi')
        data = queryset.filter(baseline_activity=baseline_activity, goal=goal, bmi=bmi)
        serialized = BmiGoalGetSerializer(instance=data, many=True)
        return Response(serialized.data)


class GetRecommendationExerciseView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Exercise.objects.all()
        bmi = request.GET.get('bmi')
        data = queryset.filter(bmi=bmi)
        serialized = ExerciseGetSerializer(instance=data, many=True)
        return Response(serialized.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def DailyFoodView(request):
    data = request.data
    dmr = DailyMealRecord.objects.create(
        user=User.objects.get(id=data[0]['user']),
        # date=data[0]['date'],
        day=data[0]['day']
    )
    tc = 0
    for d in data:
        fdmr = FoodDailyMealRecord.objects.create(
            daily_meal_record=dmr,
            food=Food.objects.get(name=d['food'])
        )
        fdmr.save()
        f = Food.objects.get(name=d['food'])
        tc = tc + f.calories
    dmr.total_calories = tc
    dmr.save()
    return Response({"message": "success"})


# [
    # {
    #     "user": 1,
    #     "food": "name",
    #     "day": "monday"
    # },
# ]


@api_view(["GET"])
@permission_classes([AllowAny])
def DailyFoodGetView(request, user_id, day):
    data = DailyMealRecord.objects.values('day', 'date', 'total_calories').filter(Q(user=User.objects.get(id=user_id)) and Q(day=day))
    print(data)
    return Response(data[0])
