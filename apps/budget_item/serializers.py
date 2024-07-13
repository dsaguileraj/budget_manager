from rest_framework import serializers
from .models import BudgetItem


class BudgetItemSerializar(serializers.ModelSerializer):
    class Meta:
        model = BudgetItem
        fields = '__all__'
        read_only_fields = ['create_at', 'last_update']
