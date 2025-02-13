from rest_framework import serializers
from queues.models import Marquee


class MarqueeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marquee
        fields = "__all__"