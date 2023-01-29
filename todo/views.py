from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TodoView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user = request.user
        print(f"User: {user}")
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many = True)
        return Response({
            'staus':True,
            'data':serializer.data,
            'manage':'todo fetched successfully'
        })

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.uid
            serializer=TodoSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'staus':False,
                    'data':serializer.errors,
                    'manage':'todo fetched unsuccessfull'
                        })
            serializer.save()
            return Response({
                'staus':True,
                'data':serializer.data,
                'manage':'new todo add successfully'
                })
        except Exception as e:
            print(e)
            return Response({
                'staus':False,
                # 'data':serializer.errors,
                'manage':'try unsuccessfull'
            })