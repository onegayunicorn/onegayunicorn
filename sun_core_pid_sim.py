import numpy as np

class SunCorePID:
    def __init__(self, kp=1.2, ki=0.05, kd=0.8, target=0.85):
        self.target = target
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0
        self.history = []

    def step(self, current_stability: float, dt: float = 0.1) -> float:
        error = self.target - current_stability
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        correction = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        
        new_stability = min(max(current_stability + correction, 0.0), 1.0)
        self.history.append(new_stability)
        return new_stability

def main():
    sim = SunCorePID()
    state = 0.0054  # Initial stability index from BP-01
    print(f"Starting Mechanical Sun Core PID Simulation...")
    print(f"Initial Stability: {state:.4f}")
    
    for i in range(100):
        state = sim.step(state)
        if i % 10 == 0:
            print(f"Step {i}: Stability = {state:.4f}")
            
    print(f"✅ Final Stability Index: {state:.4f} (Target: 0.85)")

if __name__ == "__main__":
    main()
