from rest_framework import generics
# Create your views here.
from .serializers import TodoSerializer
from .models import TODO

class CreateTodo(generics.ListCreateAPIView):
    
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer



class ViewTodo(generics.ListAPIView):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer


