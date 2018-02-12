#mysql requires python-microsoft visual c++ compiler
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python

import MySQLdb
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class cl_mySQL_DB():
    
    
    # AWS connections
    #C_HOST_NAME = "rajawsdb.cfrxcsxi3tua.us-east-1.rds.amazonaws.com"
    #C_USER_NAME = "root"
    #C_USER_PASSWORD = "sagar123"
    #C_DB_NAME = "CRT"


    C_HOST_NAME = "localhost"
    C_USER_NAME = "root"
    C_USER_PASSWORD = ""
    C_DB_NAME = "CRT"    
    
    
    def __init__(self):
        
        self.con_db = MySQLdb.connect(cl_mySQL_DB.C_HOST_NAME,    
                                 cl_mySQL_DB.C_USER_NAME,         
                                 cl_mySQL_DB.C_USER_PASSWORD, 
                                 cl_mySQL_DB.C_DB_NAME)    
                    
        if self.con_db:
            logging.debug('Successfully connected to : %s'  %cl_mySQL_DB.C_DB_NAME )
        else:
            logging.debug('Error in connecting to : %s'  %cl_mySQL_DB.C_DB_NAME )
            

    
    def closeConnection(self):
        self.con_db.close()
        
    
    def getTableData(self, in_table, in_list_field,in_where_condition):
            
        # you must create a Cursor object. It will let you execute all the queries you need
        cur_db = self.con_db.cursor()
        sql_stmt = "Select %s from %s where "  %in_list_field %in_table %in_where_condition

        cur_db.execute(sql_stmt)
        dict_data = {}

        # print all the first cell of all the rows
        counter = 0
        for row in cur_db.fetchall():
            print row
            dict_data[counter] = row
            counter += 1
            
        return dict_data
    
    def getTicker(self,in_ticker,in_field,in_source):

        cur_db = self.con_db.cursor()
        sql_stmt = "call sp_get_ticker('" + in_ticker + "','" + in_field + "','" + in_source + "');"
        cur_db.execute(sql_stmt)
        
        dict_data = {}
        
        for row in cur_db.fetchall():
            dict_data[row[0]] = row[1]
            
        return dict_data
                
    
    def updTicker(self,in_ticker,in_field,in_source,in_date,in_value):
        
        cur_db = self.con_db.cursor()
        sql_stmt = "call sp_upd_ticker('" + in_ticker + "','" + in_field + "','" + in_source   
        sql_stmt = sql_stmt + "','" + in_date + "'," + in_value + ");"
        
        cur_db.execute(sql_stmt)



