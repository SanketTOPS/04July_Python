import random

class bank:
    ano=random.randint(11111,99999)
    def __init__(self) -> None:
        print("Your Account Number:",self.ano)


b=bank()
