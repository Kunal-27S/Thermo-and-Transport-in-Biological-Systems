import numpy as np
import matplotlib.pyplot as plt

def simulate_t6ss(size=100, steps=200, kill_rate=0.05, repro_rate=0.05):
    # Initialize lattice: 1 for Red, 2 for Blue, 0 for Empty
    lattice = np.random.choice([1, 2], size=(size, size))
    
    # Track cooperator frequency over time
    freq_history = []

    for step in range(steps):
        # 1. Killing Phase: 5% of cells activate T6SS
        kill_indices = np.where(lattice > 0)
        num_to_kill = int(len(kill_indices[0]) * kill_rate)
        selected = np.random.choice(len(kill_indices[0]), num_to_kill, replace=False)
        
        for idx in selected:
            r, c = kill_indices[0][idx], kill_indices[1][idx]
            attacker = lattice[r, c]
            # Check 8 neighbors (Moore neighborhood)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = (r + dr) % size, (c + dc) % size
                    if lattice[nr, nc] != 0 and lattice[nr, nc] != attacker:
                        lattice[nr, nc] = 0 # Killed: cell becomes empty

        # 2. Reproduction Phase: 5% of cells try to reproduce
        repro_indices = np.where(lattice > 0)
        num_to_repro = int(len(repro_indices[0]) * repro_rate)
        selected_repro = np.random.choice(len(repro_indices[0]), num_to_repro, replace=False)
        
        for idx in selected_repro:
            r, c = repro_indices[0][idx], repro_indices[1][idx]
            parent = lattice[r, c]
            # Find empty neighbors
            empty_neighbors = []
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = (r + dr) % size, (c + dc) % size
                    if lattice[nr, nc] == 0:
                        empty_neighbors.append((nr, nc))
            
            if empty_neighbors:
                target_r, target_c = empty_neighbors[np.random.choice(len(empty_neighbors))]
                lattice[target_r, target_c] = parent

        freq_history.append(np.mean(lattice == 1))

    return lattice, freq_history

# Run and Plot
final_grid, history = simulate_t6ss()

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(final_grid, cmap='bwr') # Blue-White-Red
plt.title("Final Spatial Distribution (Phase Separation)")
plt.subplot(1, 2, 2)
plt.plot(history)
plt.title("Cooperator Frequency Over Time")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.show()