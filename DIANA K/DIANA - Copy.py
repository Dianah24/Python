
class PlasticBottle:
    def _init_(self, bottle_id, brand, type, volume):
        self.bottle_id = bottle_id
        self.brand = brand
        self.type = type
        self.volume = volume


class RecyclingCenter:
    def _init_(self, center_id, location, accepted_types):
        self.center_id = center_id
        self.location = location
        self.accepted_types = accepted_types
        self.collected_volume = 0.0

    def accept_bottle(self, bottle):
        if bottle.type in self.accepted_types:
            self.collected_volume += bottle.volume
            return True
        else:
            return False

    def display_info(self):
        print(f"Center ID: {self.center_id}, Location: {self.location},
         Accepted Types: {', '.join(self.accepted_types)},
          Collected Volume: {self.collected_volume} liters")


class CommunityPlasticBottleManager:
    def _init_(self):
        self.plastic_bottles = []
        self.recycling_centers = []

    def add_bottle(self, bottle):
        self.plastic_bottles.append(bottle)

    def remove_bottle(self, bottle):
        if bottle in self.plastic_bottles:
            self.plastic_bottles.remove(bottle)

    def add_recycling_center(self, center):
        self.recycling_centers.append(center)

    def remove_recycling_center(self, center):
        if center in self.recycling_centers:
            self.recycling_centers.remove(center)

    def display_bottles(self):
        print("Plastic Bottles in the Community:")
        for bottle in self.plastic_bottles:
            print(f"ID: {bottle.bottle_id}, Brand: {bottle.brand}, 
            Type: {bottle.type}, 
            Volume: {bottle.volume} liters")

    def display_recycling_centers(self):
        print("Recycling Centers in the Community:")
        for center in self.recycling_centers:
            center.display_info()


