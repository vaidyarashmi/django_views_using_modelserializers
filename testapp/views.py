from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'created succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=p_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'updated succesfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args,**kwargs):      
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')
        emp=Employee.objects.get(id=id)     
        emp.delete() 
        msg={'msg':'Deleted succesfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')    

