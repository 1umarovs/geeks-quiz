from django.contrib import admin
from .models import Lead , Answer , Question , Category


# Register your models here.

admin.site.register(Lead)

admin.site.register(Answer)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', )
    prepopulated_fields = {'slug': ('question_text',)}
    