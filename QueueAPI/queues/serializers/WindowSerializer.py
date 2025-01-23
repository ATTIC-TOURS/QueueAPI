from rest_framework import serializers
from queues.models import Window


class WindowSerializer(serializers.Serializer):    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Window.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance