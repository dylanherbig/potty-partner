from django.contrib import admin
from app.models import ToiletReview, Toilet, Feature

# Register your models here.

admin.site.register(ToiletReview)
admin.site.register(Toilet)
admin.site.register(Feature)