import csv
import random
import time
import os
from topologies.network_topology import BusTopology

class HybridTDMFDMBus:
    def __init__(self, bus_topology, num_time_slots, num_frequency_bands):
        self.bus_topology = bus_topology
        self.num_time_slots = num_time_slots
        self.num_frequency_bands = num_frequency_bands
        self.hybrid_slots = self.create_hybrid_slots()

    def create_hybrid_slots(self):
        hybrid_slots = []
        for t in range(self.num_time_slots):
            for f in range(self.num_frequency_bands):
                hybrid_slots.append(f"T{t}F{f}")
        return hybrid_slots

    def allocate_slots(self):
        allocations = {}
        # Assuming that the nodes are stored in the graph object of BusTopology
        for i, node in enumerate(self.bus_topology.graph.nodes()):
            if node != self.bus_topology.bus_node:  # Skip the bus node
                allocated_slot = self.hybrid_slots[i % len(self.hybrid_slots)]
                allocations[node] = allocated_slot
        return allocations

    def simulate_hybrid_transmission(self):
        print("Hybrid TDM-FDM Bus Simulation:")
        results = []
        allocations = self.allocate_slots()
        for node, slot in allocations.items():
            data_size = random.randint(100, 1000)
            start_time = time.time()
            print(f"Node {node} is transmitting {data_size} units of data in slot {slot}")
            time.sleep(0.5)  # Simulate transmission time
            end_time = time.time()
            transmission_time = end_time - start_time
            print(f"Transmission for Node {node} in slot {slot} completed in {transmission_time:.2f} seconds.")
            results.append((node, data_size, transmission_time, "Completed"))
        self.save_results_to_csv(results)

    def save_results_to_csv(self, results, filename='hybrid_bus_simulation.csv'):
        print('saving csv')
        directory = "simulation"  # Adjust the directory as needed
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Node", "Data Size (Units)", "Transmission Time (Seconds)", "Status"])
            for result in results:
                csv_writer.writerow(result)
