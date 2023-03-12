class Error:
    
    @staticmethod
    def error__500():
        print('Internal Server Error')
    
    @staticmethod
    def error_400():
        print('Not Found')

Error.error__500()
Error.error__400()