from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from .models import Student
# from apipracticeaz.models import Student (same as above)

# Create your views here.
def student_details(request,pk):
    stu= Student.objects.get(id =pk)
    print("studenttttttt",stu)
    serializer = StudentSerializer(stu)
    print("serializerrrr",serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print("JSSOOSNNNSNNSNNSNNSN",json_data)

    return HttpResponse(json_data, content_type='application/json')

def student_list(request):
    stu= Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
    
