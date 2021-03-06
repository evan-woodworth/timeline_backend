from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import os
from django.views import View


# Create your views here.
class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(viewsets.ModelViewSet):
    # IsAuthenticatedOrReadOnly allows any user to view data, but not interact with it
    # Other permissions => AllowAny / IsAuthenticated (default) / IsAdminUser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ExtendedUserView(viewsets.ModelViewSet):
    serializer_class = ExtendedUserSerializer
    queryset = ExtendedUser.objects.all()

class DisplayTypeView(viewsets.ModelViewSet):
    serializer_class = DisplayTypeSerializer
    queryset = DisplayType.objects.all()

class TimelineView(viewsets.ModelViewSet):
    serializer_class = TimelineSerializer
    queryset = Timeline.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class EntryView(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()