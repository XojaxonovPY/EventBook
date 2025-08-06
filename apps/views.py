from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.models import Event
from apps.serializer import UserModelSerializer, EventModelSerializer, RegistrationModelSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class CustomTokenRefreshView(TokenRefreshView):
    pass


class RegisterCreateAPIView(CreateAPIView):
    serializer_class = UserModelSerializer


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventModelSerializer

    def perform_create(self, serializer):
        serializer.save(organizer_id=self.request.user)


class EventListAPIView(ListAPIView):
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()


class EventRegisterCreateAPIView(CreateAPIView):
    serializer_class = RegistrationModelSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UserEventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    def get_queryset(self):
        query=super().get_queryset()
        query=query.filter(organizer_id=self.request.user)
        return query


