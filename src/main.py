# Import your StarTopology class from the relevant module
# Assuming the StarTopology class is defined in the network_topology.py within the topologies folder

from topologies.network_topology import StarTopology,BusTopology,RingTopology,MeshTopology,TreeTopology


from tdm.tdm_star import TDMStar
from tdm.tdm_bus import TDMBus
from tdm.tdm_ring import TDMRing
from tdm.tdm_mesh import TDMMesh
from tdm.tdm_tree import TDMTree

from fdm.fdm_star import FDMStar
from fdm.fdm_bus import FDMBus
from fdm.fdm_ring import FDMRing
from fdm.fdm_mesh import FDMMesh
from fdm.fdm_tree import FDMTree

from hybrid.hybrid_star import HybridTDMFDM
from hybrid.hybrid_bus import HybridTDMFDMBus
from hybrid.hybrid_ring import HybridTDMFDMRing
from hybrid.hybrid_mesh import HybridTDMFDMMesh
from hybrid.hybrid_tee import HybridTDMFDMTree

def main():
    # Instantiate the star topology with the desired number of users
    star_topology = StarTopology(num_users=10)
    # Create the star topology
    star_topology.create_star_topology()
    # Simulate the network
    star_topology.simulate_network()
    # Draw the network topology
    star_topology.draw_topology()

    # Instantiate the bus topology
    bus_topology = BusTopology()
    # Add nodes to the bus topology
    for i in range(10):
        bus_topology.add_node(f'Node{i}')
    # Display the bus topology
    bus_topology.display()

    # Instantiate the ring topology with the desired number of nodes
    ring_topology = RingTopology(num_nodes=10)
    # Create the ring topology
    ring_topology.create_ring_topology()
    # Simulate the network
    ring_topology.simulate_network()
    # Draw the network topology
    ring_topology.draw_topology()

    # Instantiate the mesh topology with the desired number of nodes
    mesh_topology = MeshTopology(num_nodes=10)
    # Create the mesh topology
    mesh_topology.create_mesh_topology()
    # Simulate the network
    mesh_topology.simulate_network()
    # Draw the network topology
    mesh_topology.draw_topology()

    # Tree Topology
    tree_topology = TreeTopology(num_levels=3, branching_factor=2)
    tree_topology.create_tree_topology()
    tree_topology.simulate_network()
    tree_topology.draw_topology()

 


    # Set up the ring topology and run the TDM simulation
    print("Running TDM ring network simulation...")
    ring_topology = RingTopology(num_nodes=10)
    tdm_ring = TDMRing(ring_topology)
    tdm_ring.simulate_tdm()
    tdm_ring.save_to_csv()

    # Run the TDM star network simulation
    print("Running TDM star network simulation...")
    # Now, set up and run the TDM simulation
    tdm = TDMStar(star_topology)
    tdm.simulate_tdm()
    tdm.save_to_csv() 

    # Run the TDM bus network simulation
    print("Running TDM bus network simulation...")
    tdm_bus = TDMBus(bus_topology)
    tdm_bus.simulate_tdm()
    tdm_bus.save_to_csv()

    # Set up the mesh topology and run the TDM simulation
    print("Running TDM mesh network simulation...")
    mesh_topology = MeshTopology(num_nodes=10)
    tdm_mesh = TDMMesh(mesh_topology)
    tdm_mesh.simulate_tdm()
    tdm_mesh.save_to_csv()

    # Set up the tree topology and run the TDM simulation
    print("Running TDM tree network simulation...")
    tree_topology = TreeTopology(num_levels=3, branching_factor=2)
    tree_topology.create_tree_topology()
    tdm_tree = TDMTree(tree_topology)
    tdm_tree.simulate_tdm()
    tdm_tree.save_to_csv()
   



    # Set up and run the FDM simulation for the star topology
    print("Running FDM star network simulation...")
    star_topology = StarTopology(num_users=10)  # Example setup
    fdm_star = FDMStar(star_topology)
    fdm_star.simulate_fdm()
    fdm_star.save_to_csv()

    # Set up and run the FDM simulation for the bus topology
    print("Running FDM bus network simulation...")
    bus_topology = BusTopology()
    # Add nodes to the bus topology
    for i in range(10):
        bus_topology.add_node(f'Node{i+1}')
    fdm_bus = FDMBus(bus_topology)
    fdm_bus.simulate_fdm()
    fdm_bus.save_to_csv()

    # Set up and run the FDM simulation for the ring topology
    print("Running FDM ring network simulation...")
    ring_topology = RingTopology(num_nodes=10)
    fdm_ring = FDMRing(ring_topology)
    fdm_ring.simulate_fdm()
    fdm_ring.save_to_csv()

    # Set up and run the FDM simulation for the mesh topology
    print("Running FDM mesh network simulation...")
    mesh_topology = MeshTopology(num_nodes=10)
    fdm_mesh = FDMMesh(mesh_topology)
    fdm_mesh.simulate_fdm()
    fdm_mesh.save_to_csv()

    # Set up the tree topology and run the FDM simulation
    print("Running FDM tree network simulation...")
    tree_topology = TreeTopology(num_levels=3, branching_factor=2)
    tree_topology.create_tree_topology()
    fdm_tree = FDMTree(tree_topology)
    fdm_tree.simulate_fdm()
    fdm_tree.save_to_csv()





    # set up and run the hybrid simulation of star 
    print("Running Hybrid TDM-FDM network simulation...")
    hybrid = HybridTDMFDM(star_topology, num_time_slots=5, num_frequency_bands=5)
    hybrid.simulate_hybrid_transmission()

    # Set up and run the hybrid TDM-FDM simulation for the bus topology
    print("Running Hybrid TDM-FDM bus network simulation...")
    bus_topology = BusTopology()
    # Add nodes to the bus topology
    for i in range(10):
        bus_topology.add_node(f'Node{i+1}')
    hybrid_bus = HybridTDMFDMBus(bus_topology, num_time_slots=5, num_frequency_bands=2)
    hybrid_bus.simulate_hybrid_transmission()

    # Set up and run the hybrid TDM-FDM simulation for the ring topology
    print("Running Hybrid TDM-FDM ring network simulation...")
    ring_topology = RingTopology(num_nodes=10)
    hybrid_ring = HybridTDMFDMRing(ring_topology, num_time_slots=5, num_frequency_bands=2)
    hybrid_ring.simulate_hybrid_transmission()

    # Set up and run the hybrid TDM-FDM simulation for the mesh topology
    print("Running Hybrid TDM-FDM mesh network simulation...")
    mesh_topology = MeshTopology(num_nodes=10)
    hybrid_mesh = HybridTDMFDMMesh(mesh_topology, num_time_slots=5, num_frequency_bands=2)
    hybrid_mesh.simulate_hybrid_transmission()

    # Set up the tree topology and run the hybrid TDM-FDM simulation
    print("Running Hybrid TDM-FDM tree network simulation...")
    tree_topology = TreeTopology(num_levels=3, branching_factor=2)
    tree_topology.create_tree_topology()
    hybrid_tree = HybridTDMFDMTree(tree_topology, num_time_slots=5, num_frequency_bands=2)
    hybrid_tree.simulate_hybrid_transmission()

if __name__ == "__main__":
    main()
