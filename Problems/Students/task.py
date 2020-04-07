class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + self.birth_year


nome = input()
sobrenome = input()
ano = input()

student = Student(nome, sobrenome, ano)

print(student.id)
