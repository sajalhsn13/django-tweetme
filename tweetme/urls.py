from django.contrib import admin
from django.urls import path

from tweets.views import homeView, getTweet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView),
    path('tweets/<int:tweetId>', getTweet),
]
