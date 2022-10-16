# <editor-fold desc="GET THE STUDENT MARKS ">
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from student.api_v1_admin.serialzers import studentAdminMarksSerializer, \
    studentAdminMarksCreateUpdateSerializer, studentAdminMarksCreateSerializer, studentAdminSubjectCreate, \
    studentAdminMarksCreateSerialzer
from student.models import studentMarksModel, studentStudentModel, studentSubjectsModel


# <editor-fold desc="STUDENT SUBJECTS">
class studentAdminSubjectCreateGenericsView(generics.CreateAPIView,generics.ListAPIView):
    serializer_class = studentAdminMarksSerializer
    queryset = studentSubjectsModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["subject", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        # student=get_object_or_404(studentStudentModel,slug=slug)
        serializer = studentAdminSubjectCreate(data=request.data, context={'request': request})
        print(serializer, "===============serilazers")
        if serializer.is_valid():
            serializer.save(student=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# </editor-fold>


# <editor-fold desc="MARKS CREATE AND GET MARKS LIST">
class studentAdminMarksCreateGenericsView(generics.CreateAPIView,generics.ListAPIView):
    serializer_class = studentAdminMarksSerializer
    queryset = studentMarksModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["subjects", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        # student=get_object_or_404(studentStudentModel,slug=slug)
        serializer = studentAdminMarksCreateSerialzer(data=request.data, context={'request': request})
        print(serializer, "===============serilazers")
        if serializer.is_valid():
            serializer.save(student=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# </editor-fold>


# <editor-fold desc="MARKS DETAILS BY USING SLUG">
class studentAdminMarksDetailsAPIView(APIView):
    serializer_class = studentAdminMarksSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = studentMarksModel.objects.get(slug=slug)
        serializer = studentAdminMarksSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = studentMarksModel.objects.get(slug=slug)
        serializer = studentAdminMarksCreateUpdateSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = studentMarksModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)

# </editor-fold>
