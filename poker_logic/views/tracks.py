from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from ..models.tracks_and_topics import Track_headings, TrackHeadingsSerializer


@permission_classes((permissions.AllowAny,))
@api_view(['GET', 'POST'])
def tracks_all(request):

    track_headings_queryset = Track_headings.objects.all()
    queryset = User.objects.none()
    track_heading_serializer = TrackHeadingsSerializer(track_headings_queryset, many=True)
    #
    # track_headings_queryset_1 = Track_headings.objects.all()

    # track_heading_serializer = TrackHeadingsSerializerTest(track_headings_queryset, many=True)

    print(track_headings_queryset)

    context = {
         'track_headings': track_heading_serializer.data,
         'username': request.user.username
    }
    return Response(context)
