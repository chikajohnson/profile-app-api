from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    """Test API VIew"""

    def get(self, request, format=None):
        """Return the list of APIView features"""
        an_apiview = [
            'Uses HTTP method as functions (get, post, pu, delete)',
            'its similar to a traditional django view',
            'gives the most control over your application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hello!', 'api_view': an_apiview})
