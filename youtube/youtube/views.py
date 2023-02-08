from django.shortcuts import render, redirect
from pytube import Search as YoutubeSearch,YouTube 
from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None
        
def Home(request):
    data = {}
    if "search_str" in request.GET:
        if request.GET["search_str"]:
            data["results"] = YoutubeSearch(request.GET["search_str"]).results
            
    return render(request=request,template_name='home.html',context=data)

def Download(request):
    data = {}
    if "video_url" in request.GET:
        if request.GET["video_url"]:
            video = YouTube(request.GET["video_url"])
            data["video"] = video
            data["streams"] = video.streams
    return render(request=request,template_name='download.html',context=data)
    
        