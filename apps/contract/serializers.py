from rest_framework import serializers
from .models import Contract, AdminHistory


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ['create_at', 'last_update']


class AdminHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminHistory
        fields = '__all__'
        read_only_fields = ['create_at', 'last_update']
