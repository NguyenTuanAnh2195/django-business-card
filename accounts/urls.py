from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from accounts import views


urlpatterns = [
    path("current-user", views.current_user),
    path("signup", views.UserCreate.as_view()),
    path("", views.UserList.as_view()),
    path("<int:pk>", views.UserDetail.as_view()),
    path("token-auth", obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
