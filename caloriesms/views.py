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
        user = request.GET.get('user')
        day = request.GET.get('day')
        dmr = queryset2.filter(day=day, user=user)
        print(dmr.values('id'))
        # serialized = FoodDailyMealRecordGetSerializer(instance=queryset, many=True)
        # return Response(serialized.data[0])
        return Response({})


class GetRecommendationCaloriesView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        queryset = BmiGoal.objects.all()
        baseline_activity = request.GET.get('baseline_activity')
        goal = request.GET.get('goal')
        bmi = request.GET.get('bmi')
        print(queryset)
        data = queryset.filter(baseline_activity=baseline_activity)
        print("iiiiiiiiiiii")
        print(data)
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
    try:
        data = request.data
        user = User.objects.get(id=data[0]['user'])

        try:
            print(data)
            dmr_in = DailyMealRecord.objects.filter(Q(user=user) & Q(day=data[0]['day']))
            print(dmr_in)
            if len(dmr_in) == 0:
                print('fffff')
                dmr = DailyMealRecord.objects.create(
                    user=user,
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
                response = {'save': True}
            else:
                response = {'save': False}

        except:
            response = {'save': False}
    except:
        response = {'save': False}

    return Response(response)


# [
# {
#     "user": 1,
#     "food": "name",
#     "day": "monday"
# },
# ]


@api_view(["GET"])
@permission_classes([AllowAny])
def DailyFoodGetView(request):
    user = request.GET.get('user')
    day = request.GET.get('day')

    data = DailyMealRecord.objects.filter(user=User.objects.get(id=user))
    print(data)
    if len(data) == 1:
        if data[0].day == day:
            print("her========e")
            data2 = FoodDailyMealRecord.objects.filter(daily_meal_record=data[0])
            # daily_meal_record = data[0]
            print(data2)
        foods = []
        print(data[0].total_calories)
        for d in data2:
            foods.append(
                {
                    "food": d.food.name
                }
            )
        print(foods)
    else:
        foods = []
    return Response(foods)


@api_view(["GET"])
@permission_classes([AllowAny])
def DailyCaloriesGetView(request, user_id, day):
    data2 = DailyMealRecord.objects.values('day', 'date', 'total_calories').filter(Q(user=User.objects.get(id=user_id)) & Q(day=day))
    # d2 = [entry for entry in data2]
    response = {'total_calories': ''}
    if len(data2) == 1:
        response = data2[0]
    else:
        pass
    print(response)

    return Response(response)


@api_view(["POST"])
@permission_classes([AllowAny])
def UpdateProfileView(request):
    data = request.data
    try:
        print(data)
        profile = Profile.objects.get(id=data['profile'])
        profile.goal = Goal.objects.get(id=data['goal'])
        profile.age = data['age']
        profile.baseline_activity = BaseLineActivity.objects.get(id=data['baseline_activity'])
        profile.height = data['height']
        profile.weight = data['weight']
        profile.bmi = data['bmi']
        profile.dietary_restriction = data['dietary_restriction']
        profile.save()
        response = {'save': True}
        return Response(response)
    except:
        response = {'save': False}
        return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def DeleteToDayFoodsView(request):
    user = request.GET.get('user')
    day = request.GET.get('day')
    data = DailyMealRecord.objects.filter(Q(user=User.objects.get(id=user)) & Q(day=day))
    print(len(data))
    if len(data) == 0:
        response = {'delete': False}
    else:
        data[0].delete()
        response = {'delete': True}
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def GetProfileOnly(request, user_id):
    print(User.objects.get(id=user_id))
    profile = Profile.objects.filter(user=User.objects.get(id=user_id))[0]
    bmis = Bmi.objects.all()
    print('BMI OF USER', x.bmi)
    bmi_name = None
    for d in bmis:
        if bmi_name is None:
            if d.min_range <= x.bmi <= d.max_range:
                bmi_name = d.name
        else:
            break
    if bmi_name is None:
        bmi_name = "Overweight"
        
    data = {
        "id": profile.id,
        "gender": profile.gender,
        "goal": profile.goal.name,
        "age": profile.age,
        "baseline_activity_id": profile.baseline_activity.id,
        'bmi': profile.bmi,
        'bmi_name': bmi_name,
        'goal_id': profile.goal.id,
        'baseline_activity': profile.baseline_activity.name,
        'height': profile.height,
        'weight': profile.weight,
    }

    return Response(data)
