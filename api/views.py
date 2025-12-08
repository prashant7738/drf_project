from django.shortcuts import render , get_object_or_404
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer , EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404

from blog.models import blog , comment
from blog.serializers import blog_serializer , comment_serializer

# now using mixins and generics 
from rest_framework import mixins , generics , viewsets













# Create your views here.

# if i have to excess the studentview using only get method then use this 
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from student table
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
 
@api_view(['GET','PUT','DELETE'])   
def studentViewDetail(request , pk):
    try:
        student = Student.objects.get(pk = pk)
    
    except Student.DoesNotExist:
         return Response(status = status.HTTP_404_NOT_FOUND)
    
    
    # for getting particular view 
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(data = serializer.data , status = status.HTTP_200_OK)
    
    # For updating existing info 
    elif request.method == "PUT":
        # TO update we need to pass student in serializer
        serializer = StudentSerializer(student ,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
        
    # Deleting 
    
    elif request.method == "DELETE":
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
  
""" 
# Now using class based view,
   
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    
    def put(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status = status.HTTP_200_OK)
        return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    
    
class EmployeeListView(APIView):
   
    # Now to take the employee object 
    def get_object(self, pk):
    
        try:
            return Employee.objects.get(pk= pk)
        
        except Employee.DoesNotExist:
            raise Http404
        
    
    def get(self , request , pk):
        
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data , status = status.HTTP_200_OK)
        

    def put(self, request , pk):
        
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee , data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
            
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request , pk):
        
        employee = self.get_object(pk)
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""  



"""

#   NOW USING MIXINS

class EmployeeList(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self , request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
#   NOW USING MIXINS    
class EmployeeListView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin , mixins.UpdateModelMixin,generics.GenericAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self , request , pk):
        return self.retrieve(request , pk)
    
    def delete(self, request , pk):
        return self.destroy(request , pk)
    
    def put(self, request , pk):
        return self.update(request, pk)
        
"""


"""
# Now using Generics 

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    
"""



"""
# Now using viewset 

class EmployeeViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset , many = True)
        return Response(serializer.data)
    
    def create(self, request):

        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors)
    
    def retrieve(self, request , pk = None):
        employee = get_object_or_404(Employee , pk= pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def update(self, request , pk = None):
        employee = get_object_or_404(Employee , pk = pk)
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self , request, pk = None):
        employee = get_object_or_404(Employee, pk = pk)
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        
"""


# Now using modelviewset

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    
class blogsView(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blog_serializer
    
class commentsView(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    serializer_class = comment_serializer