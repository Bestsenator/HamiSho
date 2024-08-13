from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from funcs import check
from index.serializers import *
from index.models import Supporter, MessageToCandidate


# Create your views here.


def index(request):
    return HttpResponse('<h1>API</h1>')


@api_view(['GET'])
def getCandidateInfo(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    candidateInfoSer = CandidateSer(resHeader.get('Candidate')).data
    supportInfo = Supporter.objects.filter(Candidate=resHeader.get('Candidate'), User=resHeader.get('User')).first()
    context = {
        'Status': 200,
        'Candidate': candidateInfoSer,
        'Supporter': False,
        'Sponsor': []
    }
    sponsorInfo = Sponsor.objects.filter(Candidate=resHeader.get('Candidate'))
    if sponsorInfo:
        sponsorInfoSer = SponsorSer(sponsorInfo, many=True).data
        context['Sponsor'] = sponsorInfoSer
    if supportInfo:
        context['Supporter'] = True
    return Response(context)


@api_view(['GET'])
def getPostCandidate(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    postCandidateInfo = Post.objects.filter(Candidate=resHeader.get('Candidate')).order_by('RegisterTime')
    if postCandidateInfo:
        postCandidateInfoSer = PostSer(postCandidateInfo, many=True).data
        context = {
            'Status': 200,
            'Post': postCandidateInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,  # empty list
        }
        return Response(context)


@api_view(['GET'])
def getNewsCandidate(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    newsCandidateInfo = News.objects.filter(Candidate=resHeader.get('Candidate')).order_by('RegisterTime')
    if newsCandidateInfo:
        newsCandidateInfoSer = NewsSer(newsCandidateInfo, many=True).data
        context = {
            'Status': 200,
            'News': newsCandidateInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,  # empty list
        }
        return Response(context)


@api_view(['GET'])
def setSupporter(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    supportInfo = Supporter.objects.filter(User=resHeader.get('User'), Candidate=resHeader.get('Candidate')).first()
    if not supportInfo:
        Supporter.objects.create(User=resHeader.get('User'), Candidate=resHeader.get('Candidate'))
        resHeader.get('Candidate').nSupporter = resHeader.get('Candidate').nSupporter + 1
        resHeader.get('Candidate').qwerty = resHeader.get('Candidate').qwerty + 1
        resHeader.get('Candidate').save()
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def setMessageToCandidate(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    name = request.data.get('Name')
    phone = request.data.get('Phone')
    address = request.data.get('Address')
    message = request.data.get('Message')
    if not message:
        context = {
            'Status': 401,
            'Message': 'message must be sent'
        }
        return Response(context)
    MessageToCandidate.objects.create(User=resHeader.get('User'), Name=name, Phone=phone, Address=address,
                                      Message=message)
    resHeader.get('Candidate').nMessageSentToCandidate = resHeader.get('Candidate').nMessageSentToCandidate + 1
    resHeader.get('Candidate').nMessageSentToCandidate.save()
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['GET'])
def getDeveloperInfo(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    try:
        providerInfo = Provider.objects.filter(Candidate=resHeader.get('Candidate')).first()
        providerInfoSer = ProviderSer(providerInfo).data
        developerInfo = Developer.objects.filter(SeriesDeveloper=resHeader.get('Candidate').SeriesDeveloper)
        developerInfoSer = DeveloperSer(developerInfo, many=True).data
        context = {
            'Status': 200,
            'Provider': providerInfoSer,
            'Developer': developerInfoSer
        }
        return Response(context)
    except Exception as e:
        context = {
            'Status': 400,
            'Message': 'Fetch Error',
            'Error': e.__class__.__name__
        }
        return Response(context)


@api_view(['GET'])
def getSocialCandidate(request):
    resHeader = check.checkHeader(request.headers)
    if resHeader.get('Status') != 200:
        return Response(resHeader)
    socialInfo = SocialMedia.objects.filter(Candidate=resHeader.get('Candidate'))
    if socialInfo:
        context = {
            'Status': 200,
            'SocialMedia': SocialMediaSer(socialInfo, many=True).data
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)

