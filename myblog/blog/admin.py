from django.contrib import admin
from .models import Category, Tag, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    """在管理后台中显示详细的文章信息"""
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 注册模型
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
