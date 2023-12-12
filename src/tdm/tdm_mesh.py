import sys
import csv  # Import the CSV module
import time
import random
from datetime import datetime  # Import the datetime module
import os

from topologies.network_topology import MeshTopology

class TDMMesh:
    def __init__(self, mesh_topology):
        self.mesh_topology = mesh_topology
        self.data = []  # Create an empty list to store simulation data

    def simulate_tdm(self):
        print("TDM Mesh Simulation:")
        for node in self.mesh_topology.nodes:
            transmission_data = self.transmit_data(node)
            self.data.append(transmission_data)  # Store data for this transmission
            print(transmission_data)
            time.sleep(1)  # Sleep for 1 second between transmissions

    def transmit_data(self, node):
        # Simulate data transmission to a specific node and return the data with a timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_size = random.randint(100, 1000)
        start_time = time.time()
        data = f"{current_time}: Node {node} is transmitting {data_size} units of data using TDM"
        time.sleep(0.5)  # Simulate transmission time
        end_time = time.time()
        transmission_time = end_time - start_time
        return (node, data_size, transmission_time, "Completed")

    def save_to_csv(self, filename='tdm_mesh_simulation.csv'):
        directory = "simulation"  # Directory where the CSV file will be saved
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Node", "Data Size (Units)", "Transmission Time (Seconds)", "Status"])
            for data in self.data:
                csv_writer.writerow(data)
        print(f"File saved successfully at {filepath}")


