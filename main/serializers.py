from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = ['code', 'first_name', 'last_name', 'full_names', 'email_address', 'shares', 'welfare', 'savings', 'withdraw', 'fines', 'project_fee']