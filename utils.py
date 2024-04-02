import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from fastapi import HTTPException


def calculate_distance(point1:float, point2:float):
    """Calculate the distance between two points"""
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def fetch_coordinates(file):
    """Get the list of coordinates from the .csv file"""
    try:
        df = pd.read_csv(file)
        lats = df['lat']
        lngs = df['lng']
    except Exception as e:
        raise HTTPException(status_code=406, detail='Can\'t read the .csv file')
    points = list(zip(lngs, lats))
    if len(points) < 1:
        raise HTTPException(status_code=406, detail='No waypoints were found in the file')
    return points


def build_graph(points):
    """Make a graph from a list of coordinates"""
    graph = nx.Graph()
    for i, pos in enumerate(points):
        graph.add_node(f'{i}', pos=pos)

    # Add edges between points based on the Euclidean distance
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            waypoint1 = points[i]
            waypoint2 = points[j]
            distance = calculate_distance(waypoint1, waypoint2)
            graph.add_edge(f'{i}', f'{j}', weight=distance)
    return graph


def calculate_optimal_route(graph):
    """Find the optimal route using the greedy Travelling Salesman Problem algorithm
    having the source node set to the first node in the graph.
    Returns the list of nodes in the order of the optimal route"""
    source_node = next(iter(graph.nodes()), None)
    optimal_route = nx.approximation.greedy_tsp(graph, weight='weight', source=source_node)
    pos = nx.get_node_attributes(graph, 'pos')
    pos = [pos[node] for node in optimal_route]
    points = [{'lat': i[0], 'lng': i[1]} for i in pos]
    # plot_route(graph, optimal_route)
    return points


def plot_route(graph, optimal_route):
    # Plot the graph
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_nodes(graph.nodes['0'], pos=graph.nodes['0'])
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=[(optimal_route[i], optimal_route[i + 1]) for i in range(len(optimal_route) - 1)], edge_color='red', width=1)
    plt.title(f'Optimal route: {optimal_route}')
    plt.grid()
    plt.gca().axes.get_xaxis().set_visible(True)
    plt.savefig('route.png')
    plt.clf()