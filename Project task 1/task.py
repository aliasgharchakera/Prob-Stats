def plot_frequency_histogram(filename):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in filename:
        num = alphabet.find(i) + 1
        print(num)

plot_frequency_histogram("BRUHHH")