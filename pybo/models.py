from django.db import models

class Question(models.Model): #퀘스천 모델
    subject = models.CharField(max_length=200) #제목, 글자수 제한
    content = models.TextField()#내용, 글자수 제한 없음
    create_date = models.DateTimeField()#작성 일시

    def __str__(self):
       return self.subject#아이디값(제목)을 리턴하는 함수


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#연쇄 삭제
    content = models.TextField()
    create_date = models.DateTimeField()

