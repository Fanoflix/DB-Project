from flask import Blueprint,render_template,redirect,url_for,flash,session
from myproject import db,g
from myproject.models import Student, Teacher
from myproject.teachers.forms import SignUp,LogIn

teachers_blueprint = Blueprint('teachers', __name__ , template_folder='templates/teachers')

@teachers_blueprint.route('/signup',  methods=['GET', 'POST'])
def signup():
    form = SignUp()
    signupFailed = False

    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        password1 = form.password1.data
        password2 = form.password2.data

        checkTeacherEmail = bool(Teacher.query.filter_by(teacher_email = email).first())
        checkStudentEmail = bool(Student.query.filter_by(student_email= email).first())
        

        # Check if Email is already registered
        if checkStudentEmail or checkTeacherEmail:
            return render_template('tsignup.html',form=form, signupFailed = True)

        if password1 != '' and password1 == password2:
            new_teacher = Teacher(fname,lname,email,password1,0,0)
            db.session.add(new_teacher)
            db.session.commit()

            return redirect(url_for('teachers.login'))
    
    return render_template('tsignup.html',form=form )


@teachers_blueprint.route('/login' , methods =['GET' , 'POST'])
def login():
    form = LogIn()
    loginFailed = False

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

       
        CheckTeacher = Teacher.query.filter_by(teacher_email = email).first()

        if CheckTeacher != None and CheckTeacher.teacher_email == email and CheckTeacher.check_password(password):
            g.teacherLoggedIn = True
            return redirect( url_for('index') )
        else:
            return render_template('tlogin.html' , form=form , loginFailed = True)

    
    return render_template('tlogin.html' , form=form , loginFailed = False)
            
@teachers_blueprint.route('/' )
def signout():
    g.teacherLoggedIn = False
    return redirect( url_for('index') )
