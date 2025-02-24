from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = ['code', 'first_name', 'last_name', 'full_names', 'email_address', 'shares', 'welfare', 'savings', 'withdraw', 'fines', 'project_fee']


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = ['date', 'shares', 'savings', 'welfare', 'withdraw', 'project_fee', 'fines']


class CustomTransactionSerializer(serializers.Serializer):
    shares = serializers.IntegerField()
    savings = serializers.IntegerField()
    withdraw = serializers.IntegerField()
    welfare = serializers.IntegerField()
    fines = serializers.IntegerField()
    other = serializers.IntegerField()
    project_fee = serializers.IntegerField()
    net_shares_value = serializers.IntegerField()
    shares_value = serializers.IntegerField()
    shares_withdraw_value = serializers.IntegerField()
