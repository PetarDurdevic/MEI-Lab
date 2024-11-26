import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

def load_ground_truth(image_path):
    """
    Load the ground truth image and convert it to a matrix of dielectric properties.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Could not find or open the file: {image_path}")
    
    # Normalize image to represent dielectric properties (1.0 - 10.0 range as an example)
    dielectric_map = 1.0 + (image / 255.0) * 9.0
    return dielectric_map

def simulate_gpr(dielectric_map, antenna_position):
    """
    Simulate the radar signal at a specific antenna position.
    """
    x = antenna_position
    signal = np.zeros(dielectric_map.shape[0])
    for depth in range(dielectric_map.shape[0]):
        # Simulate signal intensity based on dielectric contrast
        signal[depth] = dielectric_map[depth, x]
    
    # Normalize signal
    signal = signal / np.max(signal)
    return signal

def update(frame, dielectric_map, antenna_position, ax1, ax2, line):
    """
    Update function for the real-time simulation.
    """
    ax1.clear()
    ax1.imshow(dielectric_map, cmap='gray', aspect='auto')
    ax1.set_title("Ground Truth Dielectric Map")
    ax1.axvline(x=antenna_position[0], color='r', linestyle='--', label="Radar Position")
    ax1.legend()
    
    # Simulate GPR signal
    signal = simulate_gpr(dielectric_map, antenna_position[0])
    
    ax2.clear()
    ax2.plot(signal, np.arange(len(signal)), label="Radar Signal")
    ax2.invert_yaxis()
    ax2.set_title("Simulated Radar Signal")
    ax2.set_xlabel("Signal Intensity")
    ax2.set_ylabel("Depth")
    ax2.legend()
    
    # Move antenna position
    antenna_position[0] = (antenna_position[0] + 1) % dielectric_map.shape[1]
    line.set_ydata(signal)

def main(image_path):
    # Load ground truth and initialize variables
    dielectric_map = load_ground_truth(image_path)
    antenna_position = [0]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Initial plot
    ax1.imshow(dielectric_map, cmap='gray', aspect='auto')
    ax1.set_title("Ground Truth Dielectric Map")
    ax1.axvline(x=antenna_position[0], color='r', linestyle='--', label="Radar Position")
    ax1.legend()
    
    signal = simulate_gpr(dielectric_map, antenna_position[0])
    line, = ax2.plot(signal, np.arange(len(signal)))
    ax2.invert_yaxis()
    ax2.set_title("Simulated Radar Signal")
    ax2.set_xlabel("Signal Intensity")
    ax2.set_ylabel("Depth")
    
    # Animation for real-time simulation
    ani = FuncAnimation(
        fig, 
        update, 
        frames=range(dielectric_map.shape[1]), 
        fargs=(dielectric_map, antenna_position, ax1, ax2, line), 
        interval=100
    )
    
    plt.tight_layout()
    plt.show()

# if __name__ == "__main__":
#     image_path = input("Enter the path to the ground truth PNG file: ")
#     main(image_path)
image_path = input("/home/petar/GitHub/Radar/radar_fixed.png")
image_path = os.path.abspath(image_path)
main(image_path)