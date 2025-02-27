from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.status import HTTP_404_NOT_FOUND

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    print("-----------------------------")
    print(exc)

    if response is None:
        return Response(
            {
            "status": HTTP_404_NOT_FOUND,
            "success": False,
            "type":"api_error",
            "error": "Provided API endpoint doesnot exist!"
            },
            status=HTTP_404_NOT_FOUND
        )