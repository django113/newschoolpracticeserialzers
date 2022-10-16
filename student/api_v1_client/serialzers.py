from rest_framework import serializers, status

from student.models import studentStudentModel, studentSubjectsModel, studentMarksModel
from accounts.api_v1_client.serializers import accountsClientUserCreateSerializer


# <editor-fold desc="STUDENT GET ">
class studentClientStudentGetSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.email")

    class Meta:
        model = studentStudentModel
        fields = '__all__'


# </editor-fold>

# # <editor-fold desc="STUDENT GET AND CREATE">
class studentClientCreateStudentSerializer(serializers.ModelSerializer):
#     """
#         TypeError: Object of type User is not JSON serializable
    # student = serializers.ReadOnlyField()

    # student=accountsClientUserCreateSerializer(read_only=True,many=True)
    # student=serializers.StringRelatedField()
#
#         views post
#         serializer.save(student=self.request.user)
#     """
#     student = serializers.ReadOnlyField(source="student.email")
#
    # def validate_student(self, value):
    #     print("======student=======",value)
    #     student = studentStudentModel.objects.filter(student=value)
    #     if student.exists():
    #         raise serializers.ValidationError({"error": "Your Already existing", 'status': status.HTTP_400_BAD_REQUEST})
    #     return student

    class Meta:
        model = studentStudentModel
        fields = '__all__'
        # read_only_fields = ['student']




# # </editor-fold>

# <editor-fold desc="STUDENT UPDATE">
class studentClientStudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentStudentModel
        fields = '__all__'


# </editor-fold>


# <editor-fold desc="STUDENT SUBJECTS">
class studentClientSubjectCreateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.email")

    def validate_subject(self, value):
        user = self.context['request'].user
        subject = value
        print("subject==============", subject)
        print("user============", user)

        subject = studentSubjectsModel.objects.filter(student=user, subject=subject)
        if subject.exists():
            raise serializers.ValidationError(
                {"error": "subject Already existing", 'status': status.HTTP_400_BAD_REQUEST})
        return value

    class Meta:
        model = studentSubjectsModel
        fields = '__all__'


# </editor-fold>


# <editor-fold desc="STUDENT SUBJECTS">
class studentClientSubjectSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField()

    class Meta:
        model = studentSubjectsModel
        fields = '__all__'


# </editor-fold>


# <editor-fold desc="STUDENT MARKS GET ALL">
class studentClientMarksSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.email")

    class Meta:
        model = studentMarksModel
        fields = '__all__'
# </editor-fold>
