from django.shortcuts import render

# Create your views here.

from mvcapp.models import Student


def welcome_page(request):
    return render(request, template_name='student_welcome.html')


def save_update_student_information(req):
    message = ''
    if req.method == 'POST':
        formdata = req.POST
    #elif req.method == 'GET':
    #    formdata = req.GET

        sid = formdata.get('id')
        stud = Student.objects.filter(id=sid).first()

        if formdata:
            if not stud:

                #ye hum usually karte hai jab model.py aur addstudentd.html ke nam alaga ho
                stud = Student(name=formdata.get('name'), age=formdata.get('age'),
                               fees=formdata.get('fees'), dept=formdata.get('dept'),
                               email=formdata.get('email'))

                if int(sid):
                    stud.id = sid

                stud.save()
                message = 'Student Record Saved...'
            else:
                stud.name = formdata.get('name')
                stud.fees = formdata.get('fees')
                stud.dept = formdata.get('dept')
                stud.age = formdata.get('age')
                stud.email = formdata.get('email')
                stud.save()
                message = 'Student Record Updated...'
    #Student(**formdata)     #jab dono name same ho to ye karna hai
    return render(req, template_name='add_student.html', context={"result": message, 'student': Student(name='', age=0, fees=0.0, dept='', email='', id=0)})


def fetch_student_for_edit(request, sid):
    student = Student.objects.get(id=sid)
    return render(request, template_name='add_student.html', context={"student": student})


def delete_student_record(req, sid):

    stud = Student.objects.get(id=sid)
    stud.delete()
    stud_list = Student.objects.all()
    return render(req, template_name='student_list.html',
                  context={"student_list": stud_list})


def show_list_of_students(req):
    stud_list = Student.objects.all()
    return render(req, template_name='student_list.html',
                  context={"student_list": stud_list})


age_flag = True
fees_flag = True
def sorting_logic(req, val):
    global age_flag
    global fees_flag

    if val == 'fees':
        if fees_flag:
            fees_flag=False
            stud_list = Student.objects.order_by(val)[::-1]
        else:
            fees_flag = True
            stud_list = Student.objects.order_by(val)

    if val == 'age':
        if age_flag:
            age_flag = False
            stud_list = Student.objects.order_by(val)[::-1]
        else:
            age_flag = True
            stud_list = Student.objects.order_by(val)

    return render(req, template_name='student_list.html',
                  context={"student_list": stud_list})
