from dataclasses import dataclass


#@dataclass(unsafe_hash=True)
@dataclass(order=True)
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str = "Item"
    unit_price: float = 0
    quantity_on_hand: int = 0

    @property
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    #def __str__(self):
    #    return "{}: {}, {}".format(self.name, self.unit_price, self.quantity_on_hand)

if __name__ == "__main__":
    sensors = InventoryItem()
    print(sensors)
    print(sensors.total_cost)
