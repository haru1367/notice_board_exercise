from django.db import models

# Create your models here.
# 게시글(post)엔 제목(postname),내용(contents)이 존재합니다.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True) #게시글 post에 이미지 추가
    contents = models.TextField()
    
    def __str__(self):
        return self.postname
#게시판 모델을 만들어 migrate로 데이터베이스에 저장