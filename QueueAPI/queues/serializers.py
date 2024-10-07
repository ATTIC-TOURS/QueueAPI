from rest_framework import serializers
from queues.models import Service, Branch, Queue, Status, Window


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BranchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Branch.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Status.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class WindowSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Window.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class QueueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=False)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), required=False)
    window_id = serializers.PrimaryKeyRelatedField(queryset=Window.objects.all(), required=False)
    queue_no = serializers.IntegerField(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=False)
    is_called = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Queue.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.window_id = validated_data.get("window_id", instance.window_id)
        instance.status_id = validated_data.get("status_id", instance.status_id)
        instance.is_called = validated_data.get("is_called", instance.is_called)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance