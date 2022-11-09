# Find all students who have a GPA greater than 3.0.
# Order the data by highest GPAs first (descending).
# Print out each student's full name and gpa to the terminal
def problem_one(request):

 
 student=Student.objects.filter( gpa__gt=3).order_by('-gpa')
 for student in student:
     print(f'{student.first_name} {student.last_name}{student.gpa}')
 

    
    
 return complete(request)

# Find all instructors hired prior to 2010
# Order by hire date ascending
# Print out the instructor's full name and hire date to the terminal
def problem_two(request):

  instructor=Instructor.objects.filter(hire_date__year__lt=2010).order_by('hire_date')
  for instructor in instructor:
   print(f'{instructor.first_name}{instructor.last_name}{instructor.hire_date}')

  return complete(request)

# Find all courses that belong to the instructor that has the primary key of 2
# Print the instructors name and courses that he belongs to in the terminal
# (Do not hard code his name in the print)
def problem_three(request):
 course=Course.objects.get(pk=2)
 print(f'{course.name}{course.instructor}{course.credits}')
 return complete(request)

# Get the count of students, courses, and instructors and print them in the terminal
def problem_four(request):

  students=Student.objects.count()
  print(f'{students}')
  course=Course.objects.count()
  print(f'{course}')
  instructor=Instructor.objects.count()
  print(f'{instructor}')

  return complete(request)

  # Create a new student in the database. Use your information!
# Print the new student's id, full name, year, and gpa to the terminal
# NOTE every time you execute this function a duplicate student will be created with a different primary key number
def problem_five(request):
  student=Student()
  student.first_name='Gwendolyn'
  student.last_name='Flewellen'
  student.year=2022
  student.gpa=3.0
  student.save()

  print(
    f'First Name {student.first_name}, Last Name {student.last_name}, Year {student.year}, GPA {student.gpa}')

  return complete(request)


 Query the previoiusly created student by the id and update the "gpa" to a new value
# Then query the studets table to get that student by their id
# Print the new student's id, full name, and gpa to the terminal
def problem_six(request):

    # Make sure to set this equal to the primary key of the row you just created!
    student_id = 11
    student=Student.objects.filter(pk=student_id).update(gpa=4.0)
    student=Student.objects.get(pk=student_id)
    print(
    f'Student id {student_id}, First Name {student.first_name}, Last Name {student.last_name}, GPA {student.gpa}')


    return complete(request)

# Delete the student that you have created and updated
# Check your MySQL Workbench to confirm the student is no longer in the table!
def problem_seven(request):

    # Make sure to set this equal to the primary key of the row you just created!
    student_id = 11
    student=Student.objects.filter(pk=student_id).delete()
    try:
     student=Student.objects.get(pk=student_id)
    except ObjectDoesNotExist:
     print('Great! It failed and couldnt find the object becasye we deleted it!')

    try:
        student = Student.objects.get(pk=student_id)
    except ObjectDoesNotExist:
        print('Great! It failed and couldnt find the object because we deleted it!')

    return complete(request)

    # Find all of the instructors that only belong to a single course
# Print out the instructors full name and number of courses to the console
def bonus_problem(request):
  student_id=3,8
  course=Course.objects.filter(pk=student_id)
  print(f'{student_id}, {course.name}')

  return complete(request)

