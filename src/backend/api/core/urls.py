from django.urls import path
from api.core.apiviews import (
    SucursalGtdDetail, SucursalGtdList,
    ProductoGtdDetail, ProductoGtdList,
    PlanesGtdDetail, PlanesGtdList,
    KnowledgeBaseDetail, KnowledgeBaseList,
    LogsChatDetail, LogsChatList,
)

urlpatterns = [
    path('sucursales/', SucursalGtdList.as_view(), name='sucursal-list'),
    path('sucursales/<int:pk>/', SucursalGtdDetail.as_view(), name='sucursal-detail'),

    path('productos/', ProductoGtdList.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoGtdDetail.as_view(), name='producto-detail'),
    
    path('planes/', PlanesGtdList.as_view(), name='plan-list'),
    path('planes/<int:pk>/', PlanesGtdDetail.as_view(), name='plan-detail'),

    path('knowledge/', KnowledgeBaseList.as_view(), name='knowledge-list'),
    path('knowledge/<int:pk>/', KnowledgeBaseDetail.as_view(), name='knowledge-detail'),

    path('logs-chat/', LogsChatList.as_view(), name='logs-chat-list'),
    path('logs-chat/<int:pk>/', LogsChatDetail.as_view(), name='logs-chat-detail'),
]
