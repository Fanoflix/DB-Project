from flask import Blueprint,render_template,redirect,url_for,flash,session
from myproject import db,g
from myproject.models import Student, Teacher
from myproject.assignments.forms import SolveAssignment
from wtforms import RadioField,SubmitField, StringField, Form, validators
from myproject.assignments.forms import AddAssignment

assignments_blueprint = Blueprint('assignments', __name__ , template_folder='templates/assignments')


@assignments_blueprint.route('/home_assignment',  methods=['GET', 'POST'])
def home_assignment():
    return render_template('home_assignment.html', teacherLoggedIn = g.teacherLoggedIn, studentLoggedIn = g.studentLoggedIn)


@assignments_blueprint.route('/description',  methods=['GET', 'POST'])
def description():
    return render_template('description.html' , teacherLoggedIn = g.teacherLoggedIn)

@assignments_blueprint.route('/add_assignment',  methods=['GET', 'POST'])
def add_assignment():
    all_questions = [] 
    questions = []
    index = []
    assignment_questions = 1
    for x in range (10):
        field = StringField([ validators.Required() ])
        setattr(AddAssignment, 'Question' + str(assignment_questions), field)
        questions.append('Question' + str(assignment_questions))
        choice = 1
        for y in range (4):
            setattr(AddAssignment, 'Choice' + str(choice), field)
            questions.append('Choice' + str(choice))
            choice += 1
        setattr(AddAssignment, 'Answer' + str(assignment_questions), field)
        questions.append('Answer' + str(assignment_questions))
        index.append(str(assignment_questions))
        assignment_questions += 1
        all_questions.append(questions)
        questions = []
    setattr(AddAssignment, 'submit', SubmitField('Add Assignment') )


    form = AddAssignment()

    # while not form.validate_on_submit():
    #     if (user plus dabaye):

    if form.validate_on_submit():
        assignment_questions = 1
        assignment_name = form.assignment_name.data
        difficulty = form.difficulty.data
        # print(form.course.data)
        course_id = form.course.data
        print(g.whichTeacher)
        
    return render_template('add_assignment.html', all_questions = all_questions, index = index, form = form, teacherLoggedIn = g.teacherLoggedIn)





@assignments_blueprint.route('/delete_assignment',  methods=['GET', 'POST'])
def delete_assignment():
    return render_template('delete_assignment.html' , teacherLoggedIn = g.teacherLoggedIn)

@assignments_blueprint.route('/solve_assignment',  methods=['GET', 'POST'])
def solve_assignment():

    # assignment = TableName1.query.filter_by(assignment_name = 'some name').first():
    # id = assignment.TableName.assignment_id
    # a sample 
    records = [ 
                ['1','1','How do you do when you cant do?','you do', 'you dont' ,'you cant' , 'you suck' ,'2'] ,
                ['1','2','What is your name?','I', 'you' ,'no' , 'yes' ,'4'] ,
                ['1','3','Is Abdullah a bot? Wrong answers only','yes', 'yes' ,'yes' , 'yes' ,'1'] ,
                ['1','4','You done fucked up','yes', 'no' ,'I am' , 'hahaha' ,'3'] ,
                ['1','5','How is testing going?','perfect', 'good' ,'not bad' , 'fucked' ,'4'] 
                ]
        


    questions = []
    # for record in TableName.query.filter_by(assignment_id = id).all():
    for record in records:  
            questions.append(record[2])
  

    #-----------Making a form------------------
    count = 1
    field_list = []

    # for record in TableName.query.filter_by(assignment_id = id).all():
    for record in records:
        field = RadioField(choices=[('1' , record[3]) , ('2' , record[4]), ('3' , record[5]), ('4' , record[6]) ])
        setattr(SolveAssignment, 'choice' + str(count), field) 
        # i.e: choice1 = RadioField(choices=[('1' , record[3]) , ('2' , record[4]), ('3' , record[5]), ('4' , record[6]) ])
        field_list.append('choice'+str(count))
        count = count + 1

    setattr(SolveAssignment, 'submit', SubmitField("Submit"))
    #----------------------------------------------
    form = SolveAssignment()   

    if form.validate_on_submit():
        count = -1
        for record in records:
            count = count + 1
            if getattr(form,field_list[count]).data == record[7]:
                # points++
                print(getattr(form,field_list[count]).data)
            
            getattr(form,field_list[count]).data = ''
        
        return redirect(url_for('assignments.after_submit'))

    return render_template('solve_assignment.html' , form = form, teacherLoggedIn = g.teacherLoggedIn, questions = questions , field_list = field_list)

    
        
@assignments_blueprint.route('/after_submit',  methods=['GET', 'POST'])
def after_submit():
    return render_template('after_submit.html' , teacherLoggedIn = g.teacherLoggedIn)  
    


