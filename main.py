class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        av_list = []
        for grade in self.grades.values():
            av_list += grade
        average = sum(av_list) / len(av_list)
        return average

    def __str__(self):
        c_i_p = ", ".join(self.courses_in_progress)
        f_c = ", ".join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}\nКурсы в процессе изучения: {c_i_p}\nЗавершенные курсы: {f_c}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        av_list = []
        for grade in self.grades.values():
            av_list += grade
        average = sum(av_list) / len(av_list)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average() < other.average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lecturer_1 = Lecturer('Хрен', 'Моржов')
lecturer_1.courses_attached = ['Python', 'Javascript', 'C++']

lecturer_2 = Lecturer('Альберт', 'Эйнштейн')
lecturer_2.courses_attached = ['PHP', 'Java', 'Swift', 'Git']

student_1 = Student('Ян', 'Железный', 'муж')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Java', 'C++']
student_1.rate_l(lecturer_1, 'Python', 9)
student_1.rate_l(lecturer_2, 'Git', 8)

student_2 = Student('Люба', 'Кочерга', 'жен')
student_2.courses_in_progress += ['Python', 'Javascript', 'Swift']
student_2.finished_courses += ['PHP']
student_2.rate_l(lecturer_1, 'Python', 8)
student_2.rate_l(lecturer_2, 'Swift', 6)

reviewer_1 = Reviewer('Иван', 'Петров')
reviewer_1.courses_attached = ['Python', 'Javascript', 'C++']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Javascript', 9)

reviewer_2 = Reviewer('Джон', 'Сидоров')
reviewer_2.courses_attached = ['PHP', 'Java', 'Swift', 'Git']
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Swift', 7)

stu_list = [student_1, student_2]
lec_list = [lecturer_1, lecturer_2]

# print(student_1.grades)
# print(student_2.grades)
# print(lecturer_1.grades)
# print(lecturer_2.grades)
def average_hw_course(student_list, course):
    av_hw_course = []
    for student in student_list:
        if course in student.grades:
            av_hw_course += student.grades[course]
    average_hw_course = sum(av_hw_course) / len(av_hw_course)
    return average_hw_course


def average_l_course(lecturer_list, course):
    av_l_course = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            av_l_course += lecturer.grades[course]
    average_l_course = sum(av_l_course) / len(av_l_course)
    return average_l_course


print(reviewer_1)
print(lecturer_1)
print(student_1)
print(reviewer_2)
print(lecturer_2)
print(student_2)
print(lecturer_1 < lecturer_2)

print(average_hw_course(stu_list, 'Python'))
print(average_l_course(lec_list, 'Git'))