from manager.views import UploadView, HomeView, Signup, SearchView, FilterView
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('upload/', UploadView.as_view(), name="upload"),
                  path('editmeta/<str:title>/', views.EditMetaView, name="editmeta"),
                  path('signup/', Signup.as_view(), name="signup"),
                  path('search/', SearchView.as_view(), name="search"),
                  path('filter/', FilterView.as_view(), name="filter"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
