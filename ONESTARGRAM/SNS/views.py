from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request,'sns/index.html')

def SNS(request):
    postlist = Post.objects.all()
    return render(request,'SNS/SNS.html',{'postlist':postlist})

    