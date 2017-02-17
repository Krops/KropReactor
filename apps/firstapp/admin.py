from django.contrib import admin
from apps.firstapp.models import Post, Comment, User


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('theme', {'fields': ['theme']}),
        ('slug', {'fields': ['slug']}),
        ('message', {'fields': ['message']}),
        ('rate', {'fields': ['rate']}),
        ('user', {'fields': ['user']}),
    ]
    list_display = ('theme', 'slug', 'rate', 'user')
    search_fields = ["theme"]


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('user', {'fields': ['user']}),
        ('post', {'fields': ['post']}),
        ('message', {'fields': ['message']}),

    ]
    list_display = ('user', 'message')
    search_fields = ["message"]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('email', {'fields': ['email']}),
        ('bio', {'fields': ['bio']}),

    ]
    list_display = ('name', 'email')
    search_fields = ["name"]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
