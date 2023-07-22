from django.urls import path


# from app.views import job_list,job_detail,hello
from app.views import *







urlpatterns=[
    path('',job_list,name='jobs_home'),
    path('hello/',hello,name='hello'),
    path('job/<int:id>',job_detail,name='jobs_detail'),
]
