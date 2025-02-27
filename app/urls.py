from django.contrib import admin
from django.urls import path, include
from app.utils.custom_404_view import Custom404View
from django.http import JsonResponse

def error_404(request, exception):
    message = "Resource not found"
    return JsonResponse(data={'message': message}, status=404)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.api.urls.client.urls_v1')),
    path('api/v1/products/', include('products.api.v1.urls'))
]

handler404 = error_404