import time
import random
import os

class Neuron:
    def __init__(self, threshold=1.0, leak=0.05, refractory_steps=1):
        self.threshold = threshold
        self.leak = leak
        self.refractory_steps = refractory_steps

        self.potential = 0.0
        self.refractory_left = 0
        self.fired_last_step = False
        self.total_spikes = 0

    def stimulate(self, input_signal: float) -> bool:
        """Return True if neuron fires this step."""
        self.fired_last_step = False

        # Refractory: cannot integrate input
        if self.refractory_left > 0:
            self.refractory_left -= 1
            return False

        # Leak toward 0
        if self.potential > 0:
            self.potential = max(0.0, self.potential - self.leak)

        # Integrate input
        self.potential += input_signal

        # Fire?
        if self.potential >= self.threshold:
            self.fired_last_step = True
            self.total_spikes += 1
            self.potential = 0.0
            self.refractory_left = self.refractory_steps
            return True

        return False


class NeuromorphicGridSim:
    def __init__(self, width=10, height=6, seed=None):
        if seed is not None:
            random.seed(seed)

        self.width = width
        self.height = height
        self.step_count = 0

        # Build grid of neurons with slight randomness
        self.grid = []
        for _y in range(height):
            row = []
            for _x in range(width):
                threshold = random.uniform(0.85, 1.25)
                leak = random.uniform(0.02, 0.08)
                refractory = random.choice([1, 1, 2])  # bias toward 1
                row.append(Neuron(threshold=threshold, leak=leak, refractory_steps=refractory))
            self.grid.append(row)

        # Simple “synapses”: spike from a cell nudges its neighbors next step
        self.neighbor_boost = 0.25

    def _neighbors(self, x, y):
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                yield nx, ny

    def step(self, base_input_min=0.0, base_input_max=0.45):
        self.step_count += 1

        # Base random input for all neurons
        inputs = [[random.uniform(base_input_min, base_input_max) for _ in range(self.width)]
                  for _ in range(self.height)]

        # If a neuron fired last step, boost its neighbors this step
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].fired_last_step:
                    for nx, ny in self._neighbors(x, y):
                        inputs[ny][nx] += self.neighbor_boost

        # Apply stimulation
        spikes_this_step = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x].stimulate(inputs[y][x]):
                    spikes_this_step += 1

        return spikes_this_step

    def render(self):
        # Clear screen (works in most terminals)
        os.system("cls" if os.name == "nt" else "clear")

        # Legend:
        # ⚡ fired this step
        # ▓ high potential
        # ▒ medium potential
        # ░ low potential
        # · near zero
        def cell_char(n: Neuron):
            if n.fired_last_step:
                return "⚡"
            p = n.potential / n.threshold if n.threshold > 0 else 0
            if p >= 0.75:
                return "▓"
            if p >= 0.50:
                return "▒"
            if p >= 0.25:
                return "░"
            return "·"

        print(f"🧠 Neuromorphic Grid  |  step={self.step_count}")
        print("Legend: ⚡=spike  ▓▒░=potential  ·=low\n")

        # Grid display
        for y in range(self.height):
            row = "".join(cell_char(self.grid[y][x]) for x in range(self.width))
            print(row)

        # Basic stats
        total_spikes = sum(n.total_spikes for row in self.grid for n in row)
        hottest = max((n.total_spikes for row in self.grid for n in row), default=0)
        print("\nStats:")
        print(f"  Total spikes: {total_spikes}")
        print(f"  Max spikes in a single neuron: {hottest}")
        print("\nTip: Ctrl+C to stop.")

    def run(self, steps=200, delay=0.25):
        try:
            for _ in range(steps):
                self.step()
                self.render()
                time.sleep(delay)
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    sim = NeuromorphicGridSim(width=16, height=8)
    sim.run(steps=500, delay=0.20)
