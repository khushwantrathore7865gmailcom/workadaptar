from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id','name','email')

class CandidateEnterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=32, style={'input_type': 'password'},write_only=True)
    confirmpass = serializers.CharField(max_length=32, style={'input_type': 'password'},write_only=True)
    class Meta:

        model = Candidate
        fields = ('id', 'name', 'email', 'password','confirmpass')
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        if validated_data['password']==validated_data['confirmpass']:
            user = Candidate.objects.create(**validated_data)
            return user
        else:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
            return user