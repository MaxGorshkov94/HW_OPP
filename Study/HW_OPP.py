class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output

    # Метод выставления оценоки лекторам у класса Student. - Задание 2.
    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:

            specific_lecturer.grades.append(grade)

        else:
            return 'Ошибка'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None


# Класс Mentor статл родительским классом. От него реализовано наследование классов Lecturer и Reviewer. - Задание 1.
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return output

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return None


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    # Выставлять студентам оценки за домашние задания теперь может только класс Reviewer. - Заданеи 2.
    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student, Student) \
                and course in self.courses_attached \
                and course in specific_student.courses_in_progress:

            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                specific_student.grades[course] = [grade]
        else:
            return 'Ошибка!'


def average_grade(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_grade(amount_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average
    else:
        return "Ошибка!"


def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)


def average_lecturers_grade(all_lecturers):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            all_lecturers_grades.append(every_grade)
    return average_grade(all_lecturers_grades)


student_no_1 = Student('Иван', 'Остеров', '35')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['Science ']
student_no_1.finished_courses += ['Git']
student_no_1.add_courses('Math')
student_no_1.grades['Git'] = [5, 5, 9]
student_no_1.grades['Python'] = [6, 9, 8, 7, 10, 9]
student_no_1.grades['Science'] = [8, 7]

student_no_2 = Student('Костя', 'Пенягин', '40')
student_no_2.courses_in_progress += ['Python']
student_no_2.finished_courses += ['Git']
student_no_2.grades['Git'] = [8, 8, 8]
student_no_2.grades['Python'] = [8, 9]

student_list = [student_no_1, student_no_2]

lecturer_1 = Lecturer('Игорь', 'Нелин')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Science']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Константин', 'Щварц')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Science']
lecturer_2.courses_attached += ['Git']

lecturer_list = [lecturer_1, lecturer_2]

cool_reviewer = Reviewer('Антон', 'Обухов')
cool_reviewer.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Михаил', 'Белый')
cool_reviewer_2.courses_attached += ['Git']

print('Разновидности добавления оценок: ', "\n")

cool_reviewer.rate_hw(student_no_1, 'Python', 5)
cool_reviewer.rate_hw(student_no_1, 'Python', 7)
cool_reviewer.rate_hw(student_no_1, 'Science', 8)
print(f'Эксперт ставит оценки Студену {student_no_1.grades}')

student_no_1.rate_lecturer(lecturer_1, 'Python', 5)
student_no_1.rate_lecturer(lecturer_1, 'Python', 5)
student_no_1.rate_lecturer(lecturer_1, 'Science', 3)
print(f'Студент_1 ставит оценки Лектору: {lecturer_1.grades}')

student_no_2.rate_lecturer(lecturer_1, 'Python', 6)
student_no_2.rate_lecturer(lecturer_2, 'Python', 9)
print(f'Студент_2 ставит оценки Лектору после студента_1: {lecturer_1.grades}')
print()

print('Вывод информации у всех классов: ', "\n")
print(lecturer_2, "\n")
print(cool_reviewer, "\n")
print(student_no_1, "\n")
print(student_no_2, "\n")

# Задание 4.
print(
    'Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса): ')
print(average_course_grade(student_list, 'Git'))

print('Подсчета средней оценки лекторов по всем курсам: ')
print(average_lecturers_grade(lecturer_list))

