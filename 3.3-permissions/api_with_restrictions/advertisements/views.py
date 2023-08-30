from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Advertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer


class DateFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description',
                  'creator', 'status', 'created_at']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DateFilter

    throttle_classes = [AnonRateThrottle]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
