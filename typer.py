from pynput.keyboard import Controller
import time
import random

def human_typewrite(text):
    keyboard = Controller()
    for char in text:
        keyboard.type(char)
        time.sleep(random.uniform(0.02, 0.1))  # Adjusted delay for a moderate typing speed
    keyboard.press(' ')
    keyboard.release(' ')
    time.sleep(random.uniform(0.1, 0.1))  # Adjusted delay after pressing space

print("Starting typing after 10 seconds...")

script = """Add Text Here"""
start_time = time.time()
time.sleep(10)  # Wait for 10 seconds before typing

for word in script.split():
    human_typewrite(word)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
