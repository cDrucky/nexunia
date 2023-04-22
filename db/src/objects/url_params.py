class UrlParams:
    def __init__(self):
        self.location = ""
        self.lifecycle = ""
        self.services = ""

    def __str__(self):
        return f"Location {self.location}, Lifecycle: {self.lifecycle}, Services: {self.services}"