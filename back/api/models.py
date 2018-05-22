from io import StringIO, BytesIO

import qrcode
import os
from ckeditor.fields import RichTextField
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.conf import settings


def qrcode_location(filename):
    return 'qrcode/%s' % (filename)


class Artwortk(models.Model):
    name = models.TextField()
    desc = models.TextField()
    img = models.ImageField()
    room = models.ForeignKey(
        'Room',
        on_delete=models.CASCADE,
        db_column='id_room'
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        db_column='id_author'
    )
    flashcode=models.ImageField(upload_to='qrcode/', blank=True, null=True)

    def __str__(self):
        return self.name

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.save()
        qr.add_data(self.id)
        qr.make(fit=True)
        img = qr.make_image()

        filename = 'qr-%s.png' % (self.id)

        img.save(os.path.join(settings.MEDIA_ROOT, qrcode_location("temp-"+filename)))

        imgopen = open(os.path.join(settings.MEDIA_ROOT, qrcode_location("temp-"+filename)), "rb")

        django_file = File(imgopen)

        self.flashcode.save(filename, django_file, save=True)

        imgopen.close()

        os.remove(os.path.join(settings.MEDIA_ROOT, qrcode_location("temp-"+filename)))

    class Meta:
        managed = True
        db_table = 'Artwortk'


class Author(models.Model):
    name = models.TextField()
    firstname = models.TextField()
    mail = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    linkedin_link = models.TextField(blank=True, null=True)
    facebook_link = models.TextField(blank=True, null=True)
    instagram_link = models.TextField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Author'


class Content(models.Model):
    page = models.ForeignKey(
        'Page',
        on_delete=models.CASCADE,
        db_column='id_page'
    )
    type = models.TextField()
    text = RichTextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Page : "+str(self.page)+"  Type : "+self.type

    class Meta:
        managed = False
        db_table = 'Content'


class Page(models.Model):
    name = models.TextField(blank=False, null=False)
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        db_column='id_place'
    )

    def __str__(self):
        return "La page "+self.name+" De "+str(self.place)

    class Meta:
        managed = False
        db_table = 'Page'


class Place(models.Model):
    name = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Place'


class Room(models.Model):
    name = models.TextField(blank=False, null=False)
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        db_column='id_place'
    )

    def __str__(self):
        return "La salle "+self.name+" De "+str(self.place)

    class Meta:
        managed = False
        db_table = 'Room'


class Like(models.Model):
    token = models.TextField(blank=False, null=False)
    artwortk = models.ForeignKey(
        'Artwortk',
        on_delete=models.CASCADE,
        db_column='id_artwortk'
    )

    class Meta:
        managed = False
        db_table = 'Like'