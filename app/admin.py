from django.contrib import admin

# Register your models here.
from .models import Monday, Tuesday, Wednesday, Thursday, Friday, dismonday, distuesday, diswednesday, disthursday, disfriday

admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(dismonday)
admin.site.register(distuesday)
admin.site.register(diswednesday)
admin.site.register(disthursday)
admin.site.register(disfriday)