class DbConnection:
    def connection(self):
        # Database connection details
        db_server = 'RK-0595-SAIKAT'
        db_name = 'TRYNEW'
        db_user = 'sa'
        db_password = '123456'

        conn_str = f"DRIVER={{SQL Server}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_password}"

        return conn_str
