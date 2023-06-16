
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.conf import settings

from .models import *
def signin(request):
    return render(request,'signin.html')


def signup(request):
    return render(request,'signup.html')


def coursePage(request):
    return render(request,'addcourse.html')



from django.shortcuts import render, redirect
from .models import courseModel
def addcourse(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        if course:
            data = courseModel(course_name=course)
            data.save()
            return redirect('admintable')
    return render(request, 'addcourse.html')

    
    
from django.shortcuts import get_object_or_404, redirect
from .models import courseModel

def delete_course(request, course_id):
    course = get_object_or_404(courseModel, pk=course_id)
    course.delete()
    return redirect('admintable')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import courseModel, Teacher

def dosignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        age = request.POST['age']
        address=request.POST['address']
        phone = request.POST['phone']
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
        else:
            photo = 'image/im.png'
        username = request.POST['username']
        password = request.POST['password1']
        course_pk = request.POST['course_name']
        course = courseModel.objects.get(pk=course_pk)
        teacher = Teacher(course_name=course,)

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        teacher = Teacher(user=user, course_name=course, gender=gender, age=age,address=address, phone=phone, photo=photo)
        teacher.save()
        login(request, user)
        return redirect('signin')
    else:
        courses = courseModel.objects.all()
        return render(request, 'signup.html', {'courses': courses})












def signup(request):
    courses = courseModel.objects.all()
    print(courses)  # Debugging code
    return render(request, 'signup.html', {'courses': courses})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import courseModel, Teacher
from django.contrib.auth import authenticate

def dosignin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admintable')
            else:
                teacher = Teacher.objects.get(user=user)
                return redirect('teachertable', teacher_id=teacher.id)
    return render(request, 'signin.html')

#teacher table
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Teacher, courseModel

@login_required
def admintable(request):
    teachers = Teacher.objects.all()
    courses = courseModel.objects.all()
    context = {
        'teachers': teachers,
        'courses': courses,
    }
    return render(request, 'admintable.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Teacher

@login_required
def teachertable(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teachertable.html', {'teacher': teacher})




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import courseModel, Teacher

@login_required
def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    courses = courseModel.objects.all()
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        teacher.age = request.POST['age']
        teacher.address = request.POST['address']
        teacher.gender = request.POST['gender']
        teacher.phone = request.POST['phone']
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.course_name = courseModel.objects.get(id=request.POST['course_name'])
        teacher.save()
        return redirect('teachertable', teacher_id=teacher_id)

    return render(request, 'edit_teacher.html', {'teacher': teacher, 'courses': courses})

    
def signup(request):
    courses = courseModel.objects.all()
    print(courses)  # Debugging code
    return render(request, 'signup.html', {'courses': courses})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Teacher

@login_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return redirect('teachertable')



#admin edit and delete
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Teacher, courseModel

def edit_admin(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    courses = courseModel.objects.all()

    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            age = request.POST['age']
            address = request.POST['address']
            gender = request.POST['gender']
            phone = request.POST['phone']
            photo = request.FILES.get('photo')
            course = request.POST['course']

            # Update teacher information
            teacher.user.first_name = first_name
            teacher.user.last_name = last_name
            teacher.user.email = email
            teacher.age = age
            teacher.address = address
            teacher.gender = gender
            teacher.phone = phone
            if photo:
                teacher.photo = photo
            else:
                teacher.photo = 'default.jpg'
            teacher.course_id = course
            teacher.save()

            return redirect('admintable')
        except KeyError as e:
            # Handle missing form data
            messages.error(request, f'Missing form data: {e}')
            return redirect('edit_admin', teacher_id=teacher_id)
    else:
        context = {
            'teacher': teacher,
            'courses': courses,
        }
        return render(request, 'edit_admin.html', context)



@login_required
def delete_admin(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return redirect('admintable')



from django.shortcuts import render, redirect
from .models import Teacher

from django.contrib.auth import logout
from django.shortcuts import redirect

def signout(request):
    # Log the user out
    logout(request)

    # Redirect to the home page
    return redirect('signin')


from django.shortcuts import render, get_object_or_404
from .models import User, Teacher

def signup_details(request, user_id):
    user = get_object_or_404(User, id=user_id)
    teacher = get_object_or_404(Teacher, user=user)
    
    context = {
        'user': user,
        'teacher': teacher,
    }
    return render(request, 'signup_details.html', context)


from django.shortcuts import render, get_object_or_404
from .models import User, Teacher,courseModel

def edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    teacher = get_object_or_404(Teacher, user=user)
    course = courseModel.objects.all()
    
    context = {
        'user': user,
        'teacher': teacher,
        'courses': course,
    }
    return render(request, 'edit.html', context)

from django.shortcuts import render, redirect
from .models import Student, courseModel

def add_student(request):
    courses = courseModel.objects.all()
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        address = request.POST['address']
        gender = request.POST['gender']
        course_pk = request.POST['course_name']
        course = courseModel.objects.get(pk=course_pk)
        student = Student(fname=fname, lname=lname, age=age, address=address, gender=gender, course_name=course)
        student.save()
        return redirect('student-list')
    return render(request, 'add_student.html', {'courses': courses})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, courseModel

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = courseModel.objects.all()
    if request.method == 'POST':
        student.fname = request.POST['fname']
        student.lname = request.POST['lname']
        student.age = request.POST['age']
        student.address = request.POST['address']
        student.gender = request.POST['gender']
        course_pk = request.POST['course_name']
        course = courseModel.objects.get(pk=course_pk)
        student.course_name = course
        student.save()
        return redirect('student-list')
    return render(request, 'edit_student.html', {'student': student, 'courses': courses})
from django.shortcuts import redirect, get_object_or_404
from .models import Student

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('student-list')





from django.shortcuts import render
from .models import Student, courseModel

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list.html', context)

def student_list2(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_list2.html', context)
from django.shortcuts import render
from .models import courseModel

def coursetable(request):
    courses = courseModel.objects.all()
    context = {'courses': courses}
    return render(request, 'coursetable.html', context)

