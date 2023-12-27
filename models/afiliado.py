from dataclasses import dataclass

from settings.connections import AdabasConnection
from settings.connections import PostgresConnection


@dataclass
class Afiliado:
    nombre: str
    apellido: str
    cuil: int

    def get_nombre_apellido(self):
        return f"{self.nombre} {self.apellido}"

    def get_from_adabas(cuil: int):
        campos = ['DS_APELLIDO_NOMBRE']
        campos_str = ', '.join(campos)
        nombre_tabla = 'AFILIADO'

        sql = f"SELECT {campos_str} "
        sql += f"FROM {nombre_tabla} "
        sql += f"WHERE NU_CUIL = {cuil}"

        with AdabasConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                encabezados = cursor.description
                encabezados = [e[0] for e in encabezados]

        afiliado_dict = dict(zip(encabezados, result))
        nombre_apellido = afiliado_dict['DS_APELLIDO_NOMBRE'].split(' ')

        afiliado = Afiliado(
            apellido=nombre_apellido[0],
            nombre=' '.join(nombre_apellido[1:]),
            cuil=cuil
        )

        return afiliado

    def save_to_postgres(self):
        columns = ['DS_APELLIDO_NOMBRE', 'NU_CUIL']
        sql = f"INSERT INTO AFILIADO2 ({','.join(columns)}) "
        sql += f"VALUES (\'{self.apellido} {self.nombre}\', \'{str(self.cuil)[:1]}\')"

        with PostgresConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
        return self

    def get_from_postgres(cuil):
        campos = ['DS_APELLIDO_NOMBRE']
        campos_str = ', '.join(campos)
        nombre_tabla = 'AFILIADO2'

        sql = f"SELECT {campos_str} "
        sql += f"FROM {nombre_tabla} "
        #sql += f"WHERE NU_CUIL = \'{cuil}\'"

        with PostgresConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                encabezados = cursor.description
                encabezados = [e[0] for e in encabezados]
        if result:
            afiliado_dict = dict(zip(encabezados, result))
            nombre_apellido = afiliado_dict['DS_APELLIDO_NOMBRE'.lower()].split(
                ' ')

            afiliado = Afiliado(
                apellido=nombre_apellido[0],
                nombre=' '.join(nombre_apellido[1:]),
                cuil=cuil,
            )
            return afiliado
        else:
            return None


if __name__ == '__main__':
    afiliado = Afiliado.get(20389553469)
    print(afiliado.get_nombre_apellido())
