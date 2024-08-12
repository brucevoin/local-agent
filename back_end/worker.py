import uuid
class Worker:
    def __init__(self):
        self.worker_id = uuid.uuid4()
        self.worker_name = "worker" + str(self.worker_id)
        self.worker_status = "idle"
        
       
    def run(self):
        while True:
            self.worker_status = "idle"
            self.worker_status = "busy"
            self.worker_status = "idle"