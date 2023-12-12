import csv
import random
import time
import os



class HybridTDMFDM:
    def __init__(self, star_topology, num_time_slots, num_frequency_bands):
        self.star_topology = star_topology
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
        for i, user in enumerate(self.star_topology.users):
            allocated_slot = self.hybrid_slots[i % len(self.hybrid_slots)]
            allocations[user] = allocated_slot
        return allocations

    def simulate_hybrid_transmission(self):
        print("Hybrid TDM-FDM Simulation:")
        results = []
        allocations = self.allocate_slots()
        for user, slot in allocations.items():
            data_size = random.randint(100, 1000)  # Simulate data sizes between 100 and 1000 units
            start_time = time.time()
            print(f"User {user} is transmitting {data_size} units of data in slot {slot}")
            time.sleep(0.5)  # Simulate transmission time
            end_time = time.time()
            transmission_time = end_time - start_time
            print(f"Transmission for User {user} in slot {slot} completed in {transmission_time:.2f} seconds.")
            results.append((user, data_size, transmission_time, "Completed"))
        self.save_results_to_csv(results)

    def save_results_to_csv(self, results):
        directory = os.path.join("..", "src", "simulation")
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, "hybrid_star_simulation.csv")

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["User", "Data Size (Units)", "Transmission Time (Seconds)", "Status"])
            for result in results:
                csv_writer.writerow(result)

