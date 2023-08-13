from django.shortcuts import render
from rest_framework import generics

from men.models import Men
from men.serializers import MenSerializer


class MenView(generics.ListAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer