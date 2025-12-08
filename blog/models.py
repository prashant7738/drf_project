from django.db import models

class blog(models.Model):
    
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    
    def __str__(self):
        return self.blog_title
    
    
class comment(models.Model):
    
    blog = models.ForeignKey(blog , on_delete=models.CASCADE , related_name="comments")
    comment = models.TextField()
    
    def __str__(self):
        return self.blog
