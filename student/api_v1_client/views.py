# <editor-fold desc="GET ALL PRODUCT BRANDS AND CREATE PRODUCT BRAND">
from rest_framework import status, generics, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from student.api_v1_client.serialzers import studentClientSubjectSerializer, \
    studentClientSubjectCreateSerializer, studentClientStudentUpdateSerializer, studentClientStudentGetSerializer, \
    studentClientMarksSerializer,studentClientCreateStudentSerializer
from student.models import studentStudentModel, studentSubjectsModel, studentMarksModel

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# <editor-fold desc="STUDENT CREATE AND STUDENT GET ALL LIST">
class studentClientStudentGetGenericsView(generics.ListAPIView):
    serializer_class = studentClientStudentGetSerializer
    queryset = studentStudentModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        # s_name_brand = studentStudentModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

class studentClientStudentCreateGenericsView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def post(self, request):
        serializer = studentClientCreateStudentSerializer(data=request.data, context={'request': request})
        print(serializer, "===============serilazers")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="STUDENT DETAILS BY USING SLUG">
class studentClientStudentDetailsAPIView(APIView):
    serializer_class = studentClientStudentGetSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = studentStudentModel.objects.get(slug=slug)
        serializer = studentClientStudentGetSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = studentStudentModel.objects.get(slug=slug)
        serializer = studentClientStudentUpdateSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = studentStudentModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


# </editor-fold>

# <editor-fold desc="SUBJECT CREATE AND SUBJECT GET ALL LIST">
class studentClientSubjectCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = studentClientSubjectSerializer
    queryset = studentSubjectsModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = studentClientSubjectCreateSerializer(data=request.data, context={'request': request})
        print(serializer, "===============serilazers")
        if serializer.is_valid():
            serializer.save(student=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="STUDENT DETAILS BY USING SLUG">
class studentClientMarksDetailsAPIView(APIView):
    serializer_class = studentClientMarksSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = studentMarksModel.objects.get(slug=slug)
        serializer = studentClientMarksSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


# </editor-fold>