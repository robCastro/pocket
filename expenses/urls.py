from django.urls import include, path


from expenses.api.v1.urls import router


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
