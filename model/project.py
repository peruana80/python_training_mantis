
class Project:
    def __init__(self, name=None, status=None, viewstate=None, description=None):
        self.name = name
        self.status = status
        self.viewstate = viewstate
        self.description = description


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.status, self.viewstate, self.description)

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.viewstate==other.viewstate and self.description == other.description