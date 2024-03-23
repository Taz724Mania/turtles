from django.shortcuts import render
from .models import Turtle
from rest_framework import viewsets, permissions
from .serializer import TurtleSerializer
# Create your views here.
class TurtleViewSet(viewsets.ModelViewSet):
    queryset=Turtle.objects.all()
    serializer_class=TurtleSerializer
    permission_classes=[permissions.AllowAny]
