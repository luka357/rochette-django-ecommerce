from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from .models import Watch, Category, ContactMessage


# რეგისტრაციის ვალიდაცია: username უნიკალურია, email სავალდებულო, პაროლი Django-ს წესებით
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_password(self, value):
        # TODO(human)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'first_name', 'last_name', 'email', 'subject', 'message']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class WatchSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = Watch
        fields = [
            'id', 'name', 'price', 'description', 'image_url', 'in_stock', 'category', 'category_id']
        