from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from apps.models import Event, Registration


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)

    def validate_password(self, value):
        return make_password(value)


class EventModelSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields=('id','title','description','date','location','organizer_id')
        read_only_fields = ('id','organizer_id')


class RegistrationModelSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields=('id','event_id','user_id')
        read_only_fields = ('id','user_id')


