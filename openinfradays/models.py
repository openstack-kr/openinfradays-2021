from django.db import models


class Sponsor(models.Model):
    name_ko = models.CharField(max_length=100, default='')
    name_en = models.CharField(max_length=100)
    homepage_url = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='images/sponsor/')
    level = models.CharField(max_length=20,
                             choices=[('Diamond', 'Diamond'), ('Sapphire', 'Sapphire'), ('Gold', 'Gold')],
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
    open_date = models.DateField(default='2021-12-07')

    session_type = models.CharField(max_length=20,
                                    choices=[('Keynote', 'Keynote'), ('Sponsor', 'Sponsor'), ('Tech', "Tech")],
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
    image2 = models.ImageField(upload_to='images/virtualbooth/', default=None, blank=True)
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
