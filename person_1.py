from load_balancer.load_balancing import * 

class person_1:
    def __init__(self):
        self.p_id = 1  #consider this as an request_id
        self.request_form()

    def request_form(self):
        a = 'abc'  #data which want to store in server or anything
        load_balance(self.p_id,a)
        

person_1()

        