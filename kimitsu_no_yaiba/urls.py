from django.urls import path
from .views import kimitsuListView, kimitsuDetailView, kimitsuCreateView, kimitsuUpdateView, kimitsuDeleteView

urlpatterns = [
    path('kimitsu/', kimitsuListView.as_view(), name='kimitsu_list'),
    path('kimitsu/<int:pk>/', kimitsuDetailView.as_view(), name='kimitsu_detail'),
    path('kimitsu/create/', kimitsuCreateView.as_view(), name='kimitsu_create'),
    path('kimitsu/<int:pk>/update/', kimitsuUpdateView.as_view(), name='kimitsu_update'),
    path('kimitsu/<int:pk>/delete/', kimitsuDeleteView.as_view(), name='kimitsu_delete'),
]