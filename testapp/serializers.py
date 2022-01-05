from django.core.exceptions import ValidationError
from rest_framework import serializers
from testapp.models import Employee

#Model serializer
class EmployeeSerializer(serializers.ModelSerializer):
    def validate(self,data):
        esal=data.get('esal')
        ename=data.get('ename')
        if ename.lower() == 'puja':
            if esal < 5000:
                raise ValidationError('puja salary should be greater than 5000')
        return data

    class Meta:
        model=Employee
        fields='__all__'
        

'''
# Normal serializer
def multiples_of_1000(value):
    print('validation by validator attribute')
    if value % 1000 !=0:
        raise ValidationError('Employee salary should be multiples of thousand')
    return value

class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=100)
    esal=serializers.FloatField(validators=[multiples_of_1000])
    eaddr=serializers.CharField(max_length=100)
    #field level validation
    def validate_esal(self,value):
        if value < 5000:
            raise serializers.ValidationError('Employee salary should be minimum 5000')
        return value
    
    #object level validation
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='sunny':
            if esal<50000:
                raise serializers.ValidationError('sunny salary should be minimum 50000')
        return data

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance
'''
