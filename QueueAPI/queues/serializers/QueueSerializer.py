from rest_framework import serializers
from queues.models import Queue


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = "__all__"
        read_only_fields = ["queue_code", "created_at", "updated_at", "called_at"]