from django.contrib import admin
from .models import Question


# Quesion모델에 세부 기능을 추가할 수 있는 QuestionAdmin
class QuestionAdmin(admin.ModelAdmin) :
    # 제목 검색을 위해 serch_fields에 subject 추가
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)