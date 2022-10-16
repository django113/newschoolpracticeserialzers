# <editor-fold desc="user create">
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import practiceClientUserCreateSerializer


# <editor-fold desc="USER CREATE OR USER REGISTRATION">
class accountsClientUserCreateGenericsView(generics.CreateAPIView):

    def post(self, request):
        serializer = practiceClientUserCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(student=self.request.user)
            return Response({'msg': "Your Accounts is Successfully Created"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>
