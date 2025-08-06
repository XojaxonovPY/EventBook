from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.models import Event, Registration
from apps.serializer import UserModelSerializer, EventModelSerializer, RegistrationModelSerializer


@extend_schema(tags=['login-register'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['login-register'])
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['login-register'])
class RegisterCreateAPIView(CreateAPIView):
    serializer_class = UserModelSerializer


@extend_schema(tags=['event'])
class EventCreateAPIView(CreateAPIView):
    serializer_class = EventModelSerializer

    def perform_create(self, serializer):
        serializer.save(organizer_id=self.request.user)


@extend_schema(tags=['event'])
class EventListAPIView(ListAPIView):
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()


@extend_schema(tags=['event'])
class EventRetrieveAPIView(RetrieveAPIView):
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    lookup_url_kwarg = 'pk'


@extend_schema(tags=['event'])
class UserEventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(organizer_id=self.request.user)
        return query


@extend_schema(tags=['registration'])
class EventRegisterCreateAPIView(CreateAPIView):
    serializer_class = RegistrationModelSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


@extend_schema(tags=['registration'])
class RegisterEventListAPIView(ListAPIView):
    serializer_class = RegistrationModelSerializer
    queryset = Registration.objects.all()

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user_id=self.request.user)
        return query
