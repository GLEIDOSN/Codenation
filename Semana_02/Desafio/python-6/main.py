from abc import ABCMeta, abstractmethod

# Constantes
CARGA_HORARIA = 8
PERC_COMISSAO = 0.15


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=ABCMeta):
    def __init__(self, code, name, salary, department):
        self._department = department
        self.code = code
        self.name = name
        self.salary = salary

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return CARGA_HORARIA

    def get_department(self):
        return self._department.name

    def set_departament(self, new_department_name):
        self._departament.name = new_department_name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * PERC_COMISSAO


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * PERC_COMISSAO

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
