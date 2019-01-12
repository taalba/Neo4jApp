from py2neo import Graph

class RelationModel:
    """description of class"""
    def __init__(self, relationType, relationName, sourceEntityName, destinationEntityName):
        self.relationType = relationType
        self.relationName = relationName
        self.identifier = ""
        self.sourceEntityName = sourceEntityName
        self.destinationEntityName = destinationEntityName
        self.data = {}

    def get(self, name):
        return self.data[name]

    def set(self, name, value):
        self.data[name] = value

    def update(self, sourceEntity, destinationEntity):
        strCmd = "match (n1:" + self.sourceEntityName + "),  (n2:" + self.destinationEntityName + ")"
        strCmd = strCmd + " where n1." + sourceEntity.keyField + " = '" + sourceEntity.data[sourceEntity.keyField] + "'"
        strCmd = strCmd + " and n2." + destinationEntity.keyField + " = '" + destinationEntity.data[destinationEntity.keyField] + "'"
        strCmd = strCmd + " create (n1)-[:" + self.relationName + "]->(n2)"
        graph = Graph(password="Bluebee-123")
        graph.run(strCmd)

