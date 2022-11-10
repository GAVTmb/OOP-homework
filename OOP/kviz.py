class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating_hw = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating_students(self):
        for key, value in self.grades.items():
            self.average_rating_hw[key] = round(sum(value) / len(value), 2)

    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}\n' \
              f' Средняя оценка за домашние задания:' \
              f' {round(sum(self.average_rating_hw.values()) / len(self.average_rating_hw.values()), 1)}\n ' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n ' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнить разные классы!')
            return
        return round(sum(self.average_rating_hw.values()) / len(self.average_rating_hw.values()), 1) \
               < round(sum(other.average_rating_hw.values()) / len(other.average_rating_hw.values()), 1)


class Mentor:  # Родительский класс!!!
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # Дочерний Класс Лекторы!!!
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = {}

    def average_rating_lecturer(self):
        for key, value in self.grades.items():
            self.average_rating[key] = round(sum(value) / len(value), 2)

    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}\n' \
              f' Средняя оценка за лекции:' \
              f' {round(sum(self.average_rating.values()) / len(self.average_rating.values()), 1)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнить разные классы!')
            return
        return round(sum(self.average_rating.values()) / len(self.average_rating.values()), 1) < \
               round(sum(other.average_rating.values()) / len(other.average_rating.values()), 1)


class Reviewer(Mentor):  # Дочерний Класс Проверяющих!!!
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f' Имя: {self.name}\n Фамилия: {self.surname}'
        return res


class United(Lecturer, Reviewer):
    pass


# Студенты!!!
ivan = Student('Ivan', 'Ivanov', 'Man')
ivan.courses_in_progress += ['Python', 'Git']
ivan.finished_courses += ['Вводный модуль', 'Английский для программистов']

balabol = Student('Balabol', 'Zadushevniy', 'Man')
balabol.courses_in_progress += ['Python']
balabol.finished_courses += ['Вводный модуль']

dazdraperma = Student('Dazdraperma', 'Mayskaya', 'woman')
dazdraperma.courses_in_progress += ['Python', 'Git', 'Английский для программистов']
dazdraperma.finished_courses += ['Вводный модуль']

# Преподователи!!!
peter = Lecturer('Peter', 'Petrov')
peter.courses_attached += ['Python']

vasiliy = Lecturer('Vasiliy', 'Pupkin')
vasiliy.courses_attached += ['Git']

knows = United('Knows', 'Everything')
knows.courses_attached += ['Python', 'Git', 'Django', 'Java']

akakiy = Reviewer('Akakiy', 'Zamorskiy')
akakiy.courses_attached += ['Git']

# Выставление оценок Преподавателем "knows" Студенту "dazdraperma" за курс "Python"
knows.rate_student(dazdraperma, 'Python', 10)
knows.rate_student(dazdraperma, 'Python', 7)
knows.rate_student(dazdraperma, 'Python', 9)
# Выставление оценок Преподавателем "knows" Студенту "balabol" за курс "Python"
knows.rate_student(balabol, 'Python', 9)
knows.rate_student(balabol, 'Python', 7)
knows.rate_student(balabol, 'Python', 5)
# Выставление оценок Преподавателем "knows" Студенту "ivan" за курс "Python"
knows.rate_student(ivan, 'Python', 10)
knows.rate_student(ivan, 'Python', 8)
knows.rate_student(ivan, 'Python', 10)
# Выставление оценок Преподавателем "knows" Студенту "dazdraperma" за курс "Git"
knows.rate_student(dazdraperma, 'Git', 8)
# Выставление оценок Преподавателем "knows" Студенту "ivan" за курс "Git"
knows.rate_student(ivan, 'Git', 9)
# Выставление оценок Преподавателем "akakiy" Студенту "dazdraperma" за курс "Git"
akakiy.rate_student(dazdraperma, 'Git', 9)
akakiy.rate_student(dazdraperma, 'Git', 10)
# Выставление оценок Преподавателем "akakiy" Студенту "ivan" за курс "Git"
akakiy.rate_student(ivan, 'Git', 10)
akakiy.rate_student(ivan, 'Git', 10)
# Выставление оценок Преподавателю "knows" Студентом "ivan" за курс "Git"
ivan.rate_lecturer(knows, 'Git', 9)
ivan.rate_lecturer(knows, 'Git', 10)
# Выставление оценок Преподавателю "knows" Студентом "ivan" за курс "Git"
dazdraperma.rate_lecturer(knows, 'Git', 9)
dazdraperma.rate_lecturer(knows, 'Git', 9)
# Выставление оценок Преподавателю "vasiliy" Студентом "ivan" за курс "Git"
ivan.rate_lecturer(vasiliy, 'Git', 8)
# Выставление оценок Преподавателю "vasiliy" Студентом "ivan" за курс "Git"
dazdraperma.rate_lecturer(vasiliy, 'Git', 6)
# Выставление оценок Преподавателю "peter" Студентом "ivan" за курс "Python"
ivan.rate_lecturer(peter, 'Python', 9)
# Выставление оценок Преподавателю "peter" Студентом "balabol" за курс "Python"
balabol.rate_lecturer(peter, 'Python', 8)
# Выставление оценок Преподавателю "peter" Студентом "dazdraperma" за курс "Python"
dazdraperma.rate_lecturer(peter, 'Python', 9)
# Выставление оценок Преподавателю "knows" Студентом "ivan" за курс "Python"
ivan.rate_lecturer(knows, 'Python', 10)
ivan.rate_lecturer(knows, 'Python', 9)
# Выставление оценок Преподавателю "knows" Студентом "balabol" за курс "Python"
balabol.rate_lecturer(knows, 'Python', 7)
balabol.rate_lecturer(knows, 'Python', 7)
# Выставление оценок Преподавателю "knows" Студентом "dazdraperma" за курс "Python"
dazdraperma.rate_lecturer(knows, 'Python', 9)
dazdraperma.rate_lecturer(knows, 'Python', 10)
# Средний бал за ДЗ Студентов!!!
ivan.average_rating_students()
balabol.average_rating_students()
dazdraperma.average_rating_students()
# Средний бал за лекции!
peter.average_rating_lecturer()
vasiliy.average_rating_lecturer()
knows.average_rating_lecturer()
# Списки Студентов и Лекторов!
list_students = [ivan, balabol, dazdraperma]
list_lecturers = [peter, vasiliy, knows]


def av_gr_hw_students(students, courses):
    av_gr = []
    for student in students:
        if courses in student.courses_in_progress:
            for key, values in student.average_rating_hw.items():
                if courses in key:
                    av_gr.append(values)
            return round(sum(av_gr) / len(av_gr), 2)
        else:
            return 'Ошибка'


def av_gr_lecturers(lecturers, courses):
    av_gr = []
    for lecturer in lecturers:
        if courses in lecturer.courses_attached:
            for key, values in lecturer.average_rating.items():
                if courses in key:
                    av_gr.append(values)
            return round(sum(av_gr) / len(av_gr), 2)
        else:
            return 'Ошибка'


# print(av_gr_hw_students(list_students, 'Git'))
# print(av_gr_lecturers(list_lecturers, 'Git'))
# print(ivan.__dict__)
# print(balabol.__dict__)
# print(dazdraperma.__dict__)
# print('----------')
# print(peter.__dict__)
# print(knows.__dict__)
# print(vasiliy.__dict__)
# print(akakiy.__dict__)
# print(ivan)
# print()
# print(dazdraperma)
# print()
# print(balabol)
# print('------------')
# print(knows)
# print()
# print(akakiy)
# print()
# print(peter)
# print()
# print(vasiliy)
