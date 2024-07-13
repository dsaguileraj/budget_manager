from rest_framework import serializers
from .models import Contract, AdminHistory


class ContractSerializar(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ['create_at', 'last_update']


class AdminHistorySerializar(serializers.ModelSerializer):
    class Meta:
        model = AdminHistory
        fields = '__all__'
        read_only_fields = ['create_at', 'last_update']
