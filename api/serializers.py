from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=10, required=True)
    class Meta:
        model = Item
        fields = '__all__'