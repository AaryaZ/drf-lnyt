from rest_framework import serializers

from apipracticeaz.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    # address = serializers.TextField() #wrong drf oes not have textfield
    # address = serializers.CharField(style={'base_template': 'textarea.html'})
    address = serializers.CharField()
    city = serializers.CharField(max_length=100)


    def create(self, validate_data):
        return Student.objects.create(**validate_data)