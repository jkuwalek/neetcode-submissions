class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def _get_balance(self) -> int:
        return self.balance
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._get_balance()}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
