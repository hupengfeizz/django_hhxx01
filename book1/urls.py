from django.urls import path
from book1.views import index

urlpatterns = [
    # path(路由，视图函数名）
    path('index/',index)

]