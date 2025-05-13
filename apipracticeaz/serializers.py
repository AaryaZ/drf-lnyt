from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    # address = serializers.TextField() #wrong drf oes not have textfield
    # address = serializers.CharField(style={'base_template': 'textarea.html'})
    address = serializers.CharField()
    city = serializers.CharField(max_length=100)