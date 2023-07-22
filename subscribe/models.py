from django.db import models

NEWSLETTER_OPTION=[
    ('W','Weekly'),
    ('M',"Monthly")
]
# Create your model here.
class Subscribe(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    option=models.CharField(max_length=2,choices=NEWSLETTER_OPTION,default='M')

