from django.contrib import admin

from .models import Sponsor, TechSession, Speaker, VirtualBooth


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


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(TechSession, TechSessionAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(VirtualBooth, VirtualBoothAdmin)
