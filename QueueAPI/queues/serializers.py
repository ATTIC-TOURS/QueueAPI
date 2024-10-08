from rest_framework import serializers
from queues.models import Service, Branch, Queue, Status, Window, Mobile, Printer


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
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), required=True)
    window_id = serializers.PrimaryKeyRelatedField(queryset=Window.objects.all(), required=False)
    queue_no = serializers.IntegerField()
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), required=True)
    is_called = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(required=False)
    
    def create(self, validated_data):
        return Queue.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.window_id = validated_data.get("window_id", instance.window_id)
        instance.status_id = validated_data.get("status_id", instance.status_id)
        instance.is_called = validated_data.get("is_called", instance.is_called)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance
    
    
class MobileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mac_address = serializers.CharField(max_length=100)
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=True)
    is_active = serializers.BooleanField()
    printer_id = serializers.PrimaryKeyRelatedField(queryset=Printer.objects.all(), required=False)

    def create(self, validated_data):
        return Mobile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.mac_address = validated_data.get("name", instance.mac_address)
        instance.branch_id = validated_data.get("branch_id", instance.branch_id)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.printer_id = validated_data.get("printer_id", instance.printer_id)
        instance.save()
        return instance