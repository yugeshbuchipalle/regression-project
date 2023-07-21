from rest_framework import serializers
from .models import Actor

class ActorSerializers(serializers.SerializerMetaclass):
    class Meta:
        model = Actor
        fields = '__all__'
