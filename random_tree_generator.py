import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to generate a random labeled tree
def generate_random_tree(num_nodes):
    if num_nodes <= 0:
        return None
    # Create a random tree using networkx
    G = nx.random_labeled_tree(num_nodes)
    return G

# Function to visualize the tree
def visualize_tree(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_color='black')
    plt.title('Random Labeled Tree')
    plt.show()

if __name__ == '__main__':
    num_nodes = random.randint(3, 20)  # Random number of nodes
    tree = generate_random_tree(num_nodes)
    visualize_tree(tree)
