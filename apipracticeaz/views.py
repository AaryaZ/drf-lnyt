import io
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from .models import Student
# from apipracticeaz.models import Student (same as above)
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created successfully'}
            return JsonResponse(res, status=201,safe=False)
        return JsonResponse({'error': serializer.errors}, status=405,safe=False)
    
    
