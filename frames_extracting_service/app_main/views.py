from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Media, MediaFrames
from .serializers import MediaSerizlier, MediaFramesSerializer, FrameSerializer
from .services import frames_extracting_service



class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerizlier


class MediaFramesView(APIView):
    queryset = MediaFrames.objects.all()
    serializer_class = MediaFramesSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid()
        validated_data = serializer_data.validated_data
        media = validated_data['media']
        result = frames_extracting_service.extract(media)
        return Response(FrameSerializer(result, many=True).data)