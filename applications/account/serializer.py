from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from applications.account.sendmail import send_confirmation_email

User =get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6,write_only=True,required=True)

    class Meta:
        model = User
        fields = ('email','password','password2')
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError('passoword did  not match')
        return attrs
    def validate_email(self,email):
        if not email.endswith('gmail.com'):
            raise serializers.ValidationError('your email must end with "gmail.com"')
        return email

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email(code, user)

        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    def validate_email(self,email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('u are not registrated')
        return email
    def validate(self,attrs):
        email=attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email,password=password)
            if not user:
                raise serializers.ValidationError('not correct password or email')
            attrs['user'] = user
            return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_old_password(self,old_pass):
        user = self.context.get("request").user
        if not user.check_password(old_pass):
            raise serializers.ValidationError("the password id incorect")
        return old_pass
    def validate(self,attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')

        if pass1 != pass2:
            raise serializers.ValidationError('passwords not match')
        return attrs

    def set_user_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()
