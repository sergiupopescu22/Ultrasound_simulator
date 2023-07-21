import numpy as np
import matplotlib.pyplot as plt
import sys

# A Scan --> 2000 esantioane, fiecare a 12 biti ( intre -90 si +90, 4096 esantioane)

material_thickness = 0.01
speed_of_sound = 3000
listening_time = 2 * material_thickness / speed_of_sound
samples = 2000
echo_frequency = 5e6  # 5MHz

def plot_scan_signal(time, signal):
    plt.figure()
    plt.plot(time, signal,'o', markersize=2, linestyle='-')
    plt.xlabel('Time (2000 samples)')
    plt.ylabel('Amplitude')
    plt.title('Ultrasound A Scan')
    plt.grid(True)


def create_echo_wave():
    echo_layer_frequency = echo_frequency
    echo_layer_amplitude = 1
    echo_layer_time = np.linspace(0, listening_time / 22, int(samples / 22))
    echo_layer_wave = echo_layer_amplitude * np.sin(2 * np.pi * echo_layer_frequency * echo_layer_time)
    return echo_layer_wave
def add_echos_to_A_scan(AScan):
    echo_layer_wave = create_echo_wave()
    echo_layer_waves = [echo_layer_wave] * 4

    length_echo = len(echo_layer_wave)
    waves_location = [100, 1000, 1500, 1800]
    waves_amplitude = [6, 4, 3, 6]
    counter = 0
    for wave in echo_layer_waves:
        wave = wave * waves_amplitude[counter]

        pad_width = (waves_location[counter], samples - waves_location[counter] - length_echo)
        wave = np.pad(wave, pad_width, mode='constant')

        AScan = AScan + wave
        counter += 1

    return AScan

def plot_B_Scan(BScan):

    plt.figure(figsize=(5, 6))
    rotated_image = np.rot90(BScan, k=-1)
    plt.imshow(rotated_image, cmap='gray', aspect='auto')
    plt.xlabel('A Scans')
    plt.ylabel('ToF')
    plt.title('Ultrasound B Scan')
    plt.grid(True)


def main():
    print("Hello world!")

    amplitude = 0.2
    samples_times = np.linspace(0, listening_time, samples)
    AScan = amplitude * np.sin(2 * np.pi * echo_frequency * samples_times)
    # baseAScan[30] = baseAScan[30] + 10
    # plot_scan_signal(samples_times, baseAScan)

    add_echos_to_A_scan(AScan)
    AScan = add_echos_to_A_scan(AScan)
    plot_scan_signal(samples_times, AScan)

    BScan = [AScan] * 128
    plot_B_Scan(BScan)

    plt.show()

if __name__ == "__main__":
    main()
