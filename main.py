import streamlit as st
import random
import matplotlib.pyplot as plt

def generate_random_locations(grid_size_x, grid_size_y, num_agents):
  """
  Generates random (x, y) coordinates for a specified number of agents 
  within the defined grid dimensions.
  """
  locations = []
  for _ in range(num_agents):
    x = random.randint(0, grid_size_x - 1)
    y = random.randint(0, grid_size_y - 1)
    locations.append((x, y))
  return locations

st.title("Public Waiting Space Simulation")

# Get grid size and number of agents
grid_x = st.number_input("Grid Size (X-axis)", min_value=1)
grid_y = st.number_input("Grid Size (Y-axis)", min_value=1)
num_agents = st.number_input("Number of Agents", min_value=1)

# Button to generate the scatter plot
if st.button("Generate Agent Locations"):
  # Generate random locations for agents
  locations = generate_random_locations(grid_x, grid_y, num_agents)

  # Prepare data for scatter plot
  x_coordinates, y_coordinates = zip(*locations)

  plt.figure(figsize=(8, 6))
  plt.scatter(x_coordinates, y_coordinates, marker='o', color='b')
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.xlim(0, grid_x - 1)  # Set axis limits based on grid size
  plt.ylim(0, grid_y - 1)
  plt.title(f"Agent Locations (Grid Size: {grid_x}x{grid_y}, Agents: {num_agents})")
  plt.grid(True)
  plt.tight_layout()
  st.pyplot(plt)
  
  x = 0
  while(x < num_agents):
      st.write(f"Agent {x}: {x_coordinates[x]}, {y_coordinates[x]}")
      x+=1

# Note: This code generates random locations for agents. You can later replace it 
# with your actual logic for assigning specific locations.
