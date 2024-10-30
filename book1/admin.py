from django.contrib import admin

# Register your models here.

from book1.models import BookInfo,PeopleInfo
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)