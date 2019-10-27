from .models import Essay
from rest_framework import serializers
#모델폼과 비슷한 역할을 함, 모델을 기반으로 작성.
class UserSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ['pk', 'author_name', 'title', 'body']
