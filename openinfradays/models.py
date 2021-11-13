from django.db import models


class Sponsor(models.Model):
    name_ko = models.CharField(max_length=100, default='')
    name_en = models.CharField(max_length=100)
    homepage_url = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='images/sponsor/')
    level = models.CharField(max_length=20,
                             choices=[('Diamond', 'Diamond'), ('Sapphire', 'Sapphire'), ('Gold', 'Gold')],
                             default='Gold')


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='')
    profile_img = models.ImageField(upload_to='images/speaker/', default=None)
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
