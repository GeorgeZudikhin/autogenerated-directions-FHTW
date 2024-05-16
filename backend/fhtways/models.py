from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255, unique=True) 

    def __str__(self):
        return self.name 

class Edge(models.Model):
    source = models.ForeignKey(Node, related_name='source_edges', on_delete=models.CASCADE)
    # FK to Node for the source node
    # related_name allows reverse lookup of source edges from a node
    # on_delete=models.CASCADE deletes edges if the source node is deleted

    target = models.ForeignKey(Node, related_name='target_edges', on_delete=models.CASCADE)
    # FK to Node for the target node
    # related_name allows reverse lookup of target edges from a node
    # on_delete=models.CASCADE deletes edges if the target node is deleted

    weight = models.IntegerField() # Integer field to store the weight of the edge

    description = models.TextField() # Text field to store a description of the edge

    def __str__(self):
        return f"{self.source} -> {self.target} : {self.weight}"  # String showing source, target, and weight of the edge