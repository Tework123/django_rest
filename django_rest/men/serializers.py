from rest_framework import serializers

from men.models import Men


class MenSerializer(serializers.ModelSerializer):
    # расширяем стандартный класс
    class Meta:
        model = Men
        fields = ('title', 'category')