from django.db.models import Model, CharField, TextField, DateField, ForeignKey, CASCADE, DateTimeField


class Event(Model):
    title = CharField(max_length=100)
    description = TextField()
    date = DateField()
    location = CharField(max_length=100)
    organizer_id = CharField(max_length=100)


class Registration(Model):
    user_id = ForeignKey('auth.User', on_delete=CASCADE, related_name='registrations')
    event_id = ForeignKey('apps.Event', on_delete=CASCADE, related_name='registrations')
    registered_at = DateTimeField(auto_now_add=True)