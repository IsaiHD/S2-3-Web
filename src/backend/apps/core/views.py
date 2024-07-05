from django.shortcuts import render
from .models import SucursalGtd, ProductoGtd, PlanesGtd, KnowledgeBase, LogsChat

def index(request):
    sucursales = SucursalGtd.objects.all()
    productos = ProductoGtd.objects.all()
    planes = PlanesGtd.objects.all()
    knowledge_base = KnowledgeBase.objects.all()
    logs_chat = LogsChat.objects.all()

    context = {
        'sucursales': sucursales,
        'productos': productos,
        'planes': planes,
        'knowledge_base': knowledge_base,
        'logs_chat': logs_chat,
    }

    return render(request, 'index.html', context)
