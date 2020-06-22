from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_api import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductApiViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryListOnlyApiView.as_view()),
    re_path(r'vendas/(?P<pk>\d+)?', views.OrderApiView.as_view()),
    path('get_token', obtain_auth_token)
    # username e um password
]
