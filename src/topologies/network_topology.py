import random
import time
import networkx as nx
import matplotlib.pyplot as plt
import os

class NetworkTopology:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id):
        # Add a node to the topology
        self.nodes[node_id] = {}

    def add_edge(self, node1_id, node2_id, weight=1):
        # Add an edge between two nodes
        self.edges.append((node1_id, node2_id, weight))

    def display(self):
        # Display the topology
        for edge in self.edges:
            print(f"Node {edge[0]} is connected to Node {edge[1]} with weight {edge[2]}")



class StarTopology:
    def __init__(self, num_users):
        self.server = 'Server'
        self.users = [f'User{i+1}' for i in range(num_users)]
        self.edges = []

    def create_star_topology(self):
        # Connect each user to the server
        for user in self.users:
            self.edges.append((self.server, user))

    def display(self):
        # Display the topology
        print(f"{self.server} is the central node in the star topology.")
        for edge in self.edges:
            print(f"{edge[0]} is connected to {edge[1]}")

    # Note the indentation level of the following method
    def simulate_network(self):
        # Simulate sending data from server to all users
        for user in self.users:
            latency = self.simulate_latency()
            packet_loss = self.simulate_packet_loss()
            jitter = self.simulate_jitter()

            if not packet_loss:
                print(f"Sending data from {self.server} to {user} with latency {latency}ms and jitter {jitter}ms")
                time.sleep(latency / 1000)  # Simulate latency
            else:
                print(f"Packet lost when sending from {self.server} to {user}")

    def simulate_latency(self):
        # Return a simulated latency in milliseconds
        base_latency = 20  # base latency in ms
        return base_latency + random.randint(0, 100)  # add additional random latency

    def simulate_packet_loss(self):
        # Return True if a packet is lost, based on a random threshold
        return random.random() < 0.1  # 10% chance to lose a packet

    def simulate_jitter(self):
        # Return a simulated jitter in milliseconds
        return random.randint(0, 10)  # jitter between 0 and 10 ms

    def draw_topology(self):
            # Create a networkx graph
            G = nx.Graph()

            # Add the server node
            G.add_node(self.server)

            # Add user nodes and edges to the graph
            for user in self.users:
                G.add_node(user)
                G.add_edge(self.server, user)

            # Draw the network
            pos = nx.spring_layout(G)  # positions for all nodes
            nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
            plt.title("Star Network Topology")

            # Specify the directory path relative to the current script
            directory = "network_images"
            
            # Check if the directory exists, and create it if it doesn't
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Save the figure to a file in the specified directory
            plt.savefig(os.path.join(directory, "star_network_topology.png"), format='png', bbox_inches='tight')
            
            # Close the plot to avoid displaying it
            plt.close()

