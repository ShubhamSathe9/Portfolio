from django.contrib import admin
from portfolio.models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Tag)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    inlines = [ProjectImageInline]



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "percentage")
    search_fields = ("title", "level")
    
    
    



