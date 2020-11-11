class ATM(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, deposit, message="withdrawal is not in (5000, 15000) range"):
        self.deposit = deposit
        self.message = message
        super().__init__(self.message)


deposit = int(input("Enter withdrawal amount: "))
if not 5000 < deposit < 15000:
    raise ATM(deposit)
