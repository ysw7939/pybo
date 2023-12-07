from django.db import models
from django.contrib.auth.models import User

# 질문
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # 제목 char에 200 길이
    subject = models.CharField(max_length=200)
    # 내용 길이를 가지지 않음
    content = models.TextField()
    # 날짜 DateTimeFiled를 사용
    create_date = models.DateTimeField()
    
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    # id값대신 suject를 리턴하게 해줌
    def __str__(self):
        return self.subject

# 질문에 대한 답변에 해당됨 
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # 질문에대한 연결된 답변 ForeignKey를 이용한다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

