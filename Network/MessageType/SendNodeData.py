# This is always a post request type
# sender side
class RequestCreation:
    def __init__(self, message):
        self.message = message

    def requestType(self):
        pass

    def messageType(self):
        pass

    def data(self):
        pass

    def final(self):
        pass


# receiver side
class DataExtraction:
    def __init__(self):
        pass

    def finalDataExtraction(self):
        pass
