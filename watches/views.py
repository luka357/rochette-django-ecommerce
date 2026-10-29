from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Watch, Category, ContactMessage
from .permissions import IsAdminOrReadOnly
from .serializers import WatchSerializer, CategorySerializer, ContactMessageSerializer, RegisterSerializer


# მომხმარებლის რეგისტრაცია
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)


# საკონტაქტო შეტყობინების შენახვა
class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]


# საათების სია და დამატება
class WatchListCreateView(generics.ListCreateAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['price', 'name']
    filterset_fields = ['category']


# საათის დეტალი, განახლება, წაშლა
class WatchRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = [IsAdminOrReadOnly]


# კატეგორიების სია და დამატება
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]