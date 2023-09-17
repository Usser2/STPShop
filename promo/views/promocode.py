from rest_framework import generics
from ..models import PromoCode
from ..serializers import PromoCodeSerializer


class PromoCreateView(generics.CreateAPIView):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    lookup_field = 'id'


class PromoRetrieveView(generics.RetrieveAPIView):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    lookup_field = 'id'


class PromoUpdateView(generics.UpdateAPIView):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    lookup_field = 'id'


class PromoDeleteView(generics.DestroyAPIView):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    lookup_field = 'id'
