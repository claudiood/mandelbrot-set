import numpy as np
import matplotlib.pyplot as plt
import subprocess

def main():
    process = subprocess.run(["go", "run", "mandelbrot.go"], capture_output=True, text=True)
    go_output = process.stdout

    lines = go_output.strip().split('\n')
    data = []
    for line in lines:
        row = [int(val) for val in line.split()]
        data.append(row)

    mandelbrot_array = np.array(data)

    plt.figure(figsize=(12,8))
    plt.imshow(mandelbrot_array, cmap='viridis')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()