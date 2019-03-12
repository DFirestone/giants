from django.contrib import admin


from .models import Course, Exercise, Lesson, AgeGroup
# Register your models here.
admin.site.register(Course)
admin.site.register(Exercise)
admin.site.register(Lesson)
admin.site.register(AgeGroup)