import json
class jsonio(object):
    """description of class"""
    def __init__(self):
        self.readingfilepath = ""
        self.writingfilepath = ""

    # return a Python dictionary:
    def LoadFromFile(self):
        with open(self.readingfilepath, 'r') as infile:
            data = json.load(infile)
            return data

    def WriteToFile(self, object):
        try:
            with open(self.writingfilepath, 'w') as outfile:
                json.dump(object, outfile)
            return True
        except:
            return False