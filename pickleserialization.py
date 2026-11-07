import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_info(self):
        return f"{self.name} is level {self.level}"

player = Player("ShadowWizard", 42)

# Write (Serialize) custom object to binary file ('wb')
with open("player_save.pkl", "wb") as f:
    pickle.dump(player, f)

# Read (Deserialize) binary stream back into a live Python object ('rb')
with open("player_save.pkl", "rb") as f:
    restored_player = pickle.load(f)

print(restored_player.get_info())