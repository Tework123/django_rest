import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from men.models import Men


class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        # поля, которые возвращаются
        # fields = ('title', 'content', 'category')
        fields = '__all__'

# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

#
# class MenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField(max_length=228)
#     time_create = serializers.DateTimeField(required=False)
#     time_update = serializers.DateTimeField(required=False)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Men.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.save()
#         return instance

#
# def encode():
#     model = MenModel('afasf', 'hello')
#     print(model)
#     # кодирует
#     model_res = MenSerializer(model)
#     print(model_res.data, type(model_res), sep='/n')
#     json = JSONRenderer().render(model_res.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"afasf","content":"hello"}')
#     data = JSONParser().parse(stream)
#     print(data)
#     # декодирует
#     serializer = MenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
