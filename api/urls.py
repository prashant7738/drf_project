from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees' , views.EmployeeViewSet , basename='employees')


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentViewDetail),
    
    # path('employees/',views.EmployeeList.as_view()),
    # path('employees/<int:pk>',views.EmployeeListView.as_view()),
    
    path('' , include(router.urls)),
    
    path('blogs/',views.blogsView.as_view()),
    path('comments/',views.commentsView.as_view()),
]
