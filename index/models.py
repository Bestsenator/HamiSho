import jdatetime
import os
import uuid
import random
from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.postgres.fields import ArrayField

# Create your models here.


def rand2Num():
    return random.randint(10, 99)


def ranInt():
    return random.randint(123456, 999999)


def uploadToBackground(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('BackgroundCandidate', filename)


def uploadToSound(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}.{ext}"
    return os.path.join('Sound', filename)


def uploadToOriginImage(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('OriginCandidate', filename)


def uploadToPost(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('post', filename)


def uploadToNews(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('news', filename)


def uploadToAppFile(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.AppName}.{ext}"
    return os.path.join('appFile', filename)


def uploadToSponsor(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('sponsor', filename)


def uploadToDeveloper(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('developer', filename)


def currentDateTime():
    # time = str(jdatetime.datetime.today())
    time = jdatetime.datetime.today()
    return time


def sesProduction():
    return f'{uuid.uuid4()}-{uuid.uuid4()}'


class Candidate(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    Name = models.CharField(max_length=200)
    SirName = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to=uploadToOriginImage)
    Slogan = models.TextField(max_length=1000)
    Cv = models.TextField(max_length=5000, default='')
    Color = ArrayField(models.TextField(max_length=16), default=list,
                       help_text="1.Background - 2.Buttons - 3.SloganColor")
    Background = models.ImageField(upload_to=uploadToBackground)
    nSupporter = models.IntegerField(default=0)
    nMessageSentToCandidate = models.IntegerField(default=0)
    Sound = models.FileField(upload_to=uploadToSound, default='')
    qwerty = models.IntegerField(default=0)  # or the sttscs
    isSponsorApp = models.BooleanField(default=False)
    SeriesDeveloper = models.IntegerField(default=1)
    VersionApp = models.CharField(max_length=50, default='1.0.0')
    AppFile = models.FileField(upload_to=uploadToAppFile, default='')
    AppName = models.CharField(max_length=100, default='')
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return self.Name + ' - {}'.format(self.Code)

    def pre_save(self):  # delete old picture before change picture
        if self.pk:
            try:
                old_instance = Candidate.objects.get(pk=self.pk)
                if old_instance.Image and self.Image != old_instance.Image:
                    old_instance.Image.delete(save=False)
                if old_instance.Background and self.Background != old_instance.Background:
                    old_instance.Background.delete(save=False)
                if old_instance.AppFile and self.AppFile != old_instance.AppFile:
                    old_instance.AppFile.delete(save=False)
            except Candidate.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storageImage, pathImage = self.Image.storage, self.Image.path
        storageBackImage, pathBackImage = self.Background.storage, self.Background.path
        storageAppFile, pathAppFile = self.AppFile.storage, self.AppFile.path
        # Delete the model before the file
        super(Candidate, self).delete(*args, **kwargs)
        # Delete the file after the model
        storageImage.delete(pathImage)
        storageImage.delete(pathBackImage)
        storageImage.delete(pathAppFile)


class User(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    IMEI = models.CharField(max_length=20)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Code}'


class APIKEY(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    ApiKey = models.TextField(default=sesProduction)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Code}'


class Post(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to=uploadToPost)
    Caption = models.TextField(max_length=2000)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Code} - {self.RegisterTime}'

    def pre_save(self):  # delete old picture before change picture
        if self.pk:
            try:
                old_instance = Post.objects.get(pk=self.pk)
                if old_instance.Image and self.Image != old_instance.Image:
                    old_instance.Image.delete(save=False)
            except Post.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storageImage, pathImage = self.Image.storage, self.Image.path
        # Delete the model before the file
        super(Post, self).delete(*args, **kwargs)
        # Delete the file after the model
        storageImage.delete(pathImage)


class News(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Image = models.ImageField(upload_to=uploadToNews)
    Content = models.TextField(max_length=2000)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Code} - {self.RegisterTime}'

    def pre_save(self):  # delete old picture before change picture
        if self.pk:
            try:
                old_instance = News.objects.get(pk=self.pk)
                if old_instance.Image and self.Image != old_instance.Image:
                    old_instance.Image.delete(save=False)
            except News.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storageImage, pathImage = self.Image.storage, self.Image.path
        # Delete the model before the file
        super(News, self).delete(*args, **kwargs)
        # Delete the file after the model
        storageImage.delete(pathImage)


class Supporter(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class Sponsor(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    Name = models.CharField(max_length=150)
    Image = models.ImageField(upload_to=uploadToSponsor)
    Proper = models.CharField(max_length=150)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def pre_save(self):  # delete old picture before change picture
        if self.pk:
            try:
                old_instance = Sponsor.objects.get(pk=self.pk)
                if old_instance.Image and self.Image != old_instance.Image:
                    old_instance.Image.delete(save=False)
            except Sponsor.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storageImage, pathImage = self.Image.storage, self.Image.path
        # Delete the model before the file
        super(Sponsor, self).delete(*args, **kwargs)
        # Delete the file after the model
        storageImage.delete(pathImage)


class MessageToCandidate(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True, editable=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    Name = models.CharField(max_length=100, blank=True, null=True)
    Phone = models.CharField(max_length=11, blank=True, null=True)
    Address = models.TextField(max_length=500, blank=True, null=True)
    Message = models.TextField(max_length=2000, default='')
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class Developer(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True)
    SeriesDeveloper = models.IntegerField(default=1)
    Name = models.CharField(max_length=150, default='')
    Expertise = models.CharField(max_length=150, default='')
    Image = models.ImageField(upload_to=uploadToDeveloper)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def pre_save(self):  # delete old picture before change picture
        if self.pk:
            try:
                old_instance = Developer.objects.get(pk=self.pk)
                if old_instance.Image and self.Image != old_instance.Image:
                    old_instance.Image.delete(save=False)
            except Developer.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storageImage, pathImage = self.Image.storage, self.Image.path
        # Delete the model before the file
        super(Developer, self).delete(*args, **kwargs)
        # Delete the file after the model
        storageImage.delete(pathImage)


class Provider(models.Model):
    Code = models.IntegerField(default=ranInt, primary_key=True)
    Name = models.CharField(max_length=200)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Logo = models.ImageField(upload_to=0)
    Slogan = models.CharField(max_length=150)

