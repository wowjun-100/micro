"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myshop import views
from rest_framework_jwt.views import obtain_jwt_token
from myshop.models import Real_estate

from django.conf import settings
from django.conf.urls.static import static
from myshop.views import angular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', angular),
    path('api/category/', views.CateViewSet.as_view(), name='category'),
    path('api/realestate/', views.RS_ViewSet.as_view(), name='RS'),
    path('api-token-auth/', obtain_jwt_token),
    path('api/realestate/landmark/', views.LandMark.as_view(), name='Landmark'),
    path('api/realestate/commercial/', views.Commercial.as_view(), name='Commercial'),
    path('api/realestate/residential/', views.Residential.as_view(), name='Residential'),
    path('api/realestate/<int:id>/', views.Detail.as_view(), name='Detail'),
    path('api/signup/', views.Signup.as_view(), name='signup'),
    path('api/realestate/<int:id>/like/', views.Recommand.as_view(), name='Like'),
    path('api/message/recent/', views.RecentMessage.as_view(), name='RecentMessage'),
    path('api/message/<int:id>/', views.DetailMessageView.as_view(), name='DetailMessage'),
    path('api/message/<int:id>/user', views.MessageReceiver.as_view(), name='MessageReceiver')
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
