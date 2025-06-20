"""
Build Your Own Database – Minimal Key-Value Store
Author: Ihunna Amugo | Build-Your-Own-X Series

💾 Goal:
Build a simple database using a Python class that supports:
- Create, Read, Update, Delete operations (CRUD)
- Persistence via JSON files
- In-memory dictionary for fast lookup

🩺 Healthcare Parallel:
This could store perfusion readings from a digital twin simulation, or track model outputs (e.g., risk scores) over time.

This is the foundation of model tracking systems, patient state databases, or tiny EHR prototypes.
"""

import json
import os

class SimpleDatabase:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        """Load database from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        """Save current state to disk"""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)

    def create(self, key, value):
        if key in self.data:
            raise ValueError("Key already exists.")
        self.data[key] = value
        self.save()

    def read(self, key):
        return self.data.get(key, "Key not found.")

    def update(self, key, value):
        if key not in self.data:
            raise ValueError("Key not found.")
        self.data[key] = value
        self.save()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()
        else:
            raise ValueError("Key not found.")

    def list_keys(self):
        return list(self.data.keys())

# Example Usage
if __name__ == "__main__":
    db = SimpleDatabase()

    print("Welcome to Ihunna's DB! Simulating digital twin outputs...\n")

    db.create("brain_R1", {"perfusion": 48, "oxygen": 90, "risk_score": 0.35})
    db.create("brain_R2", {"perfusion": 22, "oxygen": 75, "risk_score": 0.92})  # high risk

    print("Current keys:", db.list_keys())
    print("Read R2:", db.read("brain_R2"))

    db.update("brain_R1", {"perfusion": 51, "oxygen": 92, "risk_score": 0.25})
    db.delete("brain_R2")
    print("Updated R1:", db.read("brain_R1"))
