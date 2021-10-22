class InsufficientFunds(Exception):
    def __init__(self, fund, message="The available balance is insufficient."):
        self.fund = fund
        self.message = message
        super().__init__(self.message)
