from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

from profiles.serializer import HelloSerializer
from profiles import serializer
from profiles import models
from profiles import permissions


class HelloAPIView(APIView):
    """Test API VIew"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Return the list of APIView features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, pu, delete)',
            'its similar to a traditional django view',
            'gives the most control over your application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hello!', 'api_view': an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete a particular object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update and delete)',
            'Automatically maps to urls using router',
            'Provides more functionality with less code'
        ]

        return Response({"message": "hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": 'GET'})

    def update(self, request, pk=None):
        """Update  an object by its ID"""
        return Response({"http_method": 'PUT'})

    def partial_update(self, request, pk=None):
        """Partial Update an object by its ID"""
        return Response({"http_method": 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object by its ID"""
        return Response({"http_method": 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle the creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'key',)


class UserLoginView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


