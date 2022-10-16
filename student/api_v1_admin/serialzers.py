# <editor-fold desc="STUDENT UPDATE">
from django.forms import model_to_dict
from rest_framework import serializers

from student.api_v1_client.serialzers import studentClientSubjectCreateSerializer, studentClientStudentGetSerializer
from student.models import studentMarksModel, studentSubjectsModel, studentStudentModel


# <editor-fold desc="STUDENT SUBJECTS GET">
class studentAdminSubjectGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentSubjectsModel
        fields = ['subject', 'slug']


# </editor-fold>


# <editor-fold desc="STUDENT MARKS GET">
class studentAdminMarksSerializer(serializers.ModelSerializer):
    """
    TypeError: Object of type studentStudentModel is not JSON serializable
    """
    student = serializers.SerializerMethodField(source="student.email")

    def get_student(self, obj):
        try:
            student = model_to_dict(obj.student)
        except:
            student = {}
        return student

    # studentMarksModel_subject = serializers.StringRelatedField(many=True,read_only=True)
    subjects = studentAdminSubjectGetSerializer(many=True, read_only=True)

    class Meta:
        model = studentMarksModel
        fields = ['student', 'subjects', 'marks', 'total_marks', 'grade', 'date_created',
                  'slug', ]


# </editor-fold>


# <editor-fold desc="STUDENT MARKS update ">
class studentAdminMarksCreateUpdateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.email")

    class Meta:
        model = studentMarksModel
        fields = '__all__'


# </editor-fold>


# <editor-fold desc="STUDENT MARKS GET">
class studentAdminMarksCreateSerializer(serializers.ModelSerializer):
    """
    ValueError: Cannot assign "<User: vishnu@gmail.com>": "studentMarksModel.student" must be a "studentStudentModel" instance.

    """
    # student = studentClientStudentGetSerializer(many=True, read_only=True)
    # subjects = studentClientSubjectCreateSerializer(many=True, read_only=True)
    # subjects_all = serializers.SerializerMethodField()

    # def get_subjects_all(self, obj):
    #     try:
    #         subjects = obj.get_subjects()
    #     except:
    #         subjects={}
    #     return subjects

    student = serializers.ReadOnlyField(source="student.email")

    studentMarksModel_subject = serializers.StringRelatedField(many=True)

    # studentMarksModel_subject=serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='subject'
    # )

    class Meta:
        model = studentMarksModel
        fields = ['student', 'studentMarksModel_subject', 'marks', 'total_marks', 'grade', 'date_created',
                  'slug', ]

        # read_only_fields = ['student', 'subjects']


# </editor-fold>


# <editor-fold desc="CREATE SUBJECT">
class studentAdminSubjectCreate(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.email")
    score_marks = serializers.IntegerField(required=True)

    def validate(self,data):
        print("data===============",data)
        user=self.context['request'].user
        subject=data['subject']

        print('user======',user,subject)
        subjects_user=studentSubjectsModel.objects.filter(student=user,subject__iexact=subject)
        if subjects_user.exists():
            raise serializers.ValidationError({"message":"subject Already exists"})
        return data

    class Meta:
        model = studentSubjectsModel
        fields = ['student','subject', 'score_marks']


# </editor-fold>


# <editor-fold desc="STUDENT MARKS CREATE">
class studentAdminMarksCreateSerialzer(serializers.ModelSerializer):
    class Meta:
        model=studentMarksModel
        field='__all__'

    def create(self, validated_data):
        print(validated_data,"validate data")
        return validated_data
# </editor-fold>
