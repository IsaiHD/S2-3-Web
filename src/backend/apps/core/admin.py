from django.contrib import admin
from apps.core.models import SucursalGtd, ProductoGtd, PlanesGtd, KnowledgeBase, LogsChat

# Registra tus modelos en el panel de administración
admin.site.register(SucursalGtd)
admin.site.register(ProductoGtd)
admin.site.register(PlanesGtd)
admin.site.register(KnowledgeBase)
admin.site.register(LogsChat)
