from django.urls import path
from . import views  # 현재 위치의 views.py

app_name = 'bulletin_board'
urlpatterns = [  # ''와 index 주소 매핑 후 함수 views.index 부르기
    path('', views.index, name='index'),  # 방법 2가지: python 함수, class(재사용성 증가)
]