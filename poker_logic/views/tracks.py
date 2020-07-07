from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from ..models.tracks_and_topics import Track_headings, TrackHeadingsSerializer


# @permission_classes((permissions.AllowAny,))
#
@authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def tracks_all(request):

    track_headings_queryset = Track_headings.objects.all()
    track_heading_serializer = TrackHeadingsSerializer(track_headings_queryset, many=True)

    context = {
         'track_headings': track_heading_serializer.data,
         'username': request.user.username
    }
    return Response(context)
