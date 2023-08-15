from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from men.models import Men, Category, Message
from men.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from men.serializers import MenSerializer


# class MenView(generics.ListAPIView):
#     queryset = Men.objects.all().select_related('category')
#     print(Men.objects.all().select_related('category'))
#     serializer_class = MenSerializer

#  также есть ReadOnlyModelViewSet
# class MenViewSet(viewsets.ModelViewSet):
#     # queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
#     # переопределяем queryset, нужно обязательно basename прописать в routes url
#     def get_queryset(self):
#         return Men.objects.all()
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         return Response({'categories': category.name})


# # заменяет get и post
class MenViewList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # только по токенам можно получить доступ
    authentication_classes = (TokenAuthentication,)


# # заменяет patch и put
# class MenViewUpdate(generics.UpdateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
#
# # заменяет patch и put get delete
class MenViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAdminOrReadOnly, IsOwnerOrReadOnly)

# class MenView(APIView):
#     def get(self, request):
#         mens = Men.objects.all()
#         print(mens)
#         return Response({'mens': MenSerializer(mens, many=True).data})
#
#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # photo = request.FILES['photo']
#         # print(photo)
#
#
#         # new_men = Men.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     # photo=photo,
#         #     category=category_object
#         # )
#         return Response({'data': serializer.data})
#         # return Response({'new_men': MenSerializer(new_men).data})
#
#     def put(self, request):
#
#         pk = request.data['pk']
#         if not pk:
#             return Response({'error': 'Fuck'})
#
#         try:
#             instance = Men.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Я не нашел объект'})
#
#         serializer = MenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#
#         # вызывает у нашего сериализатора метод create
#         serializer.save()
#         return Response({'data': serializer.data})
#
#     def delete(self, request):
#         try:
#             pk = request.data['pk']
#         except:
#             return Response({'error': 'Отправь pk довнич'})
#
#         try:
#             Message.objects.get(pk=pk).delete()
#         except:
#             return Response({'error': 'Я не нашел объект'})
#         return Response({'data': 'объект удален'})
