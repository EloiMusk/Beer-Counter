from datetime import datetime

class ActivityLogger:
    def __init__(self, filePath):
        self.filePath = filePath

    def write_log(self, prefix, text):
        timestamp = (datetime.now()).strftime('%d/%m/%Y   %H:%M:%S')
        
        self.file = open(self.filePath)
        self.file.write(str(f"{timestamp} {prefix} {text}"))
        self.file.close()

    def log_process(self,text):
        self.write_log(prefix='[PROCESS]      ', text=text)

    def log_info(self,text):
        self.write_log(prefix='[INFORMATION]  ', text=text)

    def log_warning(self,text):
        self.write_log(prefix='[WARNING]      ', text=text)

    def log_error(self,text):
        pass

    def log_success(self,text):
        pass

    def log_failure(self,text):
        pass

    def log_api_request(self,text):
        pass