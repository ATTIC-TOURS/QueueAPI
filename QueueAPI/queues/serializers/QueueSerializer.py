from rest_framework import serializers
from queues.models import Category, Service, Branch, Queue, Status, Window
from django.utils import timezone


class QueueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), required=True)
    window = serializers.PrimaryKeyRelatedField(queryset=Window.objects.all(), required=False)
    queue_no = serializers.IntegerField()
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=True)
    is_called = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S%z")
    updated_at = serializers.DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S%z", allow_null=True)
    called_at = serializers.DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S%z", allow_null=True)
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100, required=False)
    is_senior_pwd  = serializers.BooleanField(required=True)
    pax = serializers.IntegerField(required=False)
    
    def to_representation(self, instance):
        """
        Override the default `to_representation` method to convert `created_at` 
        and `updated_at` into the current time zone before returning to the client.
        """
        representation = super().to_representation(instance)

        # Convert to current time zone for created_at and updated_at
        if instance.created_at:
            representation['created_at'] = timezone.localtime(instance.created_at).isoformat()

        if instance.updated_at:
            representation['updated_at'] = timezone.localtime(instance.updated_at).isoformat()

        return representation
    
    def create(self, validated_data):
        return Queue.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.window = validated_data.get("window", instance.window)
        instance.status = validated_data.get("status", instance.status)
        instance.is_called = validated_data.get("is_called", instance.is_called)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.called_at = validated_data.get("called_at", instance.called_at)
        instance.pax = validated_data.get("pax", instance.pax)
        instance.save()
        return instance