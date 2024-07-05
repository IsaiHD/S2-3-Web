from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core import utils

class SucursalGtdDetail(APIView):
    def get(self, request, pk):
        response = utils.get_sucursal(pk)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def post(self, request):
        saved = utils.guardar_sucursal(**request.data)
        status_code = status.HTTP_201_CREATED if saved else status.HTTP_400_BAD_REQUEST
        return Response(status=status_code)
    
    def delete(self, request, pk):
        deleted = utils.borrar_sucursal(pk)
        status_code = status.HTTP_204_NO_CONTENT if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

# Vista para listar todas las SucursalGtd
class SucursalGtdList(APIView):
    def get(self, request):
        response = utils.traer_sucursales(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
# ProductoGtd
class ProductoGtdDetail(APIView):
    def get(self, request, pk):
        response = utils.get_producto(pk)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def post(self, request):
        saved = utils.guardar_producto(**request.data)
        status_code = status.HTTP_201_CREATED if saved else status.HTTP_400_BAD_REQUEST
        return Response(status=status_code)
    
    def delete(self, request, pk):
        deleted = utils.borrar_producto(pk)
        status_code = status.HTTP_204_NO_CONTENT if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class ProductoGtdList(APIView):
    def get(self, request):
        response = utils.traer_productos(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
        

# PlanesGtd
class PlanesGtdDetail(APIView):
    def get(self, request, pk):
        response = utils.get_plan(pk)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def post(self, request):
        saved = utils.guardar_plan(**request.data)
        status_code = status.HTTP_201_CREATED if saved else status.HTTP_400_BAD_REQUEST
        return Response(status=status_code)
    
    def delete(self, request, pk):
        deleted = utils.borrar_plan(pk)
        status_code = status.HTTP_204_NO_CONTENT if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class PlanesGtdList(APIView):
    def get(self, request):
        response = utils.traer_planes(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
        

# KnowledgeBase
class KnowledgeBaseDetail(APIView):
    def get(self, request, pk):
        response = utils.get_knowledge(pk)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def post(self, request):
        saved = utils.guardar_knowledge(**request.data)
        status_code = status.HTTP_201_CREATED if saved else status.HTTP_400_BAD_REQUEST
        return Response(status=status_code)
    
    def delete(self, request, pk):
        deleted = utils.borrar_knowledge(pk)
        status_code = status.HTTP_204_NO_CONTENT if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class KnowledgeBaseList(APIView):
    def get(self, request):
        response = utils.traer_knowledge(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)


# LogsChat
class LogsChatDetail(APIView):
    def get(self, request, pk):
        response = utils.get_logs_chat(pk)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def post(self, request):
        saved = utils.guardar_logs_chat(**request.data)
        status_code = status.HTTP_201_CREATED if saved else status.HTTP_400_BAD_REQUEST
        return Response(status=status_code)
    
    def delete(self, request, pk):
        deleted = utils.borrar_logs_chat(pk)
        status_code = status.HTTP_204_NO_CONTENT if deleted else status.HTTP_404_NOT_FOUND
        return Response(status=status_code)

class LogsChatList(APIView):
    def get(self, request):
        response = utils.traer_logs_chat(request)
        status_code = status.HTTP_404_NOT_FOUND if not response else status.HTTP_200_OK
        return Response(response, status=status_code)
