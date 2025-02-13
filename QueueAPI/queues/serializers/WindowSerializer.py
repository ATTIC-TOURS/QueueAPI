from rest_framework import serializers
from queues.models import Window


class WindowSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Window
        fields = "__all__"