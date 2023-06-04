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

    bmi = [
           {
            "max": "24.9",
            "min": "18.5",
            "description": "Normal"
          },
          {
            "max": "100.0",
            "min": "25.0",
            "description": "Overweight"
          },
          # {
          #   "max": "100.9",
          #   "min": "30.0",
          #   "description": "Obese"
          # },
          {
            "max": "18.5",
            "min": "0.0",
            "description": "Underweight"
          }
        ]
    for data in bmi:
        d = Bmi.objects.create(
            name=data['description'],
            max_range=data['max'],
            min_range=data['min']
        )
        d.save()

    data2 = [
              {
                "activity": "Sedentary",
                "bmi": "Underweight",
                "calories": [
                    {"data": 1600},
                    {"data": 1800},
                    {"data": 2000}
                ]
              },
              {
                "activity": "Sedentary",
                "bmi": "Normal",
                "calories": [
                    {"data": 1800},
                    {"data": 2000},
                    {"data": 2200}
                ]
              },
              {
                "activity": "Sedentary",
                "bmi": "Overweight",
                "calories": [
                    {"data": 2000},
                    {"data": 2200},
                    {"data": 2400}
                ]
              },
              {
                "activity": "Lightly Active",
                "bmi": "Underweight",
                "calories": [
                    {"data": 1800},
                    {"data": 2000},
                    {"data": 2200}
                ]
              },
              {
                "activity": "Lightly Active",
                "bmi": "Normal",
                "calories": [
                    {"data": 2000},
                    {"data": 2200},
                    {"data": 2400}
                ]
              },
              {
                "activity": "Lightly Active",
                "bmi": "Overweight",
                "calories": [
                    {"data": 2200},
                    {"data": 2400},
                    {"data": 2600}
                ]
              },
              {
                "activity": "Moderately Active",
                "bmi": "Underweight",
                "calories": [
                    {"data": 2000},
                    {"data": 2200},
                    {"data": 2400}
                ]
              },
              {
                "activity": "Moderately Active",
                "bmi": "Normal",
                "calories": [
                    {"data": 2200},
                    {"data": 2400},
                    {"data": 2600}
                ]
              },
              {
                "activity": "Moderately Active",
                "bmi": "Overweight",
                "calories": [
                    {"data": 2400},
                    {"data": 2600},
                    {"data": 2800}
                ]
              },
              {
                "activity": "Very Active",
                "bmi": "Underweight",
                "calories": [
                    {"data": 2200},
                    {"data": 2400},
                    {"data": 2600}
                ]
              },
              {
                "activity": "Very Active",
                "bmi": "Normal",
                "calories": [
                    {"data": 2400},
                    {"data": 2600},
                    {"data": 2800}
                ]
              },
              {
                "activity": "Very Active",
                "bmi": "Overweight",
                "calories": [
                    {"data": 2600},
                    {"data": 2800},
                    {"data": 3000}
                ]
              }
            ]
    for data in data2:
        go_l = ['loss', 'maintain', 'gain']
        x=0
        for d in data['calories']:
            g = Goal.objects.get(name=go_l[x])
            activ = BaseLineActivity.objects.get(name=data['activity'])
            bmi_d = Bmi.objects.get(name=data['bmi'])
            s = BmiGoal.objects.create(
                baseline_activity=activ,
                goal=g,
                bmi=bmi_d,
                calories=d['data']
            )
            s.save()


    data3 = [
        {
            "name": "Noodle",
            "type": "pasta",
            "serving_amount": "1 cup",
            "calories": 221,
            "vegetarian": True
        },
        {
            "name": "Soup",
            "type": "soup",
            "serving_amount": "1 cup",
            "calories": 100,
            "vegetarian": True
        },
        {
            "name": "Pizza",
            "type": "snack",
            "serving_amount": "1 slice",
            "calories": 285,
            "vegetarian": True
        },
        {
            "name": "Rice",
            "type": "grain",
            "serving_amount": "1 cup",
            "calories": 205,
            "vegetarian": True
        },
        {
            "name": "Roasted meat",
            "type": "protein",
            "serving_amount": "3 oz",
            "calories": 250,
            "vegetarian": False
        },
        {
            "name": "Roasted fish",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 200,
            "vegetarian": False
        },
        {
            "name": "Fried fish",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 180,
            "vegetarian": False
        },
        {
            "name": "Fried chicken",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 250,
            "vegetarian": False
        },
        {
            "name": "Banana",
            "type": "fruit",
            "serving_amount": "1 medium",
            "calories": 105,
            "vegetarian": True
        },
          {
            "name": "Broccoli",
            "type": "vegetable",
            "serving_amount": "1 cup (91g)",
            "calories": 55,
            "vegetarian": True
          },
          {
            "name": "Salmon",
            "type": "protein",
            "serving_amount": "3 oz (85g)",
            "calories": 175,
            "vegetarian": False
          },
          {
            "name": "Brown Rice",
            "type": "carbohydrate",
            "serving_amount": "1 cup cooked (195g)",
            "calories": 216,
            "vegetarian": True
          },
          {
            "name": "Avocado",
            "type": "fat",
            "serving_amount": "1/2 medium (68g)",
            "calories": 114,
            "vegetarian": True
          },
          {
            "name": "Sweet Potato",
            "type": "carbohydrate",
            "serving_amount": "1 medium (114g)",
            "calories": 103,
            "vegetarian": True
          },
          {
            "name": "Almonds",
            "type": "fat",
            "serving_amount": "1/4 cup (28g)",
            "calories": 160,
            "vegetarian": True
          },
          {
            "name": "Black Beans",
            "type": "protein",
            "serving_amount": "1/2 cup (86g)",
            "calories": 114,
            "vegetarian": True
          },
          {
            "name": "Spinach",
            "type": "vegetable",
            "serving_amount": "1 cup (30g)",
            "calories": 7,
            "vegetarian": True
          },
          {
            "name": "Eggs",
            "type": "protein",
            "serving_amount": "1 large (50g)",
            "calories": 78,
            "vegetarian": False
          },
          {
            "name": "Greek Yogurt",
            "type": "protein",
            "serving_amount": "1 cup (227g)",
            "calories": 130,
            "vegetarian": False
          },
          {
            "name": "Oatmeal",
            "type": "carbohydrate",
            "serving_amount": "1/2 cup dry (40g)",
            "calories": 150,
            "vegetarian": True
          },
        {
            "name": "Rice",
            "type": "grain",
            "serving_amount": "1 cup",
            "calories": 205,
            "vegetarian": True
        },
        {
            "name": "Ugali",
            "type": "starch",
            "serving_amount": "1 piece",
            "calories": 350,
            "vegetarian": True
        },
        {
            "name": "Dough",
            "type": "bread",
            "serving_amount": "1 piece",
            "calories": 100,
            "vegetarian": True
        },
        {
            "name": "Fried fish",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 180,
            "vegetarian": False
        },
        {
            "name": "Fried chicken",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 250,
            "vegetarian": False
        },
        {
            "name": "Beans",
            "type": "protein",
            "serving_amount": "1 cup",
            "calories": 220,
            "vegetarian": True
        },
        {
            "name": "Coconut peas",
            "type": "vegetable",
            "serving_amount": "1 cup",
            "calories": 180,
            "vegetarian": True
        },
        {
            "name": "Roasted fish",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 200,
            "vegetarian": False
        },
        {
            "name": "Roasted meat",
            "type": "protein",
            "serving_amount": "3 oz",
            "calories": 250,
            "vegetarian": False
        },
        {
            "name": "Banana meat",
            "type": "fruit",
            "serving_amount": "1 piece",
            "calories": 120,
            "vegetarian": True
        },
        {
            "name": "Spinach",
            "type": "vegetable",
            "serving_amount": "1 cup",
            "calories": 7,
            "vegetarian": True
        },
        {
            "name": "Pilau",
            "type": "rice",
            "serving_amount": "1 cup",
            "calories": 350,
            "vegetarian": True
        },
        {
            "name": "Chips",
            "type": "snack",
            "serving_amount": "1 cup",
            "calories": 312,
            "vegetarian": True
        },
        {
            "name": "Egg chop",
            "type": "snack",
            "serving_amount": "1 piece",
            "calories": 150,
            "vegetarian": False
        },
        {
            "name": "Fried bread",
            "type": "bread",
            "serving_amount": "1 piece",
            "calories": 200,
            "vegetarian": True
        },
        {
            "name": "Chapati",
            "type": "bread",
            "serving_amount": "1 piece",
            "calories": 120,
            "vegetarian": True
        },
        {
            "name": "Sausage",
            "type": "protein",
            "serving_amount": "1 piece",
            "calories": 250,
            "vegetarian": False
        },
        {
            "name": "Frying eggs",
            "type": "protein",
            "serving_amount": "2 eggs",
            "calories": 140,
            "vegetarian": False
        },
        {
            "name": "Boiled egg",
            "type": "protein",
            "serving_amount": "1 egg",
            "calories": 78,
            "vegetarian": False
        },
        {
            "name": "Sponge cake",
            "type": "dessert",
            "serving_amount": "1 slice",
            "calories": 220,
            "vegetarian": True
        },
        {
            "name": "Donut",
            "type": "dessert",
            "serving_amount": "1 piece",
            "calories": 260,
            "vegetarian": True
        },
        {
            "name": "Boiled cassava",
            "type": "starch",
            "serving_amount": "1 cup",
            "calories": 330,
            "vegetarian": True
        },
        {
            "name": "Coffee",
            "type": "beverage",
            "serving_amount": "1 cup",
            "calories": 2,
            "vegetarian": True
        },
        {
            "name": "Tea",
            "type": "beverage",
            "serving_amount": "1 cup",
            "calories": 2,
            "vegetarian": True
        },
        {
            "name": "Milk",
            "type": "beverage",
            "serving_amount": "1 cup",
            "calories": 103,
            "vegetarian": True
        },
        {
            "name": "Smoothie",
            "type": "beverage",
            "serving_amount": "1 cup",
            "calories": 150,
            "vegetarian": True
        },
        {
            "name": "Yogurt",
            "type": "dairy",
            "serving_amount": "1 cup",
            "calories": 150,
            "vegetarian": True
        },
        {
            "name": "Coffee with milk",
            "type": "beverage",
            "serving_amount": "1 cup",
            "calories": 30,
            "vegetarian": True
        }
        ]
    for data in data3:
        food = Food.objects.create(
            name=data['name'],
            food_type=data['type'],
            service_size=data['serving_amount'],
            calories=data['calories'],
            is_vegetarian_food=data['vegetarian']
        )
        food.save()

    data4 = [
              {
              "bmi": "Underweight",
                "goal": "Lose weight",
                "exercise": [
                  {
                    "name": "Jogging",
                    "calories_burned_per_hour": 400,
                    "duration_minutes": 60
                  },
                  {
                    "name": "Cycling",
                    "calories_burned_per_hour": 500,
                    "duration_minutes": 45
                  },
                  {
                    "name": "Swimming",
                    "calories_burned_per_hour": 600,
                    "duration_minutes": 30
                  }
                ]
              },
              {
                "bmi": "Normal",
                "goal": "Maintain weight",
                "exercise": [
                  {
                    "name": "Yoga",
                    "calories_burned_per_hour": 200,
                    "duration_minutes": 60
                  },
                  {
                    "name": "Walking",
                    "calories_burned_per_hour": 250,
                    "duration_minutes": 30
                  },
                  {
                    "name": "Pilates",
                    "calories_burned_per_hour": 300,
                    "duration_minutes": 45
                  }
                ]
              },
              {
                "bmi": "Overweight",
                "goal": "Gain weight",
                "exercise": [
                  {
                    "name": "Weight lifting",
                    "calories_burned_per_hour": 400,
                    "duration_minutes": 60
                  },
                  {
                    "name": "CrossFit",
                    "calories_burned_per_hour": 500,
                    "duration_minutes": 45
                  },
                  {
                    "name": "Boxing",
                    "calories_burned_per_hour": 600,
                    "duration_minutes": 30
                  }
                ]
              }
            ]
    for data in data4:
        for d in data['exercise']:
            bmi = Bmi.objects.get(name=data['bmi'])
            exercise_save = Exercise.objects.create(
                name=d['name'],
                calories_burned_per_hour=d['calories_burned_per_hour'],
                duration_minutes=d['duration_minutes'],
                bmi=bmi
            )
            exercise_save.save()










