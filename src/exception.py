import sys
import logging 

def error_messagres(error, error_detail:sys):
    _,_,err_tb = error_detail.exc_info()
    file_name=err_tb.tb_frame.f_code.co_filename
    error_message = "hsgjdgsjgfj [{0}] jsdhfksjdhf [{1}] jkfhsdh [{2}]".format(
        file_name, err_tb.tb_lineno,str(error) 
    )

    return error_message

class customExeption(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_messagres(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message


        