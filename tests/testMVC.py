import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import worker
from controller.controller_worker import ControllerWorker

class TestWorkerController(unittest.TestCase):
    
    def test_create_table_success(self):
        # Mock se usa para simular conexion y cursor
        controller_mock = MagicMock()
        controller_mock.ObtenerCursor.return_value.execute.return_value = None
        
        ControllerWorker.CreateTabla()
        
        controller_mock.ObtenerCursor.return_value.execute.assert_called_with("""create table worker (
id varchar(5) primary key not null,
salary_base int not null,
months_worked int not null,
vacation int not null,
hours_extras int not null,
extra_hours_nigth int not null,
days_finish int not null
);""")
        
    def test_create_table_already_exists(self):
        # Mock de ControllerWorker para simular la conexión y el cursor
        controller_mock = MagicMock()
        # Simulando que la tabla ya existe en la base de datos
        controller_mock.ObtenerCursor.return_value.execute.side_effect = Exception("Table already exists")
        
        # Llamar a la función CreateTabla()
        with self.assertRaises(Exception) as context:
            ControllerWorker.CreateTabla()
        
        # Verificar que se lance una excepción con el mensaje adecuado
        self.assertEqual(str(context.exception), "Table already exists")
        
    def test_delete_table_success(self):
        # Mock de ControllerWorker para simular la conexión y el cursor
        controller_mock = MagicMock()
        controller_mock.ObtenerCursor.return_value.execute.return_value = None
        
        # Llamar a la función EliminarTabla()
        ControllerWorker.EliminarTabla()
        
        # Verificar que la función execute haya sido llamada con el comando SQL correcto
        controller_mock.ObtenerCursor.return_value.execute.assert_called_with("""drop table worker""")
        
    def test_delete_table_not_exists(self):
        # Mock de ControllerWorker para simular la conexión y el cursor
        controller_mock = MagicMock()
        # Simulando que la tabla no existe en la base de datos
        controller_mock.ObtenerCursor.return_value.execute.side_effect = Exception("Table does not exist")
        
        # Llamar a la función EliminarTabla()
        with self.assertRaises(Exception) as context:
            ControllerWorker.EliminarTabla()
        
        # Verificar que se lance una excepción con el mensaje adecuado
        self.assertEqual(str(context.exception), "Table does not exist")

if __name__ == "__main__":
    unittest.main()
