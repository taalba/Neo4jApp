from py2neo import Graph
from objects.RelationModel import RelationModel

class EntityModel:
    """description of class"""
    def __init__(self, entityName):
        self.entityName = entityName
        self.identifier = ""
        self.keyField = ""
        self.model = {}
        self.data = {}
        self.relations = []

        graph = Graph(password="Bluebee-123")
        strQuery = "match (obj:EntityModel) where obj.name = '%s' return obj" %(self.entityName)
        result = graph.run(strQuery).data()        
        self.model = dict(result[0]['obj'])

        for fieldName in self.model:
            if (fieldName == "keyField"):   
                self.keyField = self.model[fieldName]
                self.data[self.model[fieldName]] = ''
            else:
                self.data[fieldName] = self.model[fieldName]

        strQuery = "match (d:EntityModel {name : '%s'})-[r]->(e) return type(r) as relationType,r.name as relationName,e.name as entityName" %(self.entityName)
        result = graph.run(strQuery).data()         
        for obj in result:
            self.relations.append(RelationModel(obj['relationType'], obj['relationName'], self.entityName, obj['entityName']))
 
    def find(self, identifier):
        graph = Graph(password="Bluebee-123")
        strCmd = "match (obj:" + self.entityName + ") where obj."
       
        for fieldName in self.model:
            if (fieldName == "keyField"):
                strCmd = strCmd + self.model[fieldName] + " = '" + identifier + "'"
        strCmd = strCmd + " return obj"
        result = graph.run(strCmd).data()
        result = dict(result[0]['obj'])

        for obj in self.data:
            self.data[obj] = result[obj]

    def findAll(self):
        graph = Graph(password="Bluebee-123")
        strCmd = 'match (obj:' + self.entityName + ') '
        strCmd = strCmd + ' return obj'
        result = graph.run(strCmd).data()
        lst = []
        for item in result:
            lst.append(dict(item['obj']))

        return lst

    def findRelated(self, relatedName):
        graph = Graph(password="Bluebee-123")
        strCmd = 'match (p:' + self.entityName + ')-[r]->(obj:' + relatedName + ') where p.' + self.keyField + ' = "' + self.data[self.keyField] + '" '
        strCmd = strCmd + ' return obj'
        result = graph.run(strCmd).data()
        lst = []
        for item in result:
            lst.append(dict(item['obj']))

        return lst
           
    def get(self, name):
        return self.data[name]

    def set(self, name, value):
        self.data[name] = value

    def update(self):
        #TODO: Check if exists, create if not else just update/merge
        i = 0
        strCmd = "merge ( :" + self.entityName + " {"
        for fieldName in self.data:
            if (i > 0):
                strCmd = strCmd + ', '
            strCmd = strCmd + fieldName + " : '" + self.data[fieldName] + "'"
            self.data[fieldName] = self.data[fieldName]
            i = i + 1
        strCmd = strCmd + "})"
        graph = Graph(password="Bluebee-123")
        graph.run(strCmd)

    def delete(self):
        #graph = Graph(password="Bluebee-123")
        print("delete called")

    def getRelationTo(self, entity):
        result = None
        for rel in self.relations:
            if rel.destinationEntityName == entity.entityName:
                result = rel
        return result



