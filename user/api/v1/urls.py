from django.urls import path
from .views import UserRegistrationViews

user_urls = [
    path('register/', UserRegistrationViews.as_view(), name="create-user")
    # path('login/', login, name="auth-tokens"),
]

admin_urls = [
    # path('admin/user-list', name='user-list'),
]


urlpatterns = user_urls + admin_urls