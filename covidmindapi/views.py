from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Activity
from .serializers import ActivitySerializer


class LatestActivities(generics.ListAPIView):
    queryset = Activity.objects.filter(visible=True).order_by('-date')[:100]
    serializer_class = ActivitySerializer


class AllActivities(generics.ListAPIView):
    queryset = Activity.objects.filter(visible=True)
    serializer_class = ActivitySerializer


class ActivityDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Activity, pk=pk)

    def get(self, request, pk):
        activity = self.get_object(pk=pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
