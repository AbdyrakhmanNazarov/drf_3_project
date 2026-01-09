from django.contrib import admin
from .models import User, OTPVerification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')

@admin.register(OTPVerification)
class OTPVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'is_used', 'created_at')
    search_fields = ('user__email', 'code')
    list_filter = ('is_used',)
