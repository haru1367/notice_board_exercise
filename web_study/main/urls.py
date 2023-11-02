from django.urls import path
from django.contrib import admin
from main.views import index,blog,posting,new_post,remove_post

from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns=[
    path('admin/',admin.site.urls), #웹사이트의 첫화면은 index페이지이다 + url이름은 index이다
    path('',index,name='index'), # URL:80/blog에 접속하면 blog페이지 + URL이름은 blog이다
    path('blog/',blog,name = 'blog'), # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',posting,name='posting'),
    path('blog/new_post/',new_post),
    path('blog/<int:pk>/remove/',remove_post),
]
#view와 url을 연결

#이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

