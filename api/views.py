import json
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class UserRegistration(APIView):
    """ Simple base registration class 
        Checking payload and creating new user, nothing else """

    def post(self, request):
        payload = request.data

        # Checking payload keys
        if not self.check_payload(payload):
            return Response({"detail": '"email" and "password" fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        email = payload['email']
        password = payload['password']

        # Checking if user already excists
        if User.objects.filter(email=email).exists():
            return Response({"detail": 'User with such email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Creating new user
        user = User.objects.create_user(email, password)
        user.save()

        return Response({"detail": "User сreated successfully."}, status=status.HTTP_201_CREATED)   

    def check_payload(self, payload):
        if not 'email' in payload or not 'password' in payload:
            return False
        else:
            return True
        

class GetUserEmail(APIView):
    """ Simple class to check if user has JWToken """

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        userEmail = request.user.email
        return Response({"detail": userEmail})