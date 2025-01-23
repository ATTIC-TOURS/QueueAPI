from rest_framework import serializers
from queues.models import Service


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    notes = serializers.CharField(required=False, max_length=100)
    is_cut_off = serializers.BooleanField()
    
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.name = validated_data.get("notes", instance.notes)
        instance.name = validated_data.get("is_cut_off", instance.is_cut_off)
        instance.save()
        return instance