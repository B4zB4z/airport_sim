import time
import random
from max_heap import MaxHeap
from random_event import RandomEvents

class Airport:
    def __init__(self):
        self.landing_heap = MaxHeap()  # Priority queue for landing planes
        self.takeoff_queue = []  # Planes on the ground waiting to take off
        self.planes_in_air = {}  # Tracks planes in the air (in the landing queue)
        self.planes_on_ground = {}  # Tracks planes on the ground (waiting for takeoff)
        self.plane_id_counter = 0
        self.random_events = RandomEvents()

        # Initialize the airport with 10 planes on the ground and 5 planes in the air wanting to land
        self.initialize_airport()

    def initialize_airport(self):
        # Add 10 planes on the ground
        for _ in range(10):
            self.add_plane_on_ground()
        
        # Add 5 planes in the air, requesting to land
        for _ in range(5):
            self.add_plane_in_air()

    def add_plane_in_air(self):
        # Adds a plane to the landing queue (in the air)
        self.plane_id_counter += 1
        plane_id = f"Plane{self.plane_id_counter}"

        priority = 5  # Default priority for landing planes
        event = self.random_events.random_event()

        if event == "emergency":
            priority += 2
            print(f"[NEW EMERGENCY] {plane_id} is requesting a landing, due to an emergency!")
        elif event == "severe_emergency":
            priority += 5
            print(f"[NEW SEVERE EMERGENCY] {plane_id} is requesting a landing, due to a severe emergency!")
        else:
            print(f"[NEW] {plane_id} is requesting a landing!")

        self.planes_in_air[plane_id] = priority
        self.landing_heap.add((priority, plane_id))  # Add plane to heap with priority

    def add_plane_on_ground(self):
        # Adds a plane to the takeoff queue (on the ground)
        self.plane_id_counter += 1
        plane_id = f"Plane{self.plane_id_counter}"
        self.planes_on_ground[plane_id] = 1  # Ground planes have a fixed low priority
        self.takeoff_queue.append(plane_id)
        print(f"[NEW] {plane_id} is requesting takeoff.")

    def allow_landing_or_takeoff(self):
        # Prioritize landing if there are planes waiting to land
        if not self.landing_heap.is_empty():
            priority, plane_id = self.landing_heap.get_max()
            if plane_id in self.planes_in_air:
                del self.planes_in_air[plane_id]
            print(f"[LANDING] {plane_id} has landed successfully (Priority was {priority}).")
        elif self.takeoff_queue:
            # If no landing planes, takeoff the first plane in the queue
            plane_id = self.takeoff_queue.pop(0)
            if plane_id in self.planes_on_ground:
                del self.planes_on_ground[plane_id]
            print(f"[TAKEOFF] {plane_id} has taken off.")
        else:
            print("[IDLE] No planes waiting to land or take off.")

    def simulate(self, steps, delay):
        for step in range(steps):
            print(f"\n--- Step {step+1} ---")
            
            # Randomly decide whether to add a new plane to the landing queue (no new planes on the ground)
            action = random.choice(["new_plane_in_air", "nothing"])  # No more planes are added to the ground automatically
            
            if action == "new_plane_in_air":
                self.add_plane_in_air()  # Adds a random plane to the air
            else:
                print("[EVENT] No new planes this step.")
            
            # Allow planes to land or take off based on priority
            self.allow_landing_or_takeoff()
            
            time.sleep(delay)  # Optional delay between steps for simulation effect
