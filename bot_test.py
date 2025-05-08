import time
import random

def simulate_bot():
    for i in range(200):  # 200 "запросов"
        print(f"Request #{i}: {random.randint(1, 100)}")
        time.sleep(0.3)  # ~200 RPM

simulate_bot()