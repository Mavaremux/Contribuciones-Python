class Employee:
    def __init__(self, id: int , name: str):
        self.id = id
        self.name = name
        self.employees = []
    def add(self, employee: Employee):
        self.employees.append(employee)

    def printemployees(self):
        for employee in self.employees:
            print(employee.name)
class Manager(Employee):
    def cordinateprojects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa")


class Programmer(Employee):
    def __init__(self, id: int , name: str, language: str):
        super().__init__(id,name )
        self.language = language
    def code(self):
        print(f"{self.name} esta programando su proyecto en {self.language}")
    def add(self, employee):
        print(f"Programmer no tiene empleados a su cargo {employee.name} no se añadira")

class ProjectManager(Employee):
    def __init__(self, id: int , name: str, projects: str):
        super().__init__(id,name )
        self.projects = projects
        
    def coordinate_project(self):
        print(f"{self.name} esta coordinando su proyecto")

    
    
my_manager = Manager(1 , "Alejandro" )
my_project_manager = ProjectManager(2, "Mavares" , "Pagina web")
my_project_manager2 = ProjectManager(3, "Mavarito" , "Pagina web 2")
my_programmer = Programmer(4, "Enrique" ,"Python")
my_programmer1 = Programmer(10, "Alfonso" ,"Fortran")
my_programmer2 = Programmer(12, "Alfonsito" ,"C")


my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)
my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)

my_project_manager2.add(my_programmer2)

my_programmer.add(my_programmer2)

my_programmer2.code()
my_project_manager.coordinate_project()
my_manager.cordinateprojects()



my_manager.printemployees()
my_project_manager.printemployees()

print("hola cabron")