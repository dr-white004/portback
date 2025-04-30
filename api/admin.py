from django.contrib import admin
from .models import UserProfile, Portfolio

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'years_of_experience', 'projects_completed', 'location')
    search_fields = ('user__username', 'position', 'location')
    list_filter = ('position', 'location')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'project_type', 'client', 'duration', 'project_link')
    search_fields = ('title', 'owner__username', 'client', 'project_type')
    list_filter = ('project_type', 'client', 'tools')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug from title
