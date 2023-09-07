class Student:
    """A class that represents a student."""

    def __init__(self, name, age, gender):
        self.full_name = name # public
        self.__age = age # private
        self._gender = gender # restricted

    def get_age(self):
        """Method to get the age of the student."""
        return self.__age

student_1 = Student('Tom', 18, 'M')
# print(student_1.__age)
print(student_1._gender)
