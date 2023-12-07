from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

# pybo/로 시작하는 페이지를 요청하면 이제 pybo/urls.py 파일의 매핑 정보를 읽어서
# 처리하라는 의미다. 하위 파일이 생성되더라도 경로를 새로 추가할 필요가 없어 진다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
   
]
