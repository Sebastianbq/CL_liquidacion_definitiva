import psycopg2
#import SecretConfig

from model.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction, worker

class ControllerWorker:

    def CreateTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControllerWorker.ObtenerCursor()

        cursor.execute("""create table worker (
  id varchar(5) primary key not null,
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

        cursor.execute("""insert into usuarios (id, salary_base,months_worked, vacation_day,
                            hours_extras, extra_hours_nigth, 
                            days_finish) '""" )
        fila = cursor.fetchone()
        resultado = worker( id=fila[0], salaty_base=fila[1], months_worked=fila[2], vacation_day=fila[3],
                            hours_extra=fila[4], hours_estra_nigth=fila[5], days_finish=fila[6] )
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
