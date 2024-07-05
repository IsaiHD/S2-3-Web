from .models import SucursalGtd, ProductoGtd, PlanesGtd, KnowledgeBase, LogsChat
from .serializers import SucursalGtdSerializer, ProductoGtdSerializer, PlanesGtdSerializer, KnowledgeBaseSerializer, LogsChatSerializer
from django.http import Http404

def get_sucursal(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            sucursal = SucursalGtd.objects.get(pk=pk)
            return SucursalGtdSerializer(sucursal).data
        except SucursalGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def get_producto(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            producto = ProductoGtd.objects.get(pk=pk)
            return ProductoGtdSerializer(producto).data
        except ProductoGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def get_plan(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            plan = PlanesGtd.objects.get(pk=pk)
            return PlanesGtdSerializer(plan).data
        except PlanesGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def get_knowledge(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            knowledge = KnowledgeBase.objects.get(pk=pk)
            return KnowledgeBaseSerializer(knowledge).data
        except KnowledgeBase.DoesNotExist:
            raise Http404
    else:
        raise Http404

def get_logs_chat(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            log_chat = LogsChat.objects.get(pk=pk)
            return LogsChatSerializer(log_chat).data
        except LogsChat.DoesNotExist:
            raise Http404
    else:
        raise Http404

def traer_sucursales(request):
    sucursales = SucursalGtd.objects.all()
    return SucursalGtdSerializer(sucursales, many=True).data

def traer_productos(request):
    productos = ProductoGtd.objects.all()
    return ProductoGtdSerializer(productos, many=True).data

def traer_planes(request):
    planes = PlanesGtd.objects.all()
    return PlanesGtdSerializer(planes, many=True).data

def traer_knowledge(request):
    knowledge = KnowledgeBase.objects.all()
    return KnowledgeBaseSerializer(knowledge, many=True).data

def traer_logs_chat(request):
    logs_chat = LogsChat.objects.all()
    return LogsChatSerializer(logs_chat, many=True).data

def guardar_sucursal(**kwargs):
    if 'nombre_sucursal' in kwargs and kwargs.get('nombre_sucursal') != "" and type(kwargs.get('nombre_sucursal')) == str:
        s = SucursalGtd.objects.create(nombre_sucursal=kwargs.get('nombre_sucursal'))
        s.ubicacion = kwargs.get('ubicacion') if 'ubicacion' in kwargs else None
        s.save()
        return True
    else:
        return False

def guardar_producto(**kwargs):
    if 'product_name' in kwargs and kwargs.get('product_name') != "" and type(kwargs.get('product_name')) == str:
        p = ProductoGtd.objects.create(product_name=kwargs.get('product_name'))
        p.description = kwargs.get('description') if 'description' in kwargs else None
        p.save()
        return True
    else:
        return False

def guardar_plan(**kwargs):
    if 'id_producto' in kwargs and 'price' in kwargs and 'id_knowledge' in kwargs:
        try:
            id_producto = ProductoGtd.objects.get(pk=kwargs.get('id_producto'))
            id_knowledge = KnowledgeBase.objects.get(pk=kwargs.get('id_knowledge'))
            pl = PlanesGtd.objects.create(id_producto=id_producto, price=kwargs.get('price'), id_knowledge=id_knowledge)
            pl.save()
            return True
        except (ProductoGtd.DoesNotExist, KnowledgeBase.DoesNotExist):
            return False
    else:
        return False
    
def guardar_knowledge(**kwargs):
    if 'tema' in kwargs and kwargs.get('tema') != "" and type(kwargs.get('tema')) == str:
        k = KnowledgeBase.objects.create(tema=kwargs.get('tema'))
        k.subtema = kwargs.get('subtema') if 'subtema' in kwargs else None
        k.pregunta = kwargs.get('pregunta') if 'pregunta' in kwargs else None
        k.respuesta = kwargs.get('respuesta') if 'respuesta' in kwargs else None
        k.save()
        return True
    else:
        return False
def guardar_logs_chat(**kwargs):
    if 'chat_type' in kwargs and kwargs.get('chat_type') != "" and type(kwargs.get('chat_type')) == str:
        try:
            id_sucursal = SucursalGtd.objects.get(pk=kwargs.get('id_sucursal'))
            id_producto = ProductoGtd.objects.get(pk=kwargs.get('id_producto'))
            lc = LogsChat.objects.create(chat_type=kwargs.get('chat_type'), id_sucursal=id_sucursal, id_producto=id_producto)
            lc.chat_description = kwargs.get('chat_description') if 'chat_description' in kwargs else None
            lc.chat_pregunta = kwargs.get('chat_pregunta') if 'chat_pregunta' in kwargs else None
            lc.chat_respuesta = kwargs.get('chat_respuesta') if 'chat_respuesta' in kwargs else None
            lc.save()
            return True
        except (SucursalGtd.DoesNotExist, ProductoGtd.DoesNotExist):
            return False
    else:
        return False

def borrar_sucursal(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            SucursalGtd.objects.get(pk=pk).delete()
            return True
        except SucursalGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def borrar_producto(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            ProductoGtd.objects.get(pk=pk).delete()
            return True
        except ProductoGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def borrar_plan(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            PlanesGtd.objects.get(pk=pk).delete()
            return True
        except PlanesGtd.DoesNotExist:
            raise Http404
    else:
        raise Http404

def borrar_knowledge(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            KnowledgeBase.objects.get(pk=pk).delete()
            return True
        except KnowledgeBase.DoesNotExist:
            raise Http404
    else:
        raise Http404

def borrar_logs_chat(pk=None):
    if pk is not None:
        try:
            pk = int(pk)
            LogsChat.objects.get(pk=pk).delete()
            return True
        except LogsChat.DoesNotExist:
            raise Http404
    else:
        raise Http404
