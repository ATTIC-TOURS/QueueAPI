from rest_framework import serializers
from queues.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["password"]
        read_only_fields = ["id", "name"]