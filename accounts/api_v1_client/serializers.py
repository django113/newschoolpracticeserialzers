from django.contrib.auth import get_user_model
from rest_framework import serializers
# from student.api_v1_client.serialzers import studentClientCreateStudentSerializer
# from student.models import studentStudentModel
User = get_user_model()


# <editor-fold desc="USER CREATE ">
class accountsClientUserCreateSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=True)
    password = serializers.CharField(required=True)
  
    class Meta:
        model = User
        fields = ('student','phone', 'password', 'email', 'dob', 'slug')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # student=validated_data.pop('student', None)
        # print("student======",student)
        # student_data=studentStudentModel.objects.create(student=user,**validated_data)
        return user
# </editor-fold>


# # <editor-fold desc="USER CREATE ">
# class accountsClientUserCreateSerializer(serializers.ModelSerializer):
#     dob = serializers.DateField(required=True)
#     password = serializers.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ('phone', 'password', 'email', 'dob', 'slug')

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)

#         return user
# # </editor-fold>

# <editor-fold desc="GET USER DETAIL">
class accountsClientUserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


# </editor-fold>