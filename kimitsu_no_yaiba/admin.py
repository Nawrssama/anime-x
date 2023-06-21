from django.contrib import admin
from .models import kimitsu, CustomUser
# Register your models here.
class CustomKimitsuUser(admin.ModelAdmin):
    model = kimitsu
    list_display = ['char_name', 'otaku_name', 'char_discription',]
    fieldsets= (
        ('Owner',{
            'fields':('otaku_name',
            )}
        ),
        ('kimitsu Info',{
            'fields':('chat_name','char_discription'
            )}
        )
    )
admin.site.register(kimitsu, CustomKimitsuUser)