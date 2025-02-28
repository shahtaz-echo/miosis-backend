from django.http import JsonResponse
from rest_framework.status import HTTP_404_NOT_FOUND
from django.shortcuts import render 

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        response = self.get_response(request)
        print(request.path)

        if response.status_code == 404 and request.path.startswith("/api"):    
            return JsonResponse(
                {
                    "status": HTTP_404_NOT_FOUND,
                    "success": False,
                    "type":"api_error",
                    "message": "Provided API endpoint doesnot exist!"
                },
                status=HTTP_404_NOT_FOUND
            )
        