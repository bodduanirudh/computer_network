
import csv
import time
from datetime import datetime
import random  # Import random for simulating data sizes
import os

class FDMBus:
    def __init__(self, bus_topology):
        self.bus_topology = bus_topology
        self.data = []  # Create an empty list to store simulation data

    def simulate_fdm(self):
        print("FDM Bus Simulation:")
        # Assuming that the nodes are stored in the graph object of BusTopology
        for node in self.bus_topology.graph.nodes():
            if node != self.bus_topology.bus_node:  # Skip the bus node
                transmission_data = self.transmit_data(node)
                self.data.append(transmission_data)
                print(transmission_data)
                time.sleep(1)  # Sleep for 1 second between transmissions

    def transmit_data(self, node):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_size = random.randint(100, 1000)  # Simulating data sizes
        start_time = time.time()
        data = f"{current_time}: Node {node} is transmitting {data_size} units of data using FDM"
        time.sleep(0.5)  # Simulate transmission time
        end_time = time.time()
        transmission_time = end_time - start_time
        return (node, data_size, transmission_time, "Completed")

    def save_to_csv(self, filename='fdm_bus_simulation.csv'):
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



