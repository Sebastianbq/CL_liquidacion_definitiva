import psycopg2
#import SecretConfig

from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction, worker

class ControllerWorker:

    def CreateTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute("""create table worker (
  id int primary key not null,
  salary_base float not null,
  months_worked int not null,
  vacation_day int not null,
  hours_extras int not null,
  extra_hours_nigth int not null,
  days_finish int not null
);""")
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute("""drop table worker""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def EliminarWorker(id):
        """ Borra el trabajador de la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute(f"""
        DELETE FROM worker
        WHERE id= {id};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def modifacarWorker():
        """ modificar trabajador"""
        id= int(input("ingrese el id del trabajador: "))
        modificar= int(input("1. id \n2. salary_base	\n3. months_worked \n4.vacation_day \n5. hours_extras \
                            \n6. extra_hours_nigth \n7. days_finish \ningrese dato a modificar: "))
        valor= input("valor a ingresar: ")
        modificar= option(modificar)
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute(f"""
        UPDATE worker
        SET {modificar} = {valor}
        WHERE id = {id};
        """ )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()

    def Insertarworker( worker : worker ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = ControllerWorker.ObtenerCursor()
        cursor.execute( f"""insert into worker (id, salary_base,months_worked, vacation_day,
                            hours_extras, extra_hours_nigth, 
                            days_finish) 
                        values ('{worker.id}', '{worker.salary_base}', '{worker.months_worked}',  
                            '{worker.vacations_day}', '{worker.hours_extra}',
                            '{worker.hours_extra_nigth}', '{worker.days_finish}')""" )
        cursor.connection.commit()

    def BuscarWorkerId( id ):
        """ Trae un usuario de la tabla de usuarios por la id """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute(f"""select id, salary_base, months_worked, vacation_day, hours_extras, extra_hours_nigth, days_finish
        from worker where id = {id}""" )
        fila = cursor.fetchone()
        print(fila)
        resultado = worker( id=fila[0], salary_base=fila[1], months_worked=fila[2], vacation_days=fila[3],
                            hours_extra=fila[4], hours_extra_nigth=fila[5], days_finish=fila[6] )
        return resultado



    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        PGHOST='ep-fragrant-river-a5e4yp1r.us-east-2.aws.neon.tech'
        PGDATABASE='worker'
        PGUSER='worker_owner'
        PGPASSWORD='nCfmLE09WVsi'
        PGPORT= 5432
        connection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor


def option(modificar):
    if modificar == 1:
        modificar= "id"
    if modificar == 2:
        modificar= "salary_base"
    if modificar == 3:
        modificar= "months_worked"
    if modificar == 4:
        modificar= "vacation_day"
    if modificar == 5:
        modificar= "hours_extras"
    if modificar == 6:
        modificar= "extra_hours_nigth"
    if modificar == 7:
        modificar= "days_finish"
    return modificar