from rest_framework import serializers
from queues.models import Category, ServiceType, Service, Branch, Queue, Status, Window, Mobile, Printer
from django.utils import timezone


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    display_name = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.display_name = validated_data.get("name", instance.display_name)
        instance.save()
        return instance
    

class ServiceTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    
    def create(self, validated_data):
        return ServiceType.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance   


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    service_type = serializers.PrimaryKeyRelatedField(queryset=ServiceType.objects.all(), required=False)
    
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
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), required=True)
    window = serializers.PrimaryKeyRelatedField(queryset=Window.objects.all(), required=False)
    queue_no = serializers.IntegerField()
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=True)
    is_called = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S%z")
    updated_at = serializers.DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S%z", allow_null=True)
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100, required=False)
    is_senior_pwd  = serializers.BooleanField(required=True)
    
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
        instance.save()
        return instance
    
    
class MobileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mac_address = serializers.CharField(max_length=100)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Mobile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.mac_address = validated_data.get("mac_address", instance.mac_address)
        instance.branch_id = validated_data.get("branch_id", instance.branch_id)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance


class PrinterSerializer(serializers.Serializer):
    id = id = serializers.IntegerField(read_only=True)
    mac_address = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField()
    error_msg = serializers.CharField(max_length=200, required=False)    
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)

    def create(self, validated_data):
        return Printer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.mac_address = validated_data.get("mac_address", instance.mac_address)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.error_msg = validated_data.get("error_msg", instance.error_msg)
        instance.branch_id = validated_data.get("branch", instance.branch)
        instance.save()
        return instance


class MarkQueueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return Window.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("text", instance.name)
        instance.save()
        return instance