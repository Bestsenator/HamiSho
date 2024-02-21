from rest_framework import serializers
from index.models import Candidate, Post, News, Sponsor, Developer, Provider


class CandidateSer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['Code', 'Name', 'Image', 'Cv', 'Slogan', 'Color', 'Background', 'nSupporter',
                  'nMessageSentToCandidate', 'Sound', 'isSponsorApp']


class PostSer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class SponsorSer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class DeveloperSer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"


class ProviderSer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class AppFileSer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['AppFile']
