from rest_framework import serializers
from .models import HaoyiAccount, HaoyiTransaction, ObjectAccount

class HaoyiAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaoyiAccount
        exclude = ()

class HaoyiTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaoyiTransaction
        exclude = ()

class ObjectAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectAccount
        exclude = ()
