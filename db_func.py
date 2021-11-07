import psycopg2
import psycopg2.extras
from config import DATABASE, USER, HOST, PASSWORD
from typing import Union
import sys

postgresql_host = {'win32': HOST,
                   'linux': 'localhost'}

HOST = postgresql_host.get(sys.platform, HOST)


class DBFunc:

    def db_connect(self, sql, values=None, dict_val=True, all_value=True) -> Union[bool, tuple, list, dict]:
        con = None
        try:
            con = psycopg2.connect(database=DATABASE, user=USER, host=HOST,
                                   password=PASSWORD, port='5432')
            con.autocommit = True
            if dict_val:
                cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            elif not dict_val:
                cur = con.cursor()
            if values:
                cur.execute(sql, values)
            else:
                cur.execute(sql)
            output = cur.fetchall() if all_value else cur.fetchone()
            cur.close()
            return output
        except psycopg2.Error as error:
            # logger.error(f"Помилка в базі: {error}")
            print(f"Помилка в базі: {error}")
            return False
        finally:
            if con is not None:
                con.close()

    def check_user(self, message):
        user_cred = message.from_user
        self.db_connect(f"select * from check_users({user_cred.id}, '{user_cred.username}',"
                        f" '{user_cred.first_name}', '{user_cred.last_name}')")
        return True

    def get_info_by_number_plate(self, number_plate):
        sql = f"select * from find_cars.public.get_operation_lp('{number_plate}')"
        info = self.db_connect(sql)
        info_dict = [dict(val) for val in info] if info else []
        return info_dict

    def get_info_by_vin_id(self, vin_id):
        sql = f"select * from find_cars.public.get_operation_vin({vin_id})"
        info = self.db_connect(sql)
        info_dict = [dict(val) for val in info] if info else []
        return info_dict
