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
    G.add_edge("stairs_left", "stairs_left_conn", weight=6, description="Öffnen Sie die Tür vor Ihnen, um in den Korridor der 4. Etage zu gelangen und biegen Sie unmittelbar rechts ab. Gehen Sie den Korridor 5 Schritte geradeaus weiter, bis Sie spüren, dass die Wand auf Ihrer rechten Seite endet. Dies zeigt das Auftreten eines neuen Korridors auf Ihrer linken Seite an.")
    G.add_edge("stairs_left_conn", "stairs_left", weight=6, description="Gehen Sie den Korridor 6 Schritte geradeaus weiter entlang, bis Sie das Ende des Korridors erreichen. Hier finden Sie eine Tür auf Ihrer linken Seite. Fühlen Sie nach dem Türgriff, um die Tür zu öffnen und die Stiegen zu erreichen.")


    G.add_edge("stairs_left_conn", "F4.27_c", weight=2, description="Gehen Sie vom Treppenhaus aus 2 Schritte geradeaus im Korridor. Fühlen Sie den Boden unter Ihren Füßen, um sich zu orientieren.")
    G.add_edge("F4.27_c", "stairs_left_conn", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Sie werden die Wand auf Ihrer rechten Seite bemerken. Nutzen Sie diese als Orientierungshilfe.")


    # Add directed edges between room nodes and their respective corridor nodes
    G.add_edge("F4.27", "F4.27_c", weight=4, description="Öffnen Sie die Tür und verlassen Sie Raum F4.27. Gehen Sie 4 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.27_c", "F4.27", weight=4, description="Gehen Sie 4 Schritte geradeaus im Korridor. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.27 zu betreten.")


    G.add_edge("F4.26", "F4.26_c", weight=2, description="Öffnen Sie die Tür und verlassen Sie Raum F4.26. Gehen Sie 2 Schritte geradeaus. Sie erreichen den Korridor. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.26_c", "F4.26", weight=2, description="Gehen Sie 2 Schritte geradeaus im Korridor. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.26 zu betreten.")


    G.add_edge("F4.25", "F4.25_c", weight=2, description="Öffnen Sie die Tür von Raum F4.25 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.25_c", "F4.25", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.25 zu betreten.")


    G.add_edge("F4.24", "F4.24_c", weight=2, description="Öffnen Sie die Tür von Raum F4.24 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.24_c", "F4.24", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.24 zu betreten.")


    G.add_edge("F4.23", "F4.23_c", weight=2, description="Öffnen Sie die Tür von Raum F4.23 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.23_c", "F4.23", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.23 zu betreten.")


    G.add_edge("F4.22", "F4.22_c", weight=2, description="Öffnen Sie die Tür von Raum F4.22 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.22_c", "F4.22", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.22 zu betreten.")


    G.add_edge("F4.20", "F4.20_c", weight=2, description="Öffnen Sie die Tür von Raum F4.20 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.20_c", "F4.20", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.20 zu betreten.")


    G.add_edge("F4.08", "F4.01_F4.08_c", weight=2, description="Öffnen Sie die Tür von Raum F4.08 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.01_F4.08_c", "F4.08", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.08 zu betreten.")


    G.add_edge("F4.07", "F4.02_F4.07_c", weight=2, description="Öffnen Sie die Tür von Raum F4.07 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.02_F4.07_c", "F4.07", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.07 zu betreten.")


    G.add_edge("F4.06", "F4.03_F4.06_c", weight=2, description="Öffnen Sie die Tür von Raum F4.06 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.03_F4.06_c", "F4.06", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.06 zu betreten.")


    G.add_edge("F4.05", "F4.04_F4.05_c", weight=3, description="Öffnen Sie die Tür von Raum F4.05 und treten Sie heraus. Gehen Sie 3 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.04_F4.05_c", "F4.05", weight=3, description="Gehen Sie im Korridor 3 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer rechten Seite, um Raum F4.05 zu betreten.")

 
    G.add_edge("F4.04", "F4.04_F4.05_c", weight=3, description="Öffnen Sie die Tür von Raum F4.04 und treten Sie heraus. Gehen Sie 3 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.04_F4.05_c", "F4.04", weight=3, description="Gehen Sie im Korridor 3 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.04 zu betreten.")


    G.add_edge("F4.03", "F4.03_F4.06_c", weight=2, description="Öffnen Sie die Tür von Raum F4.03 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.03_F4.06_c", "F4.03", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Suchen Sie die Tür auf Ihrer rechten Seite, um Raum F4.03 zu betreten.")


    G.add_edge("F4.02", "F4.02_F4.07_c", weight=2, description="Öffnen Sie die Tür von Raum F4.02 und treten Sie heraus. Gehen Sie 2 Schritte geradeaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.02_F4.07_c", "F4.02", weight=2, description="Gehen Sie im Korridor 2 Schritte geradeaus. Fühlen Sie nach der Tür auf Ihrer linken Seite, um Raum F4.02 zu betreten.")


    G.add_edge("F4.01", "F4.01_F4.08_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.01, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen. Achten Sie auf die Veränderung in der Akustik, die den Übergang zum Korridor anzeigt.")
    G.add_edge("F4.01_F4.08_c", "F4.01", weight=2, description="Gehen Sie im Korridor geradeaus für zwei Schritte. Fühlen Sie nach der Tür vor Ihnen und öffnen Sie diese, um Raum F4.01 zu betreten.")


    # Add directed edges between corridor/connection nodes
    G.add_edge("F4.27_c", "F4.26_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.26_c", "F4.27_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.26_c", "F4.25_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.25_c", "F4.26_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.25_c", "F4.24_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.24_c", "F4.25_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.24_c", "F4.23_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.23_c", "F4.24_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.23_c", "F4.22_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.22_c", "F4.23_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.22_c", "F4.20_conn", weight=3, description="Gehen Sie zwei Schritte im Korridor geradeaus, bis Sie auf eine Wand stoßen. Diese Wand kennzeichnet das Ende des Korridors und signalisiert eine Richtungsänderung.")
    G.add_edge("F4.20_conn", "F4.22_c", weight=3, description="Gehen Sie zwei Schritte im Korridor geradeaus, bis Sie auf eine Wand stoßen. Diese Wand kennzeichnet das Ende des Korridors und signalisiert eine Richtungsänderung.")


    G.add_edge("F4.20_conn", "F4.20_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.20_c", "F4.20_conn", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.01_F4.08_c", "F4.02_F4.07_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.02_F4.07_c", "F4.01_F4.08_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.02_F4.07_c", "F4.03_F4.06_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.03_F4.06_c", "F4.02_F4.07_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")


    G.add_edge("F4.03_F4.06_c", "F4.04_F4.05_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")
    G.add_edge("F4.04_F4.05_c", "F4.03_F4.06_c", weight=3, description="Bewegen Sie sich im Korridor drei Schritte geradeaus. Achten Sie auf die Beschaffenheit des Bodens und die Akustik des Raumes, um Ihre Bewegung zu orientieren.")


    G.add_edge("door_left", "F4.20_c", weight=1, description="Nachdem Sie die Tür geöffnet haben, machen Sie einen Schritt vorwärts, um den Korridor zu betreten.")
    G.add_edge("F4.20_c", "door_left", weight=1, description="Machen Sie einen Schritt vorwärts, um die Tür zu erreichen. Fühlen Sie nach der Türklinke, um in die Halle der 4. Etage zu gelangen.")


    G.add_edge("door_right", "F4.01_F4.08_c", weight=2, description="Öffnen Sie die Tür und gehen Sie zwei Schritte geradeaus im Korridor. Fühlen Sie den Boden und orientiere Sie sich in der Umgebung.")
    G.add_edge("F4.01_F4.08_c", "door_right", weight=2, description="Gehen Sie zwei Schritte geradeaus weiter im Korridor, bis Sie die Tür vor sich fühlen. Verwenden Sie Ihren Tastsinn, um die Türklinke zu finden.")


    # Add directed edges on the right side of the floor
    G.add_edge("F4.04_F4.05_c", "stairs_right_conn", weight=2, description="Gehen Sie zwei Schritte geradeaus im Korridor. Fühlen Sie die Wand, um sich zu orientieren und die Richtung zu halten.")
    G.add_edge("stairs_right_conn", "F4.04_F4.05_c", weight=2, description="Gehen Sie zwei Schritte geradeaus im Korridor. Fühlen Sie die Wand, um sich zu orientieren und die Richtung zu halten.")


    G.add_edge("stairs_right_conn", "stairs_right", weight=5, description="Gehen Sie fünf Schritte geradeaus im Korridor. Suchen Sie die Tür auf der rechten Seite am Ende des Korridors. Fühlen Sie nach dem Türgriff, um die Treppe zu erreichen.")
    G.add_edge("stairs_right", "stairs_right_conn", weight=5, description="Öffnen Sie die Tür vor Ihnen, um in den Korridor der 4. Etage zu gelangen und biegen Sie unmittelbar links ab. Gehen Sie den Korridor 5 Schritte geradeaus weiter, bis Sie spüren, dass die Wand auf Ihrer linken Seite endet. Dies zeigt das Auftreten eines neuen Korridors auf Ihrer rechten Seite an.")


    # Binding the middle part of the hall
    G.add_edge("door_left", "stairs_middle", weight=8, description="Um zur Treppe des 4. Stocks zu gelangen, gehen Sie 5 Schritte geradeaus, dann biegen Sie nach links ab und machen Sie noch 2 Schritte nach vorne. Hier erreichen Sie die Treppe. Seien Sie äußerst vorsichtig, um Stufen und Hindernisse zu erkennen und sicher zu navigieren.")
    G.add_edge("stairs_middle", "door_left", weight=8, description="Nachdem Sie die 4. Etage erreicht haben, gehen Sie 2 Schritte geradeaus und biegen Sie dann nach rechts ab. Setzen Sie Ihren Weg fort, bis Sie die Tür vor sich erreichen. Achten Sie auf den Boden, um Unebenheiten zu spüren und sicherzustellen, dass Sie auf dem richtigen Weg sind.")


    G.add_edge("door_left", "lift", weight=10, description="Nachdem Sie zur Tür gelangt haben, die zur Halle der 4.Etage führt, gehen Sie zur rechten Seite des Raumes, um die rechte Wand zu erreichen. Von dort aus gehen Sie 10 Schritte geradeaus entlang der rechten Wand. Wenn Sie die Lifttaste erreichen, die zirka auf Ihrer Brusthöhe befindet, drücken Sie sie, um den Aufzug zu rufen.")
    G.add_edge("lift", "door_left", weight=10, description="Verlassen Sie den Lift mit zwei Schritten und biegen Sie dann links ab. Gehen Sie weitere 8 Schritte geradeaus, um eine Tür zu erreichen. Fühlen Sie nach der Türklinke, um in den Eingangsbereich der 4. Etage zu gelangen.")

    G.add_edge("door_left", "door_right", weight=14, description="Gehen Sie 14 Schritte geradeaus durch die ganze Halle des 4.Stocks, bis Sie die Tür vor Ihnen erreichen. Achten Sie auf die taktilen Pflastersteine unter Ihren Füßen, die Ihnen den Weg weisen, und die Akustik in der Halle des 4.Stocks, um Ihre Orientierung zu verbessern.")
    G.add_edge("door_right", "door_left", weight=14, description="Gehen Sie 14 Schritte geradeaus durch die ganze Halle des 4.Stocks, bis Sie die Tür vor Ihnen erreichen. Achten Sie auf die taktilen Pflastersteine unter Ihren Füßen, die Ihnen den Weg weisen, und die Akustik in der Halle des 4.Stocks, um Ihre Orientierung zu verbessern.")

    G.add_edge("door_left", "toilets", weight=3, description="Drehen Sie sich direkt nach rechts und machen Sie drei gleichmäßige Schritte. Fühlen Sie nach der Türklinke auf der rechten Seite und öffnen Sie die Tür, um die Toilette zu erreichen.")
    G.add_edge("toilets", "door_left", weight=3, description="Öffnen Sie die Toilettentür, machen Sie drei gleichmäßige Schritte geradeaus, drehen Sie sich nach links und fühlen Sie nach der Türklinke vor Ihnen. Öffnen Sie die Tür und gehen Sie geradeaus.")


    G.add_edge("toilets", "stairs-middle", weight=6, description="Öffnen Sie die Toilettentür, gehen Sie zwei gleichmäßige Schritte geradeaus, dann drehen Sie sich nach rechts und machen zwei weitere Schritte. Drehen Sie sich nach links und folgen Sie dem akustischen Signal, um die Stiegen des 4. Stocks zu erreichen.")
    G.add_edge("stairs-middle", "toilets", weight=6, description="Nachdem Sie den 4. Stock erreicht haben, gehen Sie zwei gleichmäßige Schritte geradeaus, drehen Sie sich nach rechts. Gehen Sie zwei weitere Schritte und drehen Sie sich dann nach links. Öffnen Sie die Tür vor Ihnen, um die Toilette zu erreichen.")


    G.add_edge("toilets", "lift", weight=4, description="Öffnen Sie die Toilettentür, machen Sie zwei gleichmäßige Schritte geradeaus, drehen Sie sich um 90 Grad nach rechts und machen zwei weitere Schritte. Drehen Sie sich erneut um 90 Grad nach rechts. Folgen Sie der veränderten Bodentextur, um die Lifte zu erreichen.")
    G.add_edge("lift", "toilets", weight=4, description="Verlassen Sie den Lift, machen Sie zwei Schritte geradeaus und drehen Sie sich nach links. Machen Sie zwei weitere Schritte und drehen Sie sich dann nach links. Öffnen Sie die Tür vor Ihnen, um die Toilette zu erreichen.")


    G.add_edge("door_right", "stairs_middle", weight=8, description="Gehen Sie fünf gleichmäßige Schritte geradeaus und drehen Sie sich nach rechts. Machen Sie noch zwei Schritte geradeaus und Sie erreichen die Stiegen.")
    G.add_edge("stairs_middle", "door_right", weight=8, description="Nachdem Sie die 4. Etage erreicht haben, gehen Sie zwei gleichmäßige Schritte geradeaus und drehen Sie sich dann nach links. Gehen Sie weiter geradeaus, bis Sie die Tür vor sich fühlen, und öffnen Sie diese Tür.")


    G.add_edge("lift", "stairs-middle", weight=2, description="Verlassen Sie den Lift und gehen Sie zwei Schritte geradeaus. Sie erreichen dann die Treppen des 4. Stocks. Fühlen Sie die Wand oder das Geländer, um sich zur Treppe zu orientieren.")
    G.add_edge("stairs-middle", "lift", weight=2, description="Nachdem Sie den 4. Stock erreicht haben, gehen Sie zwei Schritte geradeaus. Öffnen Sie die Tür vor Ihnen, um zum Lift zu gelangen. Achten Sie auf die Änderung der Umgebungsgeräusche und den Bodenbelag, um den Lift zu identifizieren.")


    G.add_edge("door_right", "toilets", weight=12, description="Halten Sie sich an der linken Seite, wenn Sie zur Toilette gehen. Gehen Sie 12 Schritte nach vorne, bis Sie die Tür links vor sich spüren. Verwenden Sie Ihren Tastsinn, um die Tür zu identifizieren.")
    G.add_edge("toilets", "door_right", weight=12, description="Verlassen Sie die Toilette, machen Sie zwei Schritte und biegen Sie nach rechts ab. Gehen Sie zehn Schritte nach vorne, bis Sie die Tür vor sich erreichen. Spüren Sie nach der Tür, um den Eingang zu finden.")


    G.add_edge("door_right", "lift", weight=7, description="Halten Sie sich an der linken Seite, wenn Sie zu den Aufzügen gehen. Gehen Sie 7 Schritte nach vorne, bis Sie die Aufzüge links vor sich spüren. Verwenden Sie Ihren Tastsinn, um die Aufzüge zu lokalisieren.")
    G.add_edge("lift", "door_right", weight=7, description="Verlassen Sie den Lift, gehen Sie zwei Schritte nach vorne und biegen Sie dann rechts ab. Machen Sie 5 Schritte nach vorne, bis Sie die Tür vor sich erreichen. Fühlen Sie nach der Tür, um den Eingangsbereich zu erkennen.")

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
                    descriptions.append(f"Biegen Sie {turn} ab.")

            else:
                # Add accumulated distance to the description
                if accumulated_distance:
                    print("Finally appending the entire corridor description")
                    descriptions.append(f"Gehen Sie geradeaus {accumulated_distance} Schritte im Korridor. Orientieren Sie sich an den Zimmern auf ihrer rechten Seite: Sie werden an {accumulated_nodes} Zimmern vorbeigehen.")
                    print(descriptions)
                    accumulated_distance = 0
                    accumulated_nodes = 0

                if turn:
                    descriptions.append(f"Biegen Sie {turn} ab.")
        
                # If there is no accumulated distance, add the current edge's description
                print("Simply appending edge description")
                descriptions.append(edge_data['description'])

            print(descriptions)
        
        return path, descriptions
    
    except nx.NetworkXNoPath:
        return None, "No path exists between the specified nodes."