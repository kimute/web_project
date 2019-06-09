from django.contrib import admin
from .models import User, Entry


#userとenttryモデルを追加
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
