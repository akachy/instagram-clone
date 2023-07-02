from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.DO_NOTHING)
    content = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='post_like', blank=True)
    caption = models.CharField(max_length=1500, blank=True,null=True)

    def no_of_likes(self):
        return self.likes.count()
    def __str__(self):
        return(
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d}): "
            f"{self.content}..."
        )

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self',
        related_name='followed_by',
        symmetrical=False,
        blank = True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='p_images/')
    profile_bio = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        # have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)
    
