class CustomException(Exception):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
