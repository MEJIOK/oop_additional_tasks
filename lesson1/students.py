"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса, 3 [курс]
- Маргарита, 2 [курс]
"""


class Student:

    def __init__(self, name: object = str, course: object = int) -> None:
        self.name = name
        self.course = course


student_1 = Student('Алиса', 3)
student_2 = Student('Маргарита', 2)

# код для проверки
print(student_1.name, student_1.course, 'курс')  # Алиса 3 курс
print(student_2.name, student_2.course, 'курс')  # Маргарита 2 курс
