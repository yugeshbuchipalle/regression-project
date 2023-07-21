from rest_framework.views import APIView
from .serializers import ActorSerializers
from .models import Actor
from rest_framework.response import Response


class ActorsList(APIView):# this will enable the get function

    def get(self, request):
        actors = Actor.objects.all()
        seralize = ActorSerializers(actors,many=True)
        return Response(seralize.data)

