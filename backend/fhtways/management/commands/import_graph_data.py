import os
import pandas as pd
from django.core.management.base import BaseCommand
from fhtways.models import Node, Edge

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **kwargs):
        data_dir = os.path.join('fhtways', 'data_csv') # Verzeihcnis in denen sich die csv Dateien befinden

        for filename in os.listdir(data_dir): # geht alle Dateien im Verzeichnis durch
            file_path = os.path.join(data_dir, filename) # Pfad zur Dateix
            if filename.endswith('.csv'): #prüft ob Datei csv-Datei ist
                if 'edges' in filename:
                    self.import_edges_from_csv(file_path) # wird impotriert, falls die Datei 'edges' in Namen hat
                elif 'nodes' in filename:
                    self.import_nodes_from_csv(file_path) # wird impotriert, falls die Datei 'nodes' in Namen hat

        self.stdout.write(self.style.SUCCESS('Successfully imported data from all CSV files'))

    def import_nodes_from_csv(self, file_path):
        nodes_df = pd.read_csv(file_path, delimiter=';') # csv-Datei einlesen, mit ';' getrennt
        print(f"Importing nodes from {file_path}")
        print(nodes_df.head())  

        for _, row in nodes_df.iterrows():
            print(row)  
            Node.objects.get_or_create(name=row['node']) #erstellt oder holt bestimmten node aus der node spalte

    def import_edges_from_csv(self, file_path):
        edges_df = pd.read_csv(file_path, delimiter=';')
        print(f"Importing edges from {file_path}")
        print(edges_df.head())  

        for _, row in edges_df.iterrows():
            print(row)  
            source_node, _ = Node.objects.get_or_create(name=row['source']) # erstellt oder holt source node aus source Spalte
            target_node, _ = Node.objects.get_or_create(name=row['target']) # erstellt oder holt target node aus source Spalte
            Edge.objects.create( # erstellt eine neue Kante mit den angeegebenen Attributen
                source=source_node,
                target=target_node,
                weight=int(row['weight']),
                description=row['description']
            )
