class DbConnection:
    def connection(self):
        # Database connection details
        db_server = 'RK-0595-SAIKAT'
        db_name = 'NEW'
        db_user = 'sa'
        db_password = '123456'

        conn_str = f"mssql+pyodbc://{db_user}:{db_password}@{db_server}/{db_name}?driver=SQL+Server"

        return conn_str
