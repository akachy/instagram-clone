from django.contrib import admin
from django.contrib.auth.models import Group, User
from . models import Post, Profile, Comment
# Register your models here
admin.site.unregister(Group)

# extend user model

class ProfileInline(admin.StackedInline):
    model = Profile



class UserAdmin(admin.ModelAdmin):
    model = User
    # dislay username fields

    fields = ['username']
    inlines = [ProfileInline]

    
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)



# mix profile into user


