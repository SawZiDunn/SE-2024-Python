from abc import ABC, abstractmethod

class PhoneService(ABC):
    def __init__(self, phone_no, customer_name, mm_yyyy):
        self.phone_no = phone_no
        self.customer_name = customer_name
        self.mm_yyyy = mm_yyyy

    @abstractmethod
    def find_cost(self):
        pass
        
class Post_paid(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.call_duration = call_duration
        self.monthly_allowance = 1000 # minutes
        self.fixed_cost = 800 # Baht

    def find_cost(self):
        if self.call_duration <= self.monthly_allowance:
            return self.fixed_cost
        else:
            return self.fixed_cost + self.call_duration - self.monthly_allowance

class Pre_paid(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.call_duration = call_duration

    def find_cost(self):
         return self.call_duration * 2
        

class Fixed_paid(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, local_calls):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.local_calls = local_calls

    def find_cost(self):
        # 3 Bahts per local call 
        return self.local_calls * 3 

def main():
    post_paid = Post_paid("081-000-0007", "John English", "09-2021", 1250)
    pre_paid = Pre_paid("080-000-0007", "John English", "09-2021", 100)
    fixed_line = Fixed_paid("02-000-0007", "John English", "09-2021", 200)

    print(f"Post-paid service fee: {post_paid.find_cost()} Baht")
    print(f"Pre-paid service fee: {pre_paid.find_cost()} Baht")
    print(f"Fixed-line service fee: {fixed_line.find_cost()} Baht")

main()