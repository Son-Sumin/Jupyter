from django.shortcuts import render
from .models import Bulletin
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# controller 같은 기능
# .html이 view 같은 기능

def index(request):
    bulletin_list = Bulletin.objects.all().order_by('-writeDate')  # -: descending(최근일 위로)
    context = {'bulletin_list': bulletin_list}
    return render(request, 'bulletin/index.html', context)

def create_bulletin(request):
    return render(request, 'bulletin/create_bulletin.html')

def add_bulletin(request):
    bulletin = Bulletin()
    bulletin.title = request.POST['title']
    bulletin.content = request.POST['content']
    bulletin.name = request.POST['name']
    bulletin.passwd = request.POST['pincode']
    bulletin.save()

    return HttpResponseRedirect(reverse('bulletin_board:index'))