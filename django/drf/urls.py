"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'ncwellwise_subset_20102019', views.ncwellwise_subset_20102019)
#router.register(r'triangle_tracts', views.triangle_tracts_View)
router.register(r'ncwellwise_subset_20102019_geom', views.drf_ncwellwise_subset_20102019_geom_View)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
