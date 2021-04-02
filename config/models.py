from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Education(models.Model):
    title = models.CharField('Title pendidikan Kamu', max_length=255)
    long = models.CharField('Lama kamu bersekolah (dalam tahun)', max_length=255)
    desc = CKEditor5Field('Deskripsi Singkat', null=False, blank=False)

    def __str__(self):
        return self.title


class MyProfile(models.Model):
    nick = models.CharField('Nama panggilan/sapaan', max_length=255)
    prof_img = models.ImageField(upload_to='img/', default='')
    f_name = models.CharField('Nama Lengkap', max_length=255)
    w_phone = models.CharField('Nomor handphone / Wa kamu +62 (cth: 813xxxxxxxxxx)', max_length=255)
    email = models.EmailField(max_length=255)
    desc = CKEditor5Field('Deskripsi Singkat', null=False, blank=False)

    def __str__(self):
        return self.nick


# class SocialMedia(models.Model):
#     name = models.CharField(max_length=255)
#     icon = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.icon
#
#
class MySocial(models.Model):
    icon = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.icon


class Skill(models.Model):
    skills = CKEditor5Field(null=False, blank=False)


class Award(models.Model):
    title = models.CharField('Nama Sertifikat', max_length=255)
