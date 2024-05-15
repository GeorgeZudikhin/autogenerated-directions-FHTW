from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255, unique=True) 

    def __str__(self):
        return self.name 

class Edge(models.Model):
    source = models.ForeignKey(Node, related_name='source_edges', on_delete=models.CASCADE)
    target = models.ForeignKey(Node, related_name='target_edges', on_delete=models.CASCADE)
    weight = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.source} -> {self.target} : {self.weight}"
