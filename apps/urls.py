from django.urls import path
from apps.views import *

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('create/event/', EventCreateAPIView.as_view()),
    path('list/event/', EventListAPIView.as_view()),
    path('registeration/event', EventRegisterCreateAPIView.as_view()),
    path('list/user/event/', UserEventListAPIView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh')
]
