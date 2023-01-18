class ApiException(Exception):
    def __init__(self, message):
        super(message)


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
