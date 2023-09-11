class HeaderRequest:
    def __init__(self, request_item: dict) -> None:
        self.request = request_item
        self.__auth

    def __auth(self):
        self.auth = self.request.get(
            'auth') if 'auth' in self.request else None
        if self.auth:
            self.header = """
    headers: {
        'Authorization':process.env.AUTH
    },
"""

    def set_data(self, data):
        if data:
            self.header += f"""
    data: {str(data)}
"""
        self.header = "{"+self.header+"}"
        print(self.header)

    def result(self):
        return self.header
    
