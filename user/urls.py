from django.urls import path,include
from .views import hello,RegisterAPIView,signin,AuthAPIView,refreshToken


urlpatterns = [
    path("hello/",hello),
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
    path('signin/',signin),
    path("refresh/",refreshToken)
]
