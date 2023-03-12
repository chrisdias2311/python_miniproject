from django.contrib import admin
from authapp.models import Contact, MembershipPlan, Enroll, Trainer

# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enroll)
admin.site.register(Trainer)
