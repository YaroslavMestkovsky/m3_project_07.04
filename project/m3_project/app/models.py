from django.db import models


# Create your models here.

class ContentType(models.Model):
    name = models.CharField(u'Имя', max_length=40, null=True)
    content_type = models.CharField(u'Тип', max_length=40, null=True)
    codename = models.CharField(u'Кодовое название', max_length=40, null=True)

    @property
    def result(self):
        return u' '.join((self.name, self.content_type, self.codename))

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = u'Content Type'
        verbose_name_plural = u'Content Type'


class User(models.Model):
    name = models.CharField(u'Имя', max_length=40, null=True)
    content_type = models.CharField(u'Тип', max_length=40, null=True)
    codename = models.CharField(u'Кодовое название', max_length=40, null=True)

    @property
    def result(self):
        return u' '.join((self.name, self.content_type, self.codename))

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'User'


class Group(models.Model):
    name = models.CharField(u'Имя', max_length=40, null=True)
    content_type = models.CharField(u'Тип', max_length=40, null=True)
    codename = models.CharField(u'Кодовое название', max_length=40, null=True)

    @property
    def result(self):
        return u' '.join((self.name, self.content_type, self.codename))

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = u'Group'
        verbose_name_plural = u'Group'


class Permission(models.Model):
    LE = 'LE'
    GR = 'GR'
    PR = 'PR'
    US = 'US'
    CHOICES = [
        (LE, 'Log entry'),
        (GR, 'Group'),
        (PR, 'Permission'),
        (US, 'User'),
    ]
    name = models.CharField(u'Имя', max_length=40, null=True)
    content_type = models.CharField(u'Тип', choices=CHOICES, max_length=40, default=LE)
    codename = models.CharField(u'Кодовое название', max_length=40, null=True)

    @property
    def result(self):
        return u' '.join((self.name, self.content_type, self.codename))

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = u'Permission'
        verbose_name_plural = u'Permission'
