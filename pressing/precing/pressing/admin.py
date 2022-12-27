from django.contrib import admin
from pressing.models import Client,ClientComment,Lenge,NotifierClient

admin.site.site_header = "Pressing Administration"
admin.site.site_title = "Your Admin site"
admin.site.index_title = "WELCOME"

@admin.register(Lenge)
class LengeAdmin(admin.ModelAdmin):
    search_fields =['author__user__username']
admin.site.register(ClientComment)
@admin.register(NotifierClient)
class NotifAdmin(admin.ModelAdmin):
    search_fields = ("client__username__startswith", )
@admin.register(Client)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("user__username__startswith", )