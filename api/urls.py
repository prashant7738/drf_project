from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentViewDetail),
    
    path('employees/',views.EmployeeList.as_view()),
    path('employees/<int:pk>',views.EmployeeListView.as_view()),
]
