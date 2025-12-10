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
    
    
    # for blogs and comments
    
    path('blogs/',views.blogsList.as_view()),
    path('comments/',views.commentsList.as_view()),
    
    #   primary key based operation 
    path('comments/<int:pk>',views.commentsListView.as_view()),
    path('blogs/<int:pk>/',views.blogsListView.as_view()),
    
]
