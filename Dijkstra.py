{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import heapq\ndef dijkstra(graph,start):\n    dist={vertex:float('infinity')for vertex in graph}\n    prev={vertex:None for vertex in graph}\n    dist[start]=0\n    priority_queue=[(0,start)]\n    while priority_queue:\n        current_dist,u=heapq.heappop(priority_queue)\n        if current_dist>dist[u]:\n            continue\n        for neighbor,weight in graph[u]:\n            distance=current_dist+weight\n            if distance<dist[neighbor]:\n                dist[neighbor]=distance\n                prev[neighbor]=u\n                heapq.heappush(priority_queue,(distance,neighbor))\n    return dist,prev\ngraph={\n    0:[(1,4),(7,8)],\n    1:[(0,4),(2,8),(7,11)],\n    2:[(1,8),(3,7),(5,4),(8,2)],\n    3:[(2,7),(4,9),(5,14)],\n    4:[(3,9),(5,10)],\n    5:[(2,4),(3,14),(4,10),(6,2)],\n    6:[(5,2),(7,1),(8,6)],\n    7:[(0,8),(1,11),(6,1),(8,7)],\n    8:[(2,2),(6,6),(7,7)]\n}\nstart_vertex=0;\ndistances,predecessors=dijkstra(graph,start_vertex)\nprint(\"Distances:\",distances)\nprint(\"Predecessors\",predecessors)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Distances: {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}\nPredecessors {0: None, 1: 0, 2: 1, 3: 2, 4: 5, 5: 6, 6: 7, 7: 0, 8: 2}\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 4
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}