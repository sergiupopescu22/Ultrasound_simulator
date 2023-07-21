import matplotlib.pyplot as plt
import numpy as np

def main():

    frequency = 1
    duration = 2
    time = np.linspace(0, duration, 300)

    signal1 = np.sin(2 * np.pi * frequency*time)

    # plt.figure(figsize=(10, 4))
    # plt.subplot(1, 2, 1)
    plt.plot(time,signal1,'o', markersize=2)
    plt.show()

    low_frequency = 5
    time2 = np.linspace(0, duration, duration * low_frequency)
    signal2 = np.sin(2 * np.pi*frequency*time2)

    # plt.subplot(1, 2, 2)
    # plt.plot(time2, signal2, 'o', markersize=2)
    # plt.show()





if __name__ == "__main__":
    main()