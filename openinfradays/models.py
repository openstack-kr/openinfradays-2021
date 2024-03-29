from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


class Sponsor(models.Model):
    name_ko = models.CharField(max_length=100, default='')
    name_en = models.CharField(max_length=100)
    homepage_url = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='images/sponsor/')
    level = models.CharField(max_length=20,
                             choices=[('Diamond', 'Diamond'), ('Sapphire', 'Sapphire'), ('Gold', 'Gold'), ('Media', 'Media')],
                             default='Gold')

    def __str__(self):
        return self.name_ko


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='')
    profile_img = models.ImageField(upload_to='images/speaker/', default=None, blank=True)
    bio = models.TextField(max_length=1000, default='')
    twitter = models.CharField(max_length=100, default='', blank=True)
    facebook = models.CharField(max_length=100, default='', blank=True)
    blog = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name


class TechSession(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)
    speaker = models.OneToOneField(Speaker, on_delete=models.SET_NULL, null=True)
    slide = models.FileField(upload_to='slides/', default='', blank=True)
    video_url = models.CharField(max_length=1000, default='', blank=True)
    ad1_url = models.CharField(max_length=1000, default='', blank=True)
    ad2_url = models.CharField(max_length=1000, default='', blank=True)
    open_date = models.DateField(default='2021-12-07')

    session_type = models.CharField(max_length=20,
                                    choices=[('Keynote', 'Keynote'), ('Sponsor', 'Sponsor'), ('Tech', "Tech"),
                                             ('Community', "Community")],
                                    default='Tech')
    qna_enable = models.BooleanField(default=False, blank=True)
    qna_date = models.DateField(blank=True, default='2021-12-07')
    qna_time = models.TimeField(blank=True, default='00:00:00')
    qna_location = models.CharField(max_length=100, default='Gather Town')


class VirtualBooth(models.Model):
    sponsor = models.OneToOneField(Sponsor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, default='', blank=True)
    short_desc = models.CharField(max_length=200, default='', blank=True)
    body = models.TextField(max_length=10000, default='', blank=True)
    custom_logo = models.ImageField(upload_to='images/virtualbooth/', null=True, default=None, blank=True)
    video1 = models.CharField(max_length=100, default='', blank=True)
    video2 = models.CharField(max_length=100, default='', blank=True)
    video3 = models.CharField(max_length=100, default='', blank=True)
    image1 = models.ImageField(upload_to='images/virtualbooth/', default=None, blank=True)
    image1_link = models.FileField(upload_to='files/virtualbooth/', default='', blank=True)
    image2 = models.ImageField(upload_to='images/virtualbooth/', default=None, blank=True)
    image2_link = models.FileField(upload_to='files/virtualbooth/', default='', blank=True)
    image3 = models.ImageField(upload_to='images/virtualbooth/', default=None, blank=True)
    link1 = models.CharField(max_length=100, default='', blank=True)
    link1_txt = models.CharField(max_length=100, default='', blank=True)
    link2 = models.CharField(max_length=100, default='', blank=True)
    link2_txt = models.CharField(max_length=100, default='', blank=True)
    link3 = models.CharField(max_length=100, default='', blank=True)
    link3_txt = models.CharField(max_length=100, default='', blank=True)
    link4 = models.CharField(max_length=100, default='', blank=True)
    link4_txt = models.CharField(max_length=100, default='', blank=True)
    link5 = models.CharField(max_length=100, default='', blank=True)
    link5_txt = models.CharField(max_length=100, default='', blank=True)


class Profile(models.Model):
    GITHUB = 'github'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    is_check_navercloud = models.BooleanField(default=False)
    login_type = models.CharField(max_length=10)
    complete = models.BooleanField(default=False)
    company = models.CharField(max_length=100, default='', blank=True)
    job = models.CharField(max_length=100, default='', blank=True)
    agree_with_private = models.BooleanField(default=False, null=True)
    agree_with_sponsor = models.BooleanField(default=False, null=True)
    naver_cloud_form = models.CharField(max_length=10000, default='', blank=True)


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)


class OnetimeToken(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, default='', blank=True)
    expired = models.BooleanField(default=False)
    error_msg = models.CharField(max_length=10000, default='', blank=True)
    request_ip = models.CharField(max_length=100, default='', blank=True)
    access_time = models.DateTimeField(null=True)
    expire_at = models.DateTimeField(default=datetime.now() + timedelta(days=1))


class AccessLog(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=100, default='', blank=True)
    access_at = models.DateTimeField(default=datetime.now())


class SponsorNight(models.Model):
    sponsor = models.OneToOneField(Sponsor, on_delete=models.CASCADE)
    event_date = models.DateField(blank=True, default='2021-12-07')
    event_time = models.CharField(max_length=100, default='', blank=True)
    feature1 = models.CharField(max_length=100, default='', blank=True)
    feature2 = models.CharField(max_length=100, default='', blank=True)
    feature3 = models.CharField(max_length=100, default='', blank=True)
    custom_btn_txt = models.CharField(max_length=100, default='', blank=True)
    custom_btn_link = models.CharField(max_length=100, default='', blank=True)


class Bof(models.Model):
    title = models.CharField(max_length=100, default='')
    moderator = models.CharField(max_length=120, default='')
    profile_img = models.ImageField(upload_to='images/bof/', default=None, blank=True)
    bof_date = models.DateField(default='2021-12-07')
    bof_time = models.CharField(max_length=30, default='')
    content = models.TextField(max_length=1000, default='')


class AdVideo(models.Model):
    url = models.CharField(max_length=100, default='')