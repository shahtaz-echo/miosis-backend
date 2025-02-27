from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND


class Custom404View(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
            "status": HTTP_404_NOT_FOUND,
            "success": False,
            "type": "api_error",
            "error": "Provided API endpoint doesnot exist!"
            },
            status=HTTP_404_NOT_FOUND
        )
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)