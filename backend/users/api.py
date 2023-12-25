from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    users = User.objects.all().order_by('-id')  
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
def create_user(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        created_user = User.objects.get(id=serializer.data['id'])  
        return JsonResponse(UserSerializer(created_user).data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    
