import os
import pandas as pd
from django.core.management.base import BaseCommand
from fhtways.models import Node, Edge

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **kwargs):
        data_dir = os.path.join('fhtways', 'data_csv') # directory where the csv files are located

        for filename in os.listdir(data_dir): # goes through all files in the directory
            file_path = os.path.join(data_dir, filename) # path to file
            if filename.endswith('.csv'): # checks if file is csv-file
                if 'edges' in filename:
                    self.import_edges_from_csv(file_path) # is imported if the file has 'edges' in its name
                elif 'nodes' in filename:
                    self.import_nodes_from_csv(file_path) # is imported if the file has 'nodes' in its name

        self.stdout.write(self.style.SUCCESS('Successfully imported data from all CSV files'))

    def import_nodes_from_csv(self, file_path):
        nodes_df = pd.read_csv(file_path, delimiter=';') # reads csv file, separated with ';'
        print(f"Importing nodes from {file_path}")
        print(nodes_df.head())  

        for _, row in nodes_df.iterrows():
            print(row)  
            Node.objects.get_or_create(name=row['node']) #creates or gets specific node from the node column

    def import_edges_from_csv(self, file_path):
        edges_df = pd.read_csv(file_path, delimiter=';')
        print(f"Importing edges from {file_path}")
        print(edges_df.head())  

        for _, row in edges_df.iterrows():
            print(row)  
            source_node, _ = Node.objects.get_or_create(name=row['source']) # creates or gets source node from source column
            target_node, _ = Node.objects.get_or_create(name=row['target']) # creates or gets target node from target column
            Edge.objects.create( # creates a new edge with the specified attributes
                source=source_node,
                target=target_node,
                weight=int(row['weight']),
                description=row['description']
            )
