from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .token import get_user_token
from .models import User
from django.views import generic
from caloriesms.models import *

# Create your views here.

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method == "POST":
        data = request.data
        username = data['username']
        # user = None
        user = User.objects.filter(username=username)
        if user:
            message = {'message': 'user does exist'}
            return Response(message)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
        else:
            message = {'save': False}
            return Response(message)
    return Response({'message': "register view"})


# {
#     "username":"mike",
#     "email":"mike@gmail.com",
#     "password":"123",
#     "phone":"0686666622",
# }

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        my_user = User.objects.values('id', 'username', 'email', 'password', 'phone').get(username=username)
        profile_to_check = Profile.objects.filter(user=User.objects.get(username=username))
        if len(profile_to_check) == 0:
            profile_data={}
            profile = False
        else:
            profile = True
            x = Profile.objects.filter(user=User.objects.get(username=username))[0]
            bmis = Bmi.objects.all()
            for d in bmis:
                if d.min_range <= x.bmi <= d.max_range:
                    bmi_name = d.name
                else:
                    continue

            profile_data = {
                'gender': x.gender,
                'goal': x.goal.name,
                'age': x.age,
                'baseline_activity_id': x.baseline_activity.id,
                # 'bmi_id': x.bmi.id,
                'bmi': x.bmi,
                'bmi_name': bmi_name,
                'goal_id': x.goal.id,
                'baseline_activity': x.baseline_activity.name,
                'height': x.height,
                'weight': x.weight,
            }
        response = {
            'msg': 'success',
            'tokens': get_user_token(user),
            'user': my_user,
            'profile': profile,
            'profile_data': profile_data
        }

        return Response(response)
    else:
        response = {
            'msg': 'Invalid username or password',
        }

        return Response(response)

# {
#     "username": "mike",
#     "password": "123"
# }


