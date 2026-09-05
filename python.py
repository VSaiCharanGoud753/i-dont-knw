# class bank:
#      def __init__(self,holder_name,balance):
#           print('holder_name=',holder_name)
#           print('balance=',balance)
# obj=bank('sai',5000)  

# class accc:
#     def __init__(self):
#         emp_id=int(input('Enter the emp_id:-'))
#         emp_name=input('Enter the emp_name:-')
#         emp_bal=int(input('Enter the balance:-'))

#         print(emp_id)
#         print(emp_name)
#         print(emp_bal)
# obj=accc()

class bank:
    def __init__(self):
        pass
    def createaccount(self):
        self.holder_name='sai'
        self.account_num=79525262
        self.ifsc='SBI455555'
obj=bank()
obj.createaccount()
obj.dept='sales'
print(obj.__dict__)