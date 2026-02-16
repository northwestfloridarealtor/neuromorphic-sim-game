import time
import random

class Neuron:
    def __init__(self, threshold=1.0):
        self.potential = 0.0
        self.threshold = threshold

    def stimulate(self, input_signal):
        self.potential += input_signal
        if self.potential >= self.threshold:
            self.fire()

    def fire(self):
        print("⚡ Neuron fired!")
        self.potential = 0.0


class NeuromorphicSim:
    def __init__(self, neuron_count=5):
        self.neurons = [Neuron(random.uniform(0.8, 1.2)) for _ in range(neuron_count)]

    def step(self):
        print("\n🧠 Simulation step")
        for neuron in self.neurons:
            signal = random.uniform(0.0, 0.6)
            neuron.stimulate(signal)
            print(f"   potential={neuron.potential:.2f}")

    def run(self, steps=10, delay=1):
        for _ in range(steps):
            self.step()
            time.sleep(delay)


if __name__ == "__main__":
    sim = NeuromorphicSim(neuron_count=5)
    sim.run()
