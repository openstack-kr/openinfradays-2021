from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Sponsor, TechSession, Speaker, VirtualBooth,\
    Profile, AccessLog, SponsorNight, Bof, OnetimeToken, AdVideo


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


class BofAdmin(admin.ModelAdmin):
    list_display = ('title', 'moderator', 'bof_date', 'bof_time')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class OneTimeTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'expired', 'expire_at')


class AdVideoAdmin(admin.ModelAdmin):
    list_display = ('url',)


def export_to_csv(modeladmin, request, queryset):
    from django.http import HttpResponse
    import csv, datetime

    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    title = ['name', 'email']
    writer.writerow(title)
    # Write data rows
    for u in User.objects.all():
        data_row = [u.first_name, u.email]
        writer.writerow(data_row)

    return response


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

    actions = [export_to_csv]


export_to_csv.short_description = 'Export to CSV'  #short description


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(TechSession, TechSessionAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(VirtualBooth, VirtualBoothAdmin)
admin.site.register(AccessLog, AccessLogAdmin)
admin.site.register(SponsorNight, SponsorNightAdmin)
admin.site.register(Bof, BofAdmin)
admin.site.register(OnetimeToken, OneTimeTokenAdmin)
admin.site.register(AdVideo, AdVideoAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





