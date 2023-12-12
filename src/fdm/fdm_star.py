import sys
import csv
import time
from datetime import datetime
import random  # Import random for simulating data sizes
import os

# Add the parent directory to the Python path
sys.path.append('../..')

from topologies.network_topology import StarTopology

class FDMStar:
    def __init__(self, star_topology):
        self.star_topology = star_topology
        self.data = []  # Create an empty list to store simulation data

    def simulate_fdm(self):
        print("FDM star Simulation:")
        for user in self.star_topology.users:
            transmission_data = self.transmit_data(user)
            self.data.append(transmission_data)
            print(transmission_data)
            time.sleep(1)  # Sleep for 1 second between transmissions

    def transmit_data(self, user):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_size = random.randint(100, 1000)  # Simulating data sizes
        start_time = time.time()
        data = f"{current_time}: User {user} is transmitting {data_size} units of data using FDM"
        time.sleep(0.5)  # Simulate transmission time
        end_time = time.time()
        transmission_time = end_time - start_time
        return (user, data_size, transmission_time, "Completed")

    def save_to_csv(self):
            # Define the directory path for the "simulation" folder within the "csv" folder
            directory = os.path.join("..", "src", "simulation")
            
            # Check if the directory exists, and create it if it doesn't
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Define the full file path
            filename = os.path.join(directory, "fdm_star_simulation.csv")

            # Save the CSV file to the specified path
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["User", "Data Size (Units)", "Transmission Time (Seconds)", "Status"])
                for data in self.data:
                    csv_writer.writerow(data)