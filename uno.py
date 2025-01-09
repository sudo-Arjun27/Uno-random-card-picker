import tkinter as tk
import random

# Define the UNO deck with rarities
cards = {
    "Common": ["Red 1", "Red 2", "Red 3", "Red 4", "Red 5", "Red 6", "Red 7", "Red 8", "Red 9",
               "Yellow 1", "Yellow 2", "Yellow 3", "Yellow 4", "Yellow 5", "Yellow 6", "Yellow 7", "Yellow 8", "Yellow 9",
               "Green 1", "Green 2", "Green 3", "Green 4", "Green 5", "Green 6", "Green 7", "Green 8", "Green 9",
               "Blue 1", "Blue 2", "Blue 3", "Blue 4", "Blue 5", "Blue 6", "Blue 7", "Blue 8", "Blue 9"],
    "Uncommon": ["Red Skip", "Red Draw Two", "Red Reverse",
                 "Yellow Skip", "Yellow Draw Two", "Yellow Reverse",
                 "Green Skip", "Green Draw Two", "Green Reverse",
                 "Blue Skip", "Blue Draw Two", "Blue Reverse"],
    "Rare": ["Wild", "Wild Draw Four"]
}

# Generate a full deck
def generate_deck():
    deck = []
    # Add common cards
    for card in cards["Common"]:
        deck.extend([card] * 2)
    deck.extend(["Red 0", "Yellow 0", "Green 0", "Blue 0"])  # Add zeros
    # Add uncommon cards
    for card in cards["Uncommon"]:
        deck.extend([card] * 2)
    # Add rare cards
    deck.extend(cards["Rare"] * 4)
    random.shuffle(deck)
    return deck

# Generate 4 arrays of 8 cards each
def generate_arrays():
    deck = generate_deck()
    arrays = [deck[i:i+8] for i in range(0, 32, 8)]
    return arrays

# Determine card rarity
def get_rarity(card):
    for rarity, card_list in cards.items():
        if card in card_list:
            return rarity
    return "Unknown"

# Display the arrays in the GUI
def display_arrays():
    arrays = generate_arrays()
    for widget in frame.winfo_children():  # Clear previous widgets
        widget.destroy()
    # Display each array with a graphical name
    for i, array in enumerate(arrays, start=1):
        # Add graphical name for the array
        title_label = tk.Label(frame, text=f"Array {i} 🎴", font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=5)
        # Add the array content with rarity
        result = ", ".join([f"{card} ({get_rarity(card)})" for card in array])
        content_label = tk.Label(frame, text=result, font=("Courier New", 12), wraplength=700, justify="left")
        content_label.pack(pady=5)

# Set up the GUI
root = tk.Tk()
root.title("UNO Card Generator")

# Create a frame to hold the arrays
frame = tk.Frame(root)
frame.pack(pady=20)

# Button to generate arrays
generate_button = tk.Button(root, text="Generate Card Arrays", command=display_arrays, font=("Arial", 14), bg="green", fg="white")
generate_button.pack(pady=10)

# Run the GUI
root.mainloop()
