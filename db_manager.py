import psycopg2


class DatabaseManager:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'rabin'
        self.password = 'g0tm3g00d'
        self.database = 'medical'
        self.patient_table = 'patient'
        self.user_table = 'app_user'

        # creates db if it doesn't exist.
        try:
            self.create_database()
        except:
            pass

        self.connect_to_database()

    def check_login(self, username, password):
        self.cur.execute(f'''
            SELECT username FROM app_user WHERE username = '{username}' AND password = '{password}';
        ''')

        return self.cur.fetchone()

    def create_database(self):
        con = psycopg2.connect(
            database='postgres',
            user='postgres',
            host='localhost',
            password='8characterspassword'
        )
        con.autocommit = True  # lets `CREATE DATABASE` run inside transaction block

        cur = con.cursor()
        cur.execute(f"CREATE DATABASE {self.database};")
        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {self.database} TO {self.user};")

    def connect_to_database(self):
        self.con = psycopg2.connect(
            database=self.database,
            user=self.user,
            host=self.host,
            password=self.password
        )

        self.cur = self.con.cursor()

    def create_patient_table(self):
        self.cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.patient_table} (
                id SERIAL PRIMARY KEY NOT NULL,
                full_name TEXT,
                age INT,
                address TEXT,
                thumbnail TEXT,
                other_files TEXT,
                mri_image TEXT
            );
        ''')

    def create_patient(self, **kwargs):
        self.cur.execute(f'''
            INSERT INTO {self.patient_table}(full_name, age, address, thumbnail, other_files, mri_image)
            VALUES('{kwargs.get("full_name", "")}',
            '{kwargs.get("age", 0)}',
            '{kwargs.get("address", "")}',
            '{kwargs.get("thumbnail", "")}',
            '{kwargs.get("other_files", "")}',
            '{kwargs.get("mri_image", "")}') RETURNING id;
        ''')

        return self.cur.fetchone()[0]

    def get_all_patients(self):
        self.cur.execute("SELECT * FROM patient")

        return self.cur.fetchall()

    def get_specific_patient(self, id):
        self.cur.execute(f"SELECT * FROM patient WHERE id = {id}")

        return self.cur.fetchone()

    def update_patient(self, **kwargs):
        self.cur.execute(f'''
            UPDATE patient
            SET
            full_name = '{kwargs.get("full_name", "")}',
            age = '{kwargs.get("age", 0)}',
            address = '{kwargs.get("address", "")}',
            thumbnail = '{kwargs.get("thumbnail", "")}',
            other_files = '{kwargs.get("other_files", "")}',
            mri_image = '{kwargs.get("mri_image", "")}'
            WHERE id = {kwargs.get("id")};
        ''')

    def delete_patient(self, id):
        self.cur.execute(f'''
            DELETE FROM patient where id = {id}
        ''')

    def create_app_user_table(self):
        self.cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.user_table} (
                id SERIAL PRIMARY KEY NOT NULL,
                username TEXT,
                password TEXT
            );
        ''')

    def create_app_user(self, **kwargs):
        self.cur.execute(f'''
            INSERT INTO {self.user_table}(username, password)
            VALUES('admin', 'admin');
        ''')

    def update_app_user(self, **kwargs):
        self.cur.execute(f'''
            UPDATE user
            SET
            username = '{kwargs.get('username')}',
            password = '{kwargs.get('password')}'
            WHERE id = '{kwargs.get('id')};'
        ''')

    def delete_app_user(self, id):
        self.cur.execute(f'''
            DELETE FROM user where id = {id};
        ''')

    def __del__(self):
        self.con.commit()
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    in_database = DatabaseManager()
    in_database.create_patient_table()
    in_database.create_app_user_table()

    in_database.create_app_user(username='admin', password='admin')
    # in_database.create_patient(full_name='Luffy don', age=35, address='ktm', thumbnail='thumb', other_files='nth', mri_image='nth again')
    # in_database.update_patient(full_name='Rabin dada', age=35, address='ktm', thumbnail='thumb', other_files='nth', mri_image='nth again')
    # d = in_database.get_all_patients()
