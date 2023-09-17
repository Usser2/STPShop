from rest_framework import generics
from ..models import UsedPromoCode
from ..serializers import UsedPromoCodeSerializer


class UsedPromoCreateView(generics.CreateAPIView):
    queryset = UsedPromoCode.objects.all()
    serializer_class = UsedPromoCodeSerializer
    lookup_field = 'id'


class UsedPromoRetrieveView(generics.RetrieveAPIView):
    queryset = UsedPromoCode.objects.all()
    serializer_class = UsedPromoCodeSerializer
    lookup_field = 'id'


class UsedPromoUpdateView(generics.UpdateAPIView):
    queryset = UsedPromoCode.objects.all()
    serializer_class = UsedPromoCodeSerializer
    lookup_field = 'id'


class UsedPromoDeleteView(generics.DestroyAPIView):
    queryset = UsedPromoCode.objects.all()
    serializer_class = UsedPromoCodeSerializer
    lookup_field = 'id'
