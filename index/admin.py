from django.contrib import admin
from index import models
from django.contrib.auth.models import User, Group

# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['Code', 'Name', 'nSupporter', 'RegisterTime']


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['Code', 'Name', 'Candidate', 'Proper', 'RegisterTime']


class UserAdmin(admin.ModelAdmin):
    list_display = ['Code', 'IMEI', 'RegisterTime']


class APIKEYAdmin(admin.ModelAdmin):
    list_display = ['Code', 'ApiKey', 'RegisterTime']


class PostAdmin(admin.ModelAdmin):
    list_display = ['Code', 'Candidate', 'RegisterTime']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['Code', 'Candidate', 'RegisterTime']


class SuppAdmin(admin.ModelAdmin):
    list_display = ['Code', 'User', 'Candidate']


class MessToCanAdmin(admin.ModelAdmin):
    list_display = ['Code', 'User', 'Message']


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['Code', 'SeriesDeveloper', 'Name', 'Expertise', 'RegisterTime']
    list_filter = ['SeriesDeveloper', 'Expertise']
    search_fields = ['Code', 'SeriesDeveloper', 'Name', 'Expertise']


class ProviderAdmin(admin.ModelAdmin):
    list_display = ['Code', 'Name', 'Candidate', 'Slogan']
    list_filter = ['Name', 'Candidate']
    search_fields = ['Code', 'Name']


admin.site.register(models.Candidate, CandidateAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.APIKEY, APIKEYAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Sponsor, SponsorAdmin)
admin.site.register(models.Supporter, SuppAdmin)
admin.site.register(models.MessageToCandidate, MessToCanAdmin)
admin.site.register(models.Developer, DeveloperAdmin)
admin.site.register(models.Provider, ProviderAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
