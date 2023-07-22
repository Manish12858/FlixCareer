from django.contrib import admin

from app.models import JobPost,Location,Author,Skills

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=('__str__','title','salary','date')
    list_filter=('date','salary','expiry')
    search_fields=['title','description','salary']
    search_help_text="write your query and Go"
    # fields=[('title','description'),'salary']
    # exclude=('salary',)
    fieldsets=(
        ('Basic Information',{
        'fields':('title','description')
    }),
    ('More Information',{
        'classes':('collapse','wide'),
        'fields':(('expiry','salary'),'slug')
    }),
    )
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
