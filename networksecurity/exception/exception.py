import sys
from networksecurity.logging.logger import logging
def error_message_detail(error,error_detail:sys):
    #sys.exc_info(): This function gives: Exception type, Exception object, Traceback object
    #From the traceback, we can extract: File name where error occurred, Line number of error
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class NetworkSecurityException(Exception):
    def __init__(self, error,error_message):
        super().__init__(error)
        self.error_message=error_message_detail(error,error_message)
    
    def __str__(self):
        return self.error_message
        
