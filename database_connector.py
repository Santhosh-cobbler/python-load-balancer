from servers import server_1,server_2

class send_data_to_servers:
    def __init__(self,server_id,data):
        self.data = data
        if server_id == 0:
            self.send_to_server_1()

        elif server_id == 1:
            self.send_to_server_2()

        else:
            print('there is no server to process')

    
    def send_to_server_1(self):
        server_1.SERVER_1(self.data)

    def send_to_server_2(self):
        server_2.SERVER_2(self.data)


