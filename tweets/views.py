from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet


def homeView(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")


def getTweet(request, tweetId, *args, **kwargs):
    data = {}
    try:
        o = Tweet.objects.get(id=tweetId)
        data['success'] = True
        data['content'] = o.content
        status = 200
    except:
        data['success'] = False
        data['message'] = "Content not found"
        status = 404

    return JsonResponse(data, status=status)
