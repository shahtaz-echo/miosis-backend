from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

class Custom404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return Response(
                {
                "status": HTTP_404_NOT_FOUND,
                "success": False,
                "type":"api_error",
                "error": "Provided API endpoint doesnot exist!"
                },
                status=HTTP_404_NOT_FOUND
            )