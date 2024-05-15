import unittest
import sys
sys.path.append("src")
from src.model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction
from sql import LiquidationDatabase

class DatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = LiquidationDatabase()

    def testAddEmployee(self):
        """Test para agregar un empleado a la base de datos"""
        # Caso de agregar un empleado con información válida
        employee_data_valid = {
            "id": 1,
            "salary_base": 50000,
            "months_worked": 12,
            "changeable_variables": {"vacation": 15, "extra_hours": 5, "extra_hours_nigth": 2, "days_finish": 30}
        }
        self.assertTrue(self.db.add_employee(employee_data_valid))

        # Caso de intentar agregar un empleado con ID duplicado
        employee_data_duplicate_id = {
            "id": 1,
            "salary_base": 60000,
            "months_worked": 6,
            "changeable_variables": {"vacation": 10, "extra_hours": 3, "extra_hours_nigth": 1, "days_finish": 15}
        }
        self.assertFalse(self.db.add_employee(employee_data_duplicate_id))

    def testDeleteEmployee(self):
        """Test para eliminar un empleado de la base de datos"""
        # Caso de eliminar un empleado existente
        employee_id = 1
        self.assertTrue(self.db.delete_employee(employee_id))

        # Caso de intentar eliminar un empleado que no existe
        non_existing_employee_id = 999
        self.assertFalse(self.db.delete_employee(non_existing_employee_id))

    def testSearchEmployee(self):
        """Test para buscar un empleado en la base de datos"""
        # Caso de buscar un empleado existente por ID
        employee_id = 1
        employee_data = {
            "id": 1,
            "salary_base": 50000,
            "months_worked": 12,
            "changeable_variables": {"vacation": 15, "extra_hours": 5, "extra_hours_nigth": 2, "days_finish": 30}
        }
        self.assertEqual(self.db.search_employee(employee_id), employee_data)

        # Caso de buscar un empleado que no existe
        non_existing_employee_id = 999
        self.assertIsNone(self.db.search_employee(non_existing_employee_id))

    def testAddEmployeeWithZeroSalary(self):
        """Test para agregar un empleado con salario base igual a cero"""
        employee_data_zero_salary = {
            "id": 2,
            "salary_base": 0,
            "months_worked": 6,
            "changeable_variables": {"vacation": 10, "extra_hours": 3, "extra_hours_nigth": 1, "days_finish": 15}
        }
        self.assertFalse(self.db.add_employee(employee_data_zero_salary))

    def testAddEmployeeWithZeroMonthsWorked(self):
        """Test para agregar un empleado con meses trabajados igual a cero"""
        employee_data_zero_months = {
            "id": 3,
            "salary_base": 60000,
            "months_worked": 0,
            "changeable_variables": {"vacation": 10, "extra_hours": 3, "extra_hours_nigth": 1, "days_finish": 15}
        }
        self.assertFalse(self.db.add_employee(employee_data_zero_months))

    def testDeleteNonExistingEmployee(self):
        """Test para intentar eliminar un empleado que no existe en la base de datos"""
        non_existing_employee_id = 999
        self.assertFalse(self.db.delete_employee(non_existing_employee_id))

    def testSearchNonExistingEmployee(self):
        """Test para buscar un empleado que no existe en la base de datos"""
        non_existing_employee_id = 999
        self.assertIsNone(self.db.search_employee(non_existing_employee_id))

if __name__ == '__main__':
    unittest.main()