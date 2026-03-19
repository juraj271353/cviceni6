from matplotlib import pyplot as plt

def load_signal_from_txt(path):
    with open("ekg_signal.txt", "r") as file:
        signal = []
        for line in file:
            signal.append(float(line))

def signal_min(values):
    return min(values)

    print(signal)

    plt.plot(signal)
    plt.show()

