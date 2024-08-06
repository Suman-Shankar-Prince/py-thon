
def import_package():
    try:
        from sqlalchemy import create_engine
        try:
            import pyodbc
        except:
            print(f'Checking relational database connection...')
            try:
                import pymysql
            except:
                print('Checking...')
                pass
            pass
        pass
    except:
        import sqlite3
        pass
    finally:
        try:
            import pymongo
        except Exception as e:
            print(f'non relational database connection not available - {e}')
            pass
        finally:
            print('relational database connection can be established')
            pass
        pass
    #==========================================================================
    try:
        import boto3
        print('s3 connector found')
    except:
        try:
            from redshift_connector import redshift_connector
            print('redshift connector found')
            try:
                import psycopg2
            except:
                print('postgre not available')
        except:
            print('redshift not available')
            pass
        print('s3 service not available')
        pass
    #==========================================================================
    import time
    import os
pass
    

class A:
    
    def __init__(self,):
        self.string = str()
        self.position = int()
        self.numerator = map()
        self.denominator = tuple()
        pass
    
    pass

class B(A):
    def __init__(self,):
        self.equation = list() # y=mx+c
        self.size = set()
        pass
    pass



if __name__ == "__main__":
    import_package()
    print('hii there')
    
    pass      