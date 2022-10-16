from django.contrib.auth import get_user_model
from rest_framework import serializers
# from student.api_v1_client.serialzers import studentClientCreateStudentSerializer
# from student.models import studentStudentModel
from practice.models import PracticeSubjectModel,PracticeStudentMainModel

User = get_user_model()
def email_unique(value):
    user = User.objects.filter(email=value)
    if user.exists():
        raise serializers.ValidationError({'message':"email already exists"})

# <editor-fold desc="STUDENT AND SUBJECT CREATE ">
class practiceClientUserCreateSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True,validators=[email_unique])
    phone = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)

    description = serializers.CharField(required=True)
    # marks = serializers.CharField(required=True)
    marks_gain = serializers.IntegerField(required=True)
    
    title=serializers.ListField(child=serializers.CharField(max_length=100),write_only=True)
    
    class Meta:
        model=PracticeSubjectModel
        # fields='__all__'
        fields = ('title','description','marks','marks_gain','student','phone', 'password', 'email', 'dob','name')
        read_only_fields=['student']

    def create(self,validated_data):
        # title=validate_data.pop['title', None]
        dob=validated_data['dob']
        password=validated_data['password']
        email=validated_data['email']
        phone=validated_data['phone']
        name=validated_data['name']
        print("user data========",dob,password,email,phone,name)
        title=validated_data.pop('title', [])
        user = User.objects.create_user(
            dob=validated_data['dob'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
        )
        print(user,'===========user created============')


        print("subjects======",title)
        print("validate data======",validated_data)
        if user:
            for sub in title:
                print("=============data====",sub)

                instance_subject=PracticeSubjectModel.objects.create(student=user,
                            title=sub,
                            description=validated_data['description'],
                            marks_gain=validated_data['marks_gain'],
                )

                print(instance_subject,"==========subject===============")
        
                marks_gain = PracticeSubjectModel.objects.all().filter(student=user).values_list('marks_gain', flat=True)
                marks = PracticeSubjectModel.objects.all().filter(student=user).values_list('marks', flat=True)



                # student_subject=PracticeStudentMainModel.objects.filter(student=user)

                # if student_subject.exists():
                try:
                    instance_student=PracticeStudentMainModel.objects.get(student=user)
                except:
                    instance_student=PracticeStudentMainModel.objects.create(student=user)

                instance_student.total_marks=sum(marks_gain)
            
                student_grade = (sum(marks_gain) /sum(marks) ) * 100
                print("percentage======3=======", student_grade)
                if student_grade >= 100:
                    instance_student.grade = "A"
                elif student_grade >= 80:
                    instance_student.grade = "B"
                elif student_grade >= 60:
                    instance_student.grade = "C"
                elif student_grade >= 40:
                    instance_student.grade = "D"
                elif student_grade >= 35 or student_grade < 40:
                    instance_student.grade = "E"
                elif student_grade < 35:
                    instance_student.grade = "F"
                
                instance_student.save()
                instance_student.subjects.add(instance_subject.id)

        else:
            user.delete()
            
        return validated_data



#     # class Meta:
#     #     model = User
#     #     fields = ('student','phone', 'password', 'email', 'dob', 'slug')

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         # student=validated_data.pop('student', None)
#         # print("student======",student)
#         # student_data=studentStudentModel.objects.create(student=user,**validated_data)
#         return user
# # </editor-fold>


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