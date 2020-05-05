from rest_framework import serializers
from apps.projectmini.models import (
    InstaPost
)
class InstaPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = InstaPost
        fields = ('author',
                  'image',
                  'caption',
                  'created_date'
                  )