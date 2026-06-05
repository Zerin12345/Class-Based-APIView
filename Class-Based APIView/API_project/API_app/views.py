from rest_framework.views import APIView
from rest_framework.response import Response
from API_app.models import *
from API_app.serializers import *

class StudentAPIView(APIView):
    def get(self, request):
        student = StudentModel.objects.all()
        serializer = StudentSerializers(student, many=True)

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "data": serializer.data,
        })
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Data created successfully",
                "data": serializer.data,
            })
        else:
            return Response({
                "success": False,
                "message": "Data creation failed",
                "errors": serializer.errors,
            })
class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            student = StudentModel.objects.get(pk=pk)
            serializer = StudentSerializers(student)
            return Response({
                "success": True,
                "message": "Data fetched successfully",
                "data": serializer.data,
            })
        except StudentModel.DoesNotExist:
            return Response({
                "success": False,
                "message": "Data not found",
            })
    def put(self, request, pk):
        try:
            student = StudentModel.objects.get(pk=pk)
            serializer = StudentSerializers(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Data updated successfully",
                    "data": serializer.data,
                })
            else:
                return Response({
                    "success": False,
                    "message": "Data update failed",
                    "errors": serializer.errors,
                })
        except StudentModel.DoesNotExist:
            return Response({
                "success": False,
                "message": "Data not found",
            })
    def delete(self, request, pk):
        try:
            student = StudentModel.objects.get(pk=pk)
            student.delete()
            return Response({
                "success": True,
                "message": "Data deleted successfully",
            })
        except StudentModel.DoesNotExist:
            return Response({
                "success": False,
                "message": "Data not found",
            })
    