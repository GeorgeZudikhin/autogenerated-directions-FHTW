import networkx as nx
import math

def create_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_node("stairs_left",       coord=(0, 6),    type="stairs")
    G.add_node("stairs_left_conn",  coord=(0, 0),    type="conn")

    G.add_node("F4.27",             coord=(2, 4),    type="room")
    G.add_node("F4.27_c",           coord=(2, 0),    type="corridor")

    G.add_node("F4.26",             coord=(5, 2),    type="room")
    G.add_node("F4.26_c",           coord=(5, 0),    type="corridor")

    G.add_node("F4.25",             coord=(8, 2),    type="room")
    G.add_node("F4.25_c",           coord=(8, 0),    type="corridor")

    G.add_node("F4.24",             coord=(11, 2),   type="room")
    G.add_node("F4.24_c",           coord=(11, 0),   type="corridor")

    G.add_node("F4.23",             coord=(14, 2),   type="room")
    G.add_node("F4.23_c",           coord=(14, 0),   type="corridor")

    G.add_node("F4.22",             coord=(17, 2),   type="room")
    G.add_node("F4.22_c",           coord=(17, 0),   type="corridor")

    G.add_node("F4.20",             coord=(20, 5),   type="room")
    G.add_node("F4.20_c",           coord=(20, 3),   type="corridor")
    G.add_node("F4.20_conn",        coord=(20, 0),   type="conn")

    G.add_node("door_left",         coord=(21, 3),   type="door")
    G.add_node("toilets",           coord=(24, 1),   type="toilets")
    G.add_node("lift",              coord=(30, 1),   type="lift")
    G.add_node("stairs_middle",     coord=(28, 6),   type="stairs")
    G.add_node("door_right",        coord=(35, 3),   type="door")
    
    G.add_node("F4.08",             coord=(37, 5),   type="room")
    G.add_node("F4.01",             coord=(37, 1),   type="room")
    G.add_node("F4.01_F4.08_c",     coord=(37, 3),   type="corridor")

    G.add_node("F4.07",             coord=(40, 5),   type="room")
    G.add_node("F4.02",             coord=(40, 1),   type="room")
    G.add_node("F4.02_F4.07_c",     coord=(40, 3),   type="corridor")

    G.add_node("F4.06",             coord=(43, 5),   type="room")
    G.add_node("F4.03",             coord=(43, 1),   type="room")
    G.add_node("F4.03_F4.06_c",     coord=(43, 3),   type="corridor")

    G.add_node("F4.05",             coord=(46, 6),   type="room")
    G.add_node("F4.04",             coord=(46, 0),   type="room")
    G.add_node("F4.04_F4.05_c",     coord=(46, 3),   type="corridor")

    G.add_node("stairs_right_conn", coord=(48, 3),   type="conn")
    G.add_node("stairs_right",      coord=(48, 8),   type="stairs")


