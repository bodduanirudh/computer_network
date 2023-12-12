import csv
import matplotlib.pyplot as plt
import os

# Function to read simulation data from a CSV file
def read_simulation_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            user, data_size, transmission_time, status = row
            data.append({
                "user": user,
                "data_size": int(data_size),
                "transmission_time": float(transmission_time),
                "status": status
            })
    return data

# Function to evaluate and compare TDM, FDM, and Hybrid
def evaluate_networks(tdm_data, fdm_data, hybrid_data):
    # Calculate average data size and transmission speed for each network
    def calculate_averages(data):
        total_data_size = sum(item['data_size'] for item in data)
        total_time = sum(item['transmission_time'] for item in data)
        average_data_size = total_data_size / len(data)
        average_speed = total_data_size / total_time if total_time > 0 else 0
        return average_data_size, average_speed

    tdm_avg_data_size, tdm_avg_speed = calculate_averages(tdm_data)
    fdm_avg_data_size, fdm_avg_speed = calculate_averages(fdm_data)
    hybrid_avg_data_size, hybrid_avg_speed = calculate_averages(hybrid_data)

    # Compare the networks based on the average data size and speed
    best_network = max(
        [('TDM', tdm_avg_speed), ('FDM', fdm_avg_speed), ('Hybrid', hybrid_avg_speed)],
        key=lambda x: x[1]
    )

    return {
        "TDM": {"Average Data Size": tdm_avg_data_size, "Average Speed": tdm_avg_speed},
        "FDM": {"Average Data Size": fdm_avg_data_size, "Average Speed": fdm_avg_speed},
        "Hybrid": {"Average Data Size": hybrid_avg_data_size, "Average Speed": hybrid_avg_speed},
        "Best Network": best_network[0]
    }

# Function to generate a plot for the evaluation results
def generate_plot(result, ax, title):
    networks = ['TDM', 'FDM', 'Hybrid']
    average_data_sizes = [
        result['TDM']['Average Data Size'],
        result['FDM']['Average Data Size'],
        result['Hybrid']['Average Data Size']
    ]
    average_speeds = [
        result['TDM']['Average Speed'],
        result['FDM']['Average Speed'],
        result['Hybrid']['Average Speed']
    ]

    ax.bar(networks, average_data_sizes, color='blue', alpha=0.6, label='Average Data Size')

    ax.set_ylabel('Average Data Size (Units)', color='blue')
    ax.tick_params(axis='y', labelcolor='blue')

    ax2 = ax.twinx()
    ax2.plot(networks, average_speeds, color='red', marker='o', label='Average Speed')
    ax2.set_ylabel('Average Speed (Units/Second)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    ax.set_title(title)
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    

def run_evaluation():
    # Filepaths for Star, Bus, Ring, Mesh, and Tree Topology simulations
    filenames = {
        "Star": {
            "tdm": '../simulation/tdm_star_simulation.csv',
            "fdm": '../simulation/fdm_star_simulation.csv',
            "hybrid": '../simulation/hybrid_star_simulation.csv'
        },
        "Bus": {
            "tdm": '../simulation/tdm_bus_simulation.csv',
            "fdm": '../simulation/fdm_bus_simulation.csv',
            "hybrid": '../simulation/hybrid_bus_simulation.csv'
        },
        "Ring": {
            "tdm": '../simulation/tdm_ring_simulation.csv',
            "fdm": '../simulation/fdm_ring_simulation.csv',
            "hybrid": '../simulation/hybrid_ring_simulation.csv'
        },
        "Mesh": {
            "tdm": '../simulation/tdm_mesh_simulation.csv',
            "fdm": '../simulation/fdm_mesh_simulation.csv',
            "hybrid": '../simulation/hybrid_mesh_simulation.csv'
        },
        "Tree": {
            "tdm": '../simulation/tdm_tree_simulation.csv',
            "fdm": '../simulation/fdm_tree_simulation.csv',
            "hybrid": '../simulation/hybrid_tree_simulation.csv'
        }
    }

    results = {}

    # Read and evaluate data for each topology
    for topology in filenames:
        tdm_data = read_simulation_data(filenames[topology]["tdm"])
        fdm_data = read_simulation_data(filenames[topology]["fdm"])
        hybrid_data = read_simulation_data(filenames[topology]["hybrid"])
        results[topology] = evaluate_networks(tdm_data, fdm_data, hybrid_data)
        print(f"\n{topology} Topology Evaluation Results:")
        for key, value in results[topology].items():
            print(f"{key}: {value}")

   # Plotting
    fig, axs = plt.subplots(2, 3, figsize=(24, 12), constrained_layout=True)  # 2 rows, 3 columns

    # Assuming results have been calculated and stored in 'results' dict
    topologies = ["Star", "Bus", "Ring", "Mesh", "Tree"]
    for i, topology in enumerate(topologies):
        # Determine the position of the current plot
        row = i // 3
        col = i % 3
        ax = axs[row, col]
        generate_plot(results[topology], ax, f"{topology} Topology")
        
        # Hide the last (empty) subplot if there is an odd number of topologies
        if i == len(topologies):
            fig.delaxes(axs[row, col+1])

    plt.show()


# Main function call
if __name__ == "__main__":
    run_evaluation()
