from rest_framework import serializers
from .models import User, UserProfile

class RegistraionSerializer(serializers.ModelSerializer):
    password_again = serializers.CharField(style = {'input_type': 'password'},write_only=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password_again']
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def save(self):
        password = self.validated_data['password']
        password_again = self.validated_data['password_again']
        
        if password != password_again:
            raise serializers.ValidationError({'error':'Passwords must match'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        first_name = self.validated_data['first_name']
        last_name= self.validated_data['last_name']
        username = self.validated_data['username']
        email= self.validated_data['email']
        password= self.validated_data['password']
        
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class UserProfileSerializeer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        read_only_fields = ['user']
        exclude = ['created_at']
