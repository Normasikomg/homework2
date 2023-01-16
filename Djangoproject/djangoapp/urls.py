from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.AppDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.AppUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.AppDeleteView.as_view(), name='delete')
]