# Add directed edges on the left side of the floor
    G.add_edge("stairs_left", "stairs_left_conn", weight=6, description="Öffne die Tür. Biege sofort rechts ab. Gehe 6 Schritte geradeaus bis die Wand links endet. ")
    G.add_edge("stairs_left_conn", "stairs_left", weight=6, description="Gehe 6 Schritte geradeaus weiter entlang bis zur Wand vorne. Die Treppentür befindet sich links. ")

    G.add_edge("stairs_left_conn", "F4.27_c", weight=2, description="Gehe 2 Schritte im Korridor geradeaus. ")
    G.add_edge("F4.27_c", "stairs_left_conn", weight=2, description="Gehe im Korridor 2 Schritte geradeaus bis zur Wand vor dir. ")

    G.add_edge("F4.27", "F4.27_c", weight=4, description="Öffne die Tür vor dir und verlasse den Raum F4.27. Gehe 4 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.27_c", "F4.27", weight=4, description="Gehe 4 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.27. ")

    G.add_edge("F4.26", "F4.26_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.26. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.26_c", "F4.26", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.26. ")

    G.add_edge("F4.25", "F4.25_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.25. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.25_c", "F4.25", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.25. ")

    G.add_edge("F4.24", "F4.24_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.24. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.24_c", "F4.24", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.24. ")

    G.add_edge("F4.23", "F4.23_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.23. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.23_c", "F4.23", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.23. ")

    G.add_edge("F4.22", "F4.22_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.22. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.22_c", "F4.22", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.22. ")

    G.add_edge("F4.20", "F4.20_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.20. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.20_c", "F4.20", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.20. ")

    G.add_edge("F4.08", "F4.01_F4.08_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.08. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.01_F4.08_c", "F4.08", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.08. ")

    G.add_edge("F4.07", "F4.02_F4.07_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.07. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.02_F4.07_c", "F4.07", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.07. ")

    G.add_edge("F4.06", "F4.03_F4.06_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.06. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.03_F4.06_c", "F4.06", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.06. ")

    G.add_edge("F4.05", "F4.04_F4.05_c", weight=3, description="Öffne die Tür vor dir und verlasse den Raum F4.05. Gehe 3 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.04_F4.05_c", "F4.05", weight=3, description="Gehe 3 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.05. ")

 
    G.add_edge("F4.04", "F4.04_F4.05_c", weight=3, description="Öffne die Tür vor dir und verlasse den Raum F4.04. Gehe 3 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.04_F4.05_c", "F4.04", weight=3, description="Gehe 3 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.04. ")

    G.add_edge("F4.03", "F4.03_F4.06_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.03. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.03_F4.06_c", "F4.03", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.03. ")

    G.add_edge("F4.02", "F4.02_F4.07_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.02. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.02_F4.07_c", "F4.02", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.02. ")

    G.add_edge("F4.01", "F4.01_F4.08_c", weight=2, description="Öffne die Tür vor dir und verlasse den Raum F4.01. Gehe 2 Schritte geradeaus in den Korridor. ")
    G.add_edge("F4.01_F4.08_c", "F4.01", weight=2, description="Gehe 2 Schritte geradeaus. Vor dir ist die Tür des Raumes F4.01. ")

    # Add directed edges between corridor/connection nodes
    G.add_edge("F4.27_c", "F4.26_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.26_c", "F4.27_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.26_c", "F4.25_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.25_c", "F4.26_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.25_c", "F4.24_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.24_c", "F4.25_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.24_c", "F4.23_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.23_c", "F4.24_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.23_c", "F4.22_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.22_c", "F4.23_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.22_c", "F4.20_conn", weight=3, description="Gehe im Korridor 3 Schritte geradeaus bis zur Wand vor dir. ")
    G.add_edge("F4.20_conn", "F4.22_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.20_conn", "F4.20_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.20_c", "F4.20_conn", weight=3, description="Gehe im Korridor 3 Schritte geradeaus bis zur Wand vor dir. ")

    G.add_edge("F4.01_F4.08_c", "F4.02_F4.07_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.02_F4.07_c", "F4.01_F4.08_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.02_F4.07_c", "F4.03_F4.06_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.03_F4.06_c", "F4.02_F4.07_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("F4.03_F4.06_c", "F4.04_F4.05_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")
    G.add_edge("F4.04_F4.05_c", "F4.03_F4.06_c", weight=3, description="Gehe im Korridor 3 Schritte geradeaus. ")

    G.add_edge("door_left", "F4.20_c", weight=1, description="Öffne die Tür und mache einen Schritt vorwärts in den Korridor. ")
    G.add_edge("F4.20_c", "door_left", weight=1, description="Gehe einen Schritt zur Tür vor dir. Öffne sie und du befindest dich in der Halle der 4. Etage. ")

    G.add_edge("door_right", "F4.01_F4.08_c", weight=2, description="Öffne die Tür und mache 2 Schritte vorwärts in den Korridor. ")
    G.add_edge("F4.01_F4.08_c", "door_right", weight=2, description="Gehe 2 Schritte zur Tür vor dir. Öffne sie und du befindest dich in der Halle der 4. Etage. ")

    # Add directed edges on the right side of the floor
    G.add_edge("F4.04_F4.05_c", "stairs_right_conn", weight=2, description="Gehe im Korridor 2 Schritte geradeaus bis zur Wand vor dir. ")
    G.add_edge("stairs_right_conn", "F4.04_F4.05_c", weight=2, description="Gehe im Korridor 2 Schritte geradeaus. ")

    G.add_edge("stairs_right_conn", "stairs_right", weight=5, description="Gehe 5 Schritte geradeaus weiter entlang bis zur Wand vorne. Die Treppentür befindet sich rechts. ")
    G.add_edge("stairs_right", "stairs_right_conn", weight=5, description="Öffne die Tür, dann biege sofort links ab. Gehe 5 Schritte geradeaus bis die Wand links endet. ")

    # Binding the middle part of the hall
    G.add_edge("door_left", "stairs_middle", weight=8, description="Gehe 5 Schritte geradeaus. Biege links ab und gehe 3 Schritte nach vorne zur Treppe der 4.Etage. ")
    G.add_edge("stairs_middle", "door_left", weight=8, description="Du befindest dich auf der 4.Etage. Gehe 3 Schritte geradeaus. Biege rechts ab und gehe 5 Schritte nach vorne bis du die Tür vor dir erreichst. ")

    G.add_edge("door_left", "lift", weight=10, description="Halte dich auf der rechten Seite der Halle. Gehe 10 Schritte geradeaus entlang der rechten Wand. Du hast die Aufzüge erreicht. Fühle nach der Lifttaste. Sie befindet sich auf Brusthöhe. Drücke darauf und du rufst einen Aufzug. ")
    G.add_edge("lift", "door_left", weight=10, description="Verlasse den Lift mit 2 Schritten vorwärts und biege links ab. Gehe 8 Schritte geradeaus zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")

    G.add_edge("door_left", "door_right", weight=14, description="Gehe 14 Schritte geradeaus durch die Halle des 4.Stocks bis zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")
    G.add_edge("door_right", "door_left", weight=14, description="Gehe 14 Schritte geradeaus durch die Halle des 4.Stocks bis zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")

    G.add_edge("door_left", "toilets", weight=3, description="Halte dich auf der rechten Seite der Halle. Gehe 3 Schritte geradeaus entlang der rechten Wand. Du hast die Toiletten erreicht. Links ist die Frauentoilette. In der Mitte ist die Toilette für Menschen mit Behinderungen. Rechts ist die Männertoilette. ")
    G.add_edge("toilets", "door_left", weight=3, description="Öffne die Toilettentür. Halte dich auf der linken Seite der Wand. Gehe 3 Schritte geradeaus bis zur Tür links. Öffne die Tür und du bist im Korridor. ")

    G.add_edge("toilets", "stairs_middle", weight=6, description="Öffne die Toilettentür. Gehe 2 Schritte geradeaus und drehe dich nach rechts. Mache 4 Schritte und drehe dich nach links. Du bist bei den Stiegen des 4. Stocks. ")
    G.add_edge("stairs_middle", "toilets", weight=6, description="Du befindest dich auf der 4.Etage. Gehe 2 Schritte geradeaus und biege rechts ab. Gehe 4 Schritte nach vorne und drehe dich nach links. Gehe 2 Schritte geradeaus. Du hast die Toiletten erreicht. Links ist die Frauentoilette. In der Mitte ist die Toilette für Menschen mit Behinderungen. Rechts ist die Männertoilette. ")

    G.add_edge("toilets", "lift", weight=4, description="Öffne die Toilettentür. Halte dich auf der rechten Seite der Halle. Gehe 4 Schritte geradeaus entlang der rechten Wand. Du hast die Aufzüge erreicht. Fühle nach der Lifttaste. Sie befindet sich auf Brusthöhe. Drücke darauf und du rufst einen Aufzug. ")
    G.add_edge("lift", "toilets", weight=4, description="Verlasse den Lift mit 2 Schritten geradeaus. Biege nach links ab. Halte dich auf der linken Seite der Halle. Gehe 2 Schritte geradeaus. Du hast die Toiletten erreicht. Links ist die Frauentoilette. In der Mitte ist die Toilette für Menschen mit Behinderungen. Rechts ist die Männertoilette. ")

    G.add_edge("door_right", "stairs_middle", weight=8, description="Du bist in der Halle der 4.Etage. Halte dich auf der rechten Seite der Halle. Gehe 8 Schritte geradeaus entlang der rechten Wand. Du bist bei den Stiegen des 4. Stocks. ")
    G.add_edge("stairs_middle", "door_right", weight=8, description="Du befindest dich auf der 4.Etage. Gehe 2 Schritte geradeaus und biege nach links ab. Gehe 6 Schritte geradeaus zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")

    G.add_edge("lift", "stairs_middle", weight=2, description="Verlasse den Lift mit 2 Schritten geradeaus. Du bist bei den Stiegen des 4. Stocks.")
    G.add_edge("stairs_middle", "lift", weight=2, description="Du befindest dich auf der 4.Etage. Gehe 2 Schritte geradeaus. Du hast die Aufzüge erreicht. Fühle nach der Lifttaste. Sie befindet sich auf Brusthöhe. Drücke darauf und du rufst einen Aufzug. ")

    G.add_edge("door_right", "toilets", weight=12, description="Du bist in der Halle der 4.Etage. Halte dich auf der linken Seite der Halle. Gehe 12 Schritte geradeaus. Du hast die Toiletten erreicht. Links ist die Frauentoilette. In der Mitte ist die Toilette für Menschen mit Behinderungen. Rechts ist die Männertoilette. ")
    G.add_edge("toilets", "door_right", weight=12, description="Öffne die Toilettentür. Gehe 2 Schritte geradeaus und biege nach rechts ab. Gehe 10 Schritte nach vorne, bis zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")

    G.add_edge("door_right", "lift", weight=7, description="Du bist in der Halle der 4.Etage. Halte dich auf der linken Seite der Halle. Gehe 7 Schritte geradeaus. Du hast die Aufzüge erreicht. Fühle nach der Lifttaste. Sie befindet sich auf Brusthöhe. Drücke darauf und du rufst einen Aufzug. ")
    G.add_edge("lift", "door_right", weight=7, description="Verlasse den Lift mit 2 Schritten geradeaus und biege nach rechts ab. Gehe 5 Schritte geradeaus, bis zur Tür vor dir. Öffne die Tür und du bist im Korridor. ")

    return G

# Calculate turn direction based on the angles of two consecutive edges
def calculate_turn_direction(angle1, angle2):
    # Calculate the difference in angle
    print(f"angle1: {angle1}, angle2: {angle2}")
    angle_diff = angle2 - angle1
    # Normalize the angle difference
    angle_diff = (angle_diff + 180) % 360 - 180  # Angle difference in range [-180, 180]
    print(f"angle_diff: {angle_diff}")

    if angle1 == 0 or angle2 == 0:
        print("turn description not appended, one of the angles = 0")
        return None
    elif angle_diff == 90:
        print("description 'links' appended")
        return 'links'
    elif angle_diff == -90:
        print("description 'rechts' appended")
        return 'rechts'
    else:
        print("turn description not appended, angle difference does not equal +/-90")
        return None


def calculate_angles(graph, prev_node, current_node, next_node):
    # Check if nodes exist
    try:
        node_data1 = graph.nodes[prev_node] if prev_node else graph.nodes[current_node]
        node_data2 = graph.nodes[current_node]
        node_data3 = graph.nodes[next_node] if next_node else None
    except KeyError as e:
        print(f"Node {e} does not exist in the graph")
        return None

    # Extract the coord parameter from the nodes
    coord1 = node_data1.get('coord') 
    coord2 = node_data2.get('coord')
    coord3 = node_data3.get('coord') if node_data3 else None

    if not coord3:
        return ''

    print(f"coord1: {coord1}, coord2: {coord2}, coord3: {coord3}")
    
    # Calculate the vectors for the incoming and outgoing paths
    vector_in = (coord2[0] - coord1[0], coord2[1] - coord1[1])
    vector_out = (coord3[0] - coord2[0], coord3[1] - coord2[1])
    
    # Calculate the angle between vectors
    angle_in = math.atan2(vector_in[1], vector_in[0])
    angle_out = math.atan2(vector_out[1], vector_out[0])
    
    # Use the angles to determine the direction
    return calculate_turn_direction(math.degrees(angle_in), math.degrees(angle_out))


def find_shortest_path(graph, start_node, end_node):
    try:
        path = nx.dijkstra_path(graph, start_node, end_node)
        path_edges = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        descriptions = []
        accumulated_distance = 0
        accumulated_nodes = 0

        for i, edge in enumerate(path_edges):
            current_node, next_node = edge
            prev_node = path[i - 1] if i > 0 else current_node
            edge_data = graph[current_node][next_node]
            print(prev_node + " - " + str(graph.nodes[prev_node]['coord']))
            print(current_node + " - " + str(graph.nodes[current_node]['coord']))
            print(next_node + " - " + str(graph.nodes[next_node]['coord']))
            print(edge_data)
            print("BREAK")

            turn = calculate_angles(graph, prev_node, current_node, next_node)

            if (graph.nodes[current_node]['type'] == 'corridor' and graph.nodes[next_node]['type'] == 'corridor' or 
                graph.nodes[current_node]['type'] == 'conn' and graph.nodes[next_node]['type'] == 'corridor'):
                print("Condition for skipping edges is met")
                # Accumulate distance
                accumulated_distance += edge_data['weight']
                accumulated_nodes += 1
                
                if turn:
                    descriptions.append(f"Biege {turn} ab. ")

            else:
                # Add accumulated distance to the description
                if accumulated_distance:
                    print("Finally appending the entire corridor description")
                    descriptions.append(f"Gehe geradeaus {accumulated_distance} Schritte im Korridor. Orientiere dich an den Zimmern auf deiner rechten Seite: du wirst an {accumulated_nodes} Zimmern vorbeigehen. ")
                    print(descriptions)
                    accumulated_distance = 0
                    accumulated_nodes = 0

                if turn:
                    descriptions.append(f"Biege {turn} ab. ")
        
                # If there is no accumulated distance, add the current edge's description
                print("Simply appending edge description")
                descriptions.append(edge_data['description'])

            print(descriptions)
        
        return path, descriptions
    
    except nx.NetworkXNoPath:
        return None, "No path exists between the specified nodes."