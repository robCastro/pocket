from django.urls import include, path


from expenses.api.v1 import urls


urlpatterns = [
    path('api/v1/', include(urls)),
]
