from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .graph_setup_coord import create_graph, find_shortest_path
import json

class PathFindingView(APIView):

    """
    API View to find the shortest path between two points in a graph.
    Expects 'start' and 'end' in the POST request data.
    """

    def post(self, request):
        data = json.loads(request.body)
        start = data.get('start')
        end = data.get('end')

        try:
            graph = create_graph()
            _, descriptions = find_shortest_path(graph, start, end)

            return Response({"path": descriptions}, status=status.HTTP_200_OK)

        except Exception as e: 
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)