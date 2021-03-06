from django.db import models
from projects.models import Project,Subscriber
from users.models import Users


class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Users,on_delete=models.CASCADE)

    name = models.CharField(max_length=500)
    description = models.TextField()
    
    resources = models.TextField(null=True) 
    is_done = models.BooleanField(default=False)

    deadline = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if(self.project.user_id!=self.assigned_to):
            try:
            
                val = Subscriber.objects.get(project=self.project,subscriber=self.assigned_to)
                
            except Subscriber.DoesNotExist as e:
                raise e
        
        super(Task,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.name

