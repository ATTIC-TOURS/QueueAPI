from rest_framework import serializers
from queues.models import Marquee


class MarqueeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Marquee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.text = validated_data.get("text", instance.text)
        instance.save()
        return instance