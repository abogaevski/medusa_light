from django.contrib.auth.views import LoginView
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Medusa Light API",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email="antnbog@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html', next_page='/news/add'), name='login_url'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_url'),

]
