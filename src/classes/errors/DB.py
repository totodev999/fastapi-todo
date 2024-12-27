class DBCommonException(Exception):
    def __init__(self):
        super().__init__("DB Error")
