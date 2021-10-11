from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views


urlpatterns = [
    path('accounts/', views.UserList.as_view()),
    path('accounts/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
