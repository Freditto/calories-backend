from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@api_view(["GET"])
@permission_classes([AllowAny])
def demo(request):
    activity = ["Very Active", "Moderately Active", "Lightly Active", "Sedentary"]
    for data in activity:
        activity_to = BaseLineActivity.objects.create(
        name = data
        )
    goals = ["loss", "maintain", "gain"]
    for data in goals:
        goal = Goal.objects.create(
            name = data
        )

