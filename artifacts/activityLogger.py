from datetime import datetime

class activityLogger:
    def __init__(self):
        self.filePath = str('./../resources/activityLog.log')


    def write_log(self, prefix, text):
        timestamp = (datetime.now()).strftime('%d/%m/%Y   %H:%M:%S')
        
        self.file = open(self.filePath, "a")
        self.file.write(str(f"{timestamp}   {prefix}    {text}"))
        self.file.close()

    def log_process(self,text):
        self.write_log(prefix='[PROCESS]', text=text)

    def log_info(self,text):
        self.write_log(prefix='[INFORMATION]', text=text)

    def log_warning(self,text):
        self.write_log(prefix='[WARNING]', text=text)

    def log_error(self,text):
        self.write_log(prefix='[ERROR]', text=text)
        raise Exception(text)

    def log_success(self,text):
        self.write_log(prefix='[SUCCESS]', text=text)

    def log_failure(self,text):
        self.write_log(prefix='[FAIL]', text=text)

    def log_api_request(self,text):
        self.write_log(prefix='[API-REQUEST]', text=text)

    def log_db_change(self,text):
        self.write_log(prefix='[DB-CHANGE]', text=text)