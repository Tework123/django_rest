from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from men.models import Men, Category
from men.serializers import MenSerializer


# class MenView(generics.ListAPIView):
#     queryset = Men.objects.all().select_related('category')
#     print(Men.objects.all().select_related('category'))
#     serializer_class = MenSerializer

class MenView(APIView):
    def get(self, request):
        mens = Men.objects.all().values()
        return Response({'mens': mens})

    def post(self, request):
        category_object = Category.objects.get(id=request.data['category'])
        print(category_object)
        photo = request.FILES['photo']
        print(photo)
        with open(photo, 'rb') as f:
            contents = f.read()

        new_men = Men.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            photo=photo,
            category=category_object
        )

        return Response({'new_men': model_to_dict(new_men)})
