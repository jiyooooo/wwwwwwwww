from django.contrib import admin
from django.urls import path, include
from post import urls
from essay import urls
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('essay/', include('essay.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),

]