from rest_framework import generics
from ..models import Specification
from ..serializers import SpecificationSerializer


class SpecificationCreateView(generics.CreateAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    lookup_field = 'id'


class SpecificationRetrieveView(generics.RetrieveAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    lookup_field = 'id'


class SpecificationUpdateView(generics.UpdateAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    lookup_field = 'id'


class SpecificationDeleteView(generics.DestroyAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    lookup_field = 'id'
