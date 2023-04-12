from django.contrib import admin
from authapp.models import Contact, MembershipPlan, Enroll, Trainer, Gallery, Attendance

# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enroll)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
