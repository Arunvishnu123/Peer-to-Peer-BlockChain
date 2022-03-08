# This is always a get request type
# request side
class RequestCreation:
    def __init__(self, message):
        self.message = message

    def requestType(self):
        str = "[]"
        rType = str[:1] + "G" + str[1:]
        return rType

    def messageType(self):
        str = "[]"
        mType = str[:1] + "T" + str[1:]
        return mType

    def final(self):
        pass

# request side
class DataExtraction:
    def __init__(self):
        pass

    def finalDataExtraction(self):
        pass

# response side

class ResponseCreation:
    def __init__(self, message):
        self.message = message

    def requestType(self):
        pass

    def messageType(self):
        pass

    def final(self):
        pass

