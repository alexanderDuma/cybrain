class User:
    def __init__(self,username,role):
        self.username = username
        self.role = role

class Adversary:
    def __init__(self,origin,organization,campaign):
        self.origin = origin
        self.organization = organization
        self.campaign = campaign

class Target:
    def __init__(self,sector,name,is_israeli:bool):
        self.sector = sector
        self.name = name
        self.is_israeli = is_israeli

class Event():
     def __init__(self, date, adversary:Adversary, target:Target ,reference, status, details, type, reporter):
         self.date = date
         self.adversary = adversary
         self.target = target
         self.reference = reference
         self.status = status
         self.details = details
         self.type = type
         self.reporter = reporter

     def toDict(self):
        dict = self.__dict__
        dict['adversary'] = self.adversary.__dict__
        dict['target'] = self.target.__dict__

        return dict
