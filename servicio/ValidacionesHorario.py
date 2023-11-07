from fastapi import HTTPException
from datetime import datetime, timedelta, time
from modelo.ModeloHorario import Horario 
from pydantic import validator



class HorarioValidations(Horario):

    @validator('dia_semana',pre=True, always=True)
    def validate_dia_semana(cls, dia_semana):
        dias_permitidos = ["lunes", "martes", "miercoles", "jueves", "viernes"]
        if dia_semana not in dias_permitidos:
            raise ValueError("El día de la semana no es válido")
        return dia_semana

    @validator('hora_inicio', pre=True, always=True)
    def validate_hora_inicio(cls, hora_inicio):
        try:
            datetime.strptime(hora_inicio, '%H:%M')
        except ValueError:
            raise ValueError("La hora de inicio no tiene el formato HH:MM válido")
        return hora_inicio
    
    @validator('hora_pico', pre=True, always=True, check_fields=False)
    def validate_hora_pico(cls, tipo_horario, values):
        if 'hora_inicio' in values and 'hora_fin' in values and 'tipo_horario' in values:
            hora_inicio = datetime.strptime(values['hora_inicio'], '%H:%M')
            hora_fin = datetime.strptime(values['hora_fin'], '%H:%M')
            hora_pico_inicio = datetime.strptime('05:00', '%H:%M')
            hora_pico_fin = datetime.strptime('09:00', '%H:%M')
            tarde_pico_inicio = datetime.strptime('16:00', '%H:%M')
            tarde_pico_fin = datetime.strptime('20:00', '%H:%M')

            if (
                (hora_pico_inicio <= hora_inicio <= hora_pico_fin or tarde_pico_inicio <= hora_inicio <= tarde_pico_fin)
                and (hora_pico_inicio <= hora_fin <= hora_pico_fin or tarde_pico_inicio <= hora_fin <= tarde_pico_fin)
            ):
                if values['tipo_horario'].lower() == 'si':
                    if tipo_horario.lower() == 'si':
                        return tipo_horario
                    else:
                        raise ValueError("La hora_pico debería ser 'si' para las horas pico")
                elif values['tipo_horario'].lower() == 'no':
                    if tipo_horario.lower() == 'no':
                        return tipo_horario
                    else:
                        raise ValueError("La hora_pico debería ser 'no' fuera de las horas pico")
            else:
                raise ValueError("Las horas de inicio y fin no están dentro del rango de horas pico")
        return tipo_horario



    
    '''
    @validator('hora_pico', pre=True, always=True, check_fields=False)
    def validate_hora_pico(cls, hora_pico, values):    
        if 'hora_inicio' in values and 'hora_fin' in values and 'tipo_horario' in values:
            hora_inicio = datetime.strptime(values['hora_inicio'], '%H:%M')
            hora_fin = datetime.strptime(values['hora_fin'], '%H:%M')
            hora_pico_inicio = datetime.strptime('05:00', '%H:%M')
            hora_pico_fin = datetime.strptime('09:00', '%H:%M')
            tarde_pico_inicio = datetime.strptime('16:00', '%H:%M')
            tarde_pico_fin = datetime.strptime('20:00', '%H:%M')

        if hora_inicio >= hora_pico_inicio and hora_fin >= hora_pico_fin or hora_inicio >=tarde_pico_inicio and hora_fin <= tarde_pico_fin:

            if values['tipo_horario'].lower() == 'si':
                return hora_pico
            else:
                raise ValueError("La hora_pico debería ser 'si' para las horas pico")

        elif hora_inicio < hora_pico_inicio and hora_fin < hora_pico_fin or hora_inicio < tarde_pico_inicio and hora_fin < tarde_pico_fin:
            
            if values['tipo_horario'].lower() == 'no':
                return hora_pico
            else:
                raise ValueError("La hora_pico debería ser 'no' fuera de las horas pico")
            
        

        
        if 'hora_inicio' in values:
            hora_pico = values['tipo_horario']
            hora_inicio = datetime.strptime(values['hora_inicio'], '%H:%M')
            hora_fin = datetime.strptime(values['hora_fin'], '%H:%M')
            hora_pico_inicio = datetime.strptime('05:00', '%H:%M')
            hora_pico_fin = datetime.strptime('09:00', '%H:%M')
            tarde_pico_inicio = datetime.strptime('16:00', '%H:%M')
            tarde_pico_fin = datetime.strptime('20:00', '%H:%M')

            if hora_inicio >= hora_pico_inicio and hora_fin >= hora_pico_fin or hora_inicio >=tarde_pico_inicio and hora_fin <= tarde_pico_fin:

                if hora_pico == 'si':
                    print
                    return values
                else:
                    raise ValueError("La hora_pico debería ser 'si' para las horas pico")
            
            elif hora_inicio < hora_pico_inicio and hora_fin < hora_pico_fin or hora_inicio < tarde_pico_inicio and hora_fin < tarde_pico_fin:
                
                if hora_pico == 'no':
                    return values
                else:
                    raise ValueError("La hora_pico debería ser 'No' fuera de las horas pico")

'''

