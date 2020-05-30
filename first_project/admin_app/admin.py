from django.contrib import admin

from first_app.models import Topic, Webpage, AccessRecord
from user_app.models import User
from user_auth_app.models import UserProfileInfo
from cbv_app.models import School, Student

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

admin.site.register(User)

admin.site.register(UserProfileInfo)

admin.site.register(School)
admin.site.register(Student)
