from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Sponsor, TechSession, Speaker, VirtualBooth, Profile, AccessLog, SponsorNight


class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'path', 'access_at')

    @admin.display(ordering='user__first_name', description='username')
    def get_user_name(self, obj):
        if obj.user is None:
            return 'Anon'
        return obj.user.first_name


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name_ko', 'homepage_url', 'level')


class TechSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_speaker', 'session_type', 'open_date')

    @admin.display(ordering='speaker__name', description='Speaker')
    def get_speaker(self, obj):
        return obj.speaker.name


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class VirtualBoothAdmin(admin.ModelAdmin):
    list_display = ('get_sponsor',)

    @admin.display(ordering='sponsor__name_ko', description="Sponsor")
    def get_sponsor(self, obj):
        return obj.sponsor.name_ko


class SponsorNightAdmin(admin.ModelAdmin):
    list_display = ('get_sponsor', 'event_date')

    @admin.display(ordering='sponsor__name_ko', description="Sponsor")
    def get_sponsor(self, obj):
        return obj.sponsor.name_ko


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(TechSession, TechSessionAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(VirtualBooth, VirtualBoothAdmin)
admin.site.register(AccessLog, AccessLogAdmin)
admin.site.register(SponsorNight, SponsorNightAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)