class BusTopology:
    def __init__(self):
        self.graph = nx.Graph()
        self.bus_node = "Bus"  # Representing the bus as a node for visualization

    def add_node(self, node_id):
        # Add a node to the topology
        self.graph.add_node(node_id)
        # Connect the node to the bus
        self.graph.add_edge(self.bus_node, node_id)
    
        def create_bus_topology(self):
        # This method will be similar to the create_star_topology
        # but will connect each node to the bus node.
            pass  # Connect each node to the self.bus_node

    def simulate_network(self):
        # Simulate sending data across the bus to all nodes
        for node in self.graph.nodes:
            if node != self.bus_node:  # Skip the bus node itself
                latency = self.simulate_latency()
                packet_loss = self.simulate_packet_loss()
                jitter = self.simulate_jitter()

                if not packet_loss:
                    print(f"Sending data over the bus to {node} with latency {latency}ms and jitter {jitter}ms")
                    time.sleep(latency / 1000)  # Simulate latency
                else:
                    print(f"Packet lost when sending to {node}")

    def simulate_latency(self):
        # Mirror method from StarTopology
        base_latency = 20  # base latency in ms
        return base_latency + random.randint(0, 100)  # add additional random latency

    def simulate_packet_loss(self):
        # Mirror method from StarTopology
        return random.random() < 0.1  # 10% chance to lose a packet

    def simulate_jitter(self):
        # Mirror method from StarTopology
        return random.randint(0, 10)  # jitter between 0 and 10 ms

    def display(self, filename='bus_topology.png'):
        # Display the topology
        G = self.graph

        # Assign positions to nodes for visualization
        # The bus node will be at the center on the y-axis, and other nodes will be on a line (y=0)
        pos = {node: (index, 0) for index, node in enumerate(G.nodes()) if node != self.bus_node}
        pos[self.bus_node] = (len(pos) // 2, 1)  # Center the bus node above the others

        nx.draw(G, pos, with_labels=True, node_color='blue', font_weight='bold')

        # Specify the directory path relative to the current script
        directory = "network_images"
        
        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the figure in the specified directory
        plt.savefig(os.path.join(directory, filename), format='png', bbox_inches='tight')
        
        # Close the plot to avoid displaying it in interactive environments
        plt.close()


class RingTopology:
    def __init__(self, num_nodes):
        self.nodes = [f'Node{i+1}' for i in range(num_nodes)]
        self.edges = []

    def create_ring_topology(self):
        # Connect each node to its next node in the list to form a ring
        num_nodes = len(self.nodes)
        for i in range(num_nodes):
            self.edges.append((self.nodes[i], self.nodes[(i + 1) % num_nodes]))

    def display(self):
        # Display the topology
        print("Ring Network Topology:")
        for edge in self.edges:
            print(f"{edge[0]} is connected to {edge[1]}")

    def simulate_network(self):
        # Simulate sending data between nodes in the ring
        for node in self.nodes:
            latency = self.simulate_latency()
            packet_loss = self.simulate_packet_loss()
            jitter = self.simulate_jitter()

            if not packet_loss:
                print(f"Sending data from {node} with latency {latency}ms and jitter {jitter}ms")
                time.sleep(latency / 1000)  # Simulate latency
            else:
                print(f"Packet lost when sending from {node}")

    def simulate_latency(self):
        # Mirror method from StarTopology
        base_latency = 20  # base latency in ms
        return base_latency + random.randint(0, 100)

    def simulate_packet_loss(self):
        # Mirror method from StarTopology
        return random.random() < 0.1

    def simulate_jitter(self):
        # Mirror method from StarTopology
        return random.randint(0, 10)

    def draw_topology(self):
        # Create a networkx graph
        G = nx.Graph()

        # Add nodes and edges to the graph
        for node in self.nodes:
            G.add_node(node)
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        # Draw the network
        pos = nx.circular_layout(G)  # positions for all nodes in a circle
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
        plt.title("Ring Network Topology")

        # Save the figure to a file
        directory = "network_images"
        if not os.path.exists(directory):
            os.makedirs(directory)
        plt.savefig(os.path.join(directory, "ring_network_topology.png"), format='png', bbox_inches='tight')
        plt.close()

class MeshTopology:
    def __init__(self, num_nodes):
        self.nodes = [f'Node{i+1}' for i in range(num_nodes)]
        self.edges = []

    def create_mesh_topology(self):
        # Connect each node to every other node
        num_nodes = len(self.nodes)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                self.edges.append((self.nodes[i], self.nodes[j]))

    def display(self):
        # Display the topology
        print("Mesh Network Topology:")
        for edge in self.edges:
            print(f"{edge[0]} is connected to {edge[1]}")

    def simulate_network(self):
        # Simulate sending data between all pairs of nodes
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    latency = self.simulate_latency()
                    packet_loss = self.simulate_packet_loss()
                    jitter = self.simulate_jitter()

                    if not packet_loss:
                        print(f"Sending data from {node1} to {node2} with latency {latency}ms and jitter {jitter}ms")
                        time.sleep(latency / 1000)  # Simulate latency
                    else:
                        print(f"Packet lost when sending from {node1} to {node2}")

    def simulate_latency(self):
        # Mirror method from StarTopology
        base_latency = 20  # base latency in ms
        return base_latency + random.randint(0, 100)

    def simulate_packet_loss(self):
        # Mirror method from StarTopology
        return random.random() < 0.1

    def simulate_jitter(self):
        # Mirror method from StarTopology
        return random.randint(0, 10)

    def draw_topology(self):
        # Create a networkx graph
        G = nx.Graph()

        # Add nodes and edges to the graph
        for node in self.nodes:
            G.add_node(node)
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        # Draw the network
        pos = nx.spring_layout(G)  # Positions for all nodes
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
        plt.title("Mesh Network Topology")

        # Save the figure to a file
        directory = "network_images"
        if not os.path.exists(directory):
            os.makedirs(directory)
        plt.savefig(os.path.join(directory, "mesh_network_topology.png"), format='png', bbox_inches='tight')
        plt.close()

class TreeTopology:
    def __init__(self, num_levels, branching_factor):
        self.root = 'Root'
        self.nodes = [self.root]
        self.edges = []
        self.num_levels = num_levels
        self.branching_factor = branching_factor

    def create_tree_topology(self):
        # Manually adding nodes to create an unbalanced tree with 10 nodes
        self.nodes = ['Root', 'Node1', 'Node2', 'Node3', 'Node4', 'Node5', 'Node6', 'Node7', 'Node8', 'Node9']
        self.edges = [('Root', 'Node1'), ('Root', 'Node2'), ('Root', 'Node3'),
                    ('Node1', 'Node4'), ('Node1', 'Node5'), ('Node2', 'Node6'), 
                    ('Node2', 'Node7'), ('Node3', 'Node8'), ('Node3', 'Node9')]

    def display(self):
        # Display the topology
        print("Tree Network Topology:")
        for edge in self.edges:
            print(f"{edge[0]} is connected to {edge[1]}")

    def simulate_network(self):
        # Simulate sending data from root to all nodes
        for node in self.nodes:
            if node != self.root:
                latency = self.simulate_latency()
                packet_loss = self.simulate_packet_loss()
                jitter = self.simulate_jitter()

                if not packet_loss:
                    print(f"Sending data from {self.root} to {node} with latency {latency}ms and jitter {jitter}ms")
                    time.sleep(latency / 1000)  # Simulate latency
                else:
                    print(f"Packet lost when sending from {self.root} to {node}")

    def simulate_latency(self):
        # Mirror method from StarTopology
        base_latency = 20  # base latency in ms
        return base_latency + random.randint(0, 100)

    def simulate_packet_loss(self):
        # Mirror method from StarTopology
        return random.random() < 0.1

    def simulate_jitter(self):
        # Mirror method from StarTopology
        return random.randint(0, 10)

    def draw_topology(self):
        # Create a networkx graph
        G = nx.Graph()

        # Add nodes and edges to the graph
        for node in self.nodes:
            G.add_node(node)
        for edge in self.edges:
            G.add_edge(edge[0], edge[1])

        # Draw the network
        pos = nx.spring_layout(G)  # Positions for all nodes
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
        plt.title("Tree Network Topology")

        # Save the figure to a file
        directory = "network_images"
        if not os.path.exists(directory):
            os.makedirs(directory)
        plt.savefig(os.path.join(directory, "tree_network_topology.png"), format='png', bbox_inches='tight')
        plt.close()

