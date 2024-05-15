
import sys
sys.path.append("src")
import model.calculateLogic as calculateLogic
from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction, worker
from controller.controller_worker import ControllerWorker

"""
salary_base = salario base
months_worked = meses trabajados
annual_layoffs = cesantias anuales
interest_layoffs = intereses de cesantias
bonus_services = prima de servicios
vacation_days = dias de vacaciones
extra_hours = horas extras
night_charges = cargos nocturnos
compensation_dismissal = indemnizacion por despido
"""

#metodo para consola
def main():
   #aviso de uso del programa
   print("Para usar la calculadora de liquidaciones, porfavor introduzca la informacion necesaria")
   print("Ingrese la accion que dese hacer:")
   
   # Pedir los datos necesarios al usuario
   try:
         #verificar que accion desea hacer el usuario
         action= int(input("1: nuevo empleado \
                           2: seleccionar empleado \
                           3: eliminar empleado\
                           4: modificar empleado \
                           5: liquidacion de empleado"))         
         if action == 1:
            worker= create_worker()
            ControllerWorker.Insertarworker(worker)
         if action == 3:
            ControllerWorker.EliminarTabla()
         if action == 4:
            id= int(input("Ingrese id del empleado: "))
            ControllerWorker.BuscarWorkerId(id)
         if action == 5 or action == 2:
            id= int(input("Ingrese id del empleado: "))
            result= ControllerWorker.BuscarWorkerId(id)
            if action == 2:
               print(result)
               action
            else:
               ()
    #control de excepcciones
   except ValueError:
      print("Error: por favor, introduce valores numéricos válidos.")
      return
    

def create_worker(worker):
   try:
      salary_base = float(input("Salario base: "))
      months_worked = int(input("Meses trabajados: "))         

      #diccionario para almacenar las entradas variadas
      changeable_variables = {}

      #check_vacation: pregunta si se deben dias de vacaciones
      check_vacation= input('se deben dias de vacaciones: digite "si" o "no": ' )
      if check_vacation == "no":
         changeable_variables["vacation"]= 0
      if check_vacation == "si":
         changeable_variables["vacation"]= int(input('cuantos dias de vacaciones: '))
         

      #extra_hours_quest: pregunta si realizo horas extras
      extra_hours_quest= input('realizo horas extras: digite "si" o "no": ' )
      if extra_hours_quest == "no":
         changeable_variables["extra_hours"]= 0
         changeable_variables["extra_hours_nigth"]= 0
      if extra_hours_quest == "si":
         #extra_hours_nigth: horas extras diurnas realizo
         changeable_variables["extra_hours"]= int(input('cuantas horas diurnas realizo: '))        
         #extra_hours_nigth: horas extras nocturnas realizo
         changeable_variables["extra_hours_nigth"]= int(input('cuantas horas nocturnas realizo:' ))

      #days_finish_quest: pregunta si se despidio con justa causa
      days_finish_quest= input('despino con justa causa: digite "si" o "no": ' )
      if days_finish_quest == "si":
         #days_finish: cuantos dias faltan para que termione contrato
         changeable_variables["days_finish"]= 0
      if days_finish_quest == "no":
         changeable_variables["days_finish"]= int(input('cuantos dias faltaron para finalizar contrato: '))        
      
      return calculateLogic.worker(salary_base,months_worked,changeable_variables["vacation"], \
                                 changeable_variables["extra_hours"],changeable_variables["extra_hours_nigth"],changeable_variables["days_finish"])
   
   except ValueError:
      print("Error: por favor, introduce valores numéricos válidos.")
      return
   
def calculate_liquidacion(worker):   
   changeable_variables= []
   changeable_variables["vacation"]= worker.vations_day
   changeable_variables["vacation"]= worker.hours_extra
   changeable_variables["vacation"]= worker.hours_extra_nigth
   changeable_variables["vacation"]= worker.days_finish
   try:
      settlement_calculator = Settlementcalculator(worker.salary_base, worker.months_worked,changeable_variables)
      net_total = settlement_calculator.Calculate_net_total()
      print(f"La cantidad total a pagar es: {net_total}")
   except SalarybaseExcepction as e:
      print(e)
   except Months_workendExcepction as a:
      print(a)

#metodo para inciar 
if __name__ == "__main__":
    main()