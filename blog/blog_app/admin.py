from django.contrib import admin
from .models import User
from .models import Blog,Comment



#Creating blogAdmin to modify fields of Blog model
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','description','blog_content','cover_photo','blog_author','created_date','populer')
    list_display_links = ('id',)
    list_editable = ('description',)
    search_fields = ('description',)
    readonly_fields = ('created_date',)

#Creating userAdmin to modify fields of Blog model
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')

#Adding User and Blog models to admin panel
admin.site.register(User,UserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

