from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.serializer import HelloSerializer


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

