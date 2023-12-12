import sys
import csv  # Import the CSV module
import time
import random
from datetime import datetime  # Import the datetime module
import os

# Add the parent directory to the Python path
sys.path.append('../..')

from topologies.network_topology import StarTopology

class TDMStar:
    def __init__(self, star_topology):
        self.star_topology = star_topology
        self.data = []  # Create an empty list to store simulation data

    def simulate_tdm(self):
        print("TDM star Simulation:")
        for user in self.star_topology.users:
            transmission_data = self.transmit_data(user)
            self.data.append(transmission_data)  # Store data for this transmission
            print(transmission_data)
            time.sleep(1)  # Sleep for 1 second between transmissions

    def transmit_data(self, user):
        # Simulate data transmission to a specific user and return the data with a timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_size = random.randint(100, 1000)
        start_time = time.time()
        # Simulate data transmission to a specific user
        data = f"{current_time}: User {user} is transmitting {data_size} units of data using TDM"
        time.sleep(0.5)  # Simulate transmission time
        end_time = time.time()
        transmission_time = end_time - start_time
        return (user, data_size, transmission_time, "Completed")

    def save_to_csv(self):
        try:
            # Define the directory path for the "simulation" folder within the "csv" folder
            directory = os.path.join("..", "src", "simulation")
            
            # Check if the directory exists, and create it if it doesn't
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Define the full file path
            filepath = os.path.join(directory, "tdm_star_simulation.csv")

            # Save the CSV file to the specified path
            with open(filepath, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["User", "Data Size (Units)", "Transmission Time (Seconds)", "Status"])
                for data in self.data:
                    csv_writer.writerow(data)
            
            print(f"File saved successfully at {filepath}")
        except Exception as e:
            print(f"An error occurred: {e}")