from index.models import APIKEY, User, Candidate
from index.serializers import AppFileSer


def checkHeader(header):
    apiKey = header.get('API-X-KEY')
    candidate = header.get('Candidate')
    imei = header.get('IMEI')
    version = header.get('Version')
    if not candidate.isdigit():
        context = {
            'Status': 901,
            'Message': 'Candidate Code invalid'
        }
        return context
    apiKeyInfo = APIKEY.objects.filter(ApiKey=apiKey).first()
    if not apiKeyInfo:
        context = {
            'Status': 900,
            'Message': 'API KEY invalid'
        }
        return context
    candidateInfo = Candidate.objects.filter(Code=candidate).first()
    if not candidateInfo:
        context = {
            'Status': 901,
            'Message': 'Candidate Code invalid'
        }
        return context
    if candidateInfo.VersionApp != str(version):
        appFileInfoSer = AppFileSer(candidateInfo).data
        context = {
            'Status': 903,
            'Message': 'Update App',
            'Link': appFileInfoSer
        }
        return context
    if not imei:
        context = {
            'Status': 902,  # key not sent
            'Message': 'IMEI is not sent'
        }
        return context
    userInfo = User.objects.filter(IMEI=imei).first()
    if not userInfo:
        candidateInfo.nSupporter = candidateInfo.nSupporter + 1
        candidateInfo.qwerty = candidateInfo.qwerty + 1
        candidateInfo.save()
        User.objects.create(IMEI=imei)
    context = {
        'Status': 200,
        'User': userInfo,
        'Candidate': candidateInfo
    }
    return context


def checkIMEIPass(key):
    if not key:
        context = {
            'Status': 902,  # key not sent
            'Message': 'IMEI is not sent'
        }
        return context
    userInfo = User.objects.filter(IMEI=key).first()
    if userInfo:
        context = {
            'Status': 200
        }
    else:
        context = {
            'Status': 902,
            'Message': 'IMEI invalid'
        }
    return context
