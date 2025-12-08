from rest_framework import serializers

from .models import blog , comment


        
class comment_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = comment
        fields = "__all__"
        
        
        
class blog_serializer(serializers.ModelSerializer):
    
    comments = comment_serializer(many = True , read_only = True)
    
    class Meta:
        model = blog
        fields = "__all__"
        
    