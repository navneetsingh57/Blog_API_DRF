from django.db import models
from accounts.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts',blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    reported = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    
    REASON_1 = 1
    REASON_2 = 2
    REASON_3 = 3
    REASON_4 = 4
    
    REPORT_CHOICE = (
        (REASON_1, 'None'),
        (REASON_2, 'Bulying or unwanted content'),
        (REASON_3,'Suicide, self-injury'),
        (REASON_4,'Nudity or sexual activity'),
        (REASON_4,'Scam, fraud, false information'),
    )
    
    commentor = models.ForeignKey(User,on_delete=models.CASCADE, related_name='commentor')
    comment_content = models.CharField(max_length=200,blank=True)
    report = models.PositiveSmallIntegerField(choices=REPORT_CHOICE, default=None,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="post_comments", blank=True, null=True)

    def __str__(self):
        return str(self.post) + '-' + str(self.commentor) + '-' + str(self.id)
