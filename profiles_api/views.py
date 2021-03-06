from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View Class """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        "Returns a list"
        fruits = [
            'apple','mango','orange'
        ]

        return Response({'message':'Hello','fruits':fruits})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})

