from django.urls import path
from .views import homePageView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', homePageView, name='home'),
]
