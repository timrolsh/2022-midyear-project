from Field import Field
from City import City


class UnionFind:
    """
    Implements the classic union find data structure to quickly determine whether two cities are connected. 
    """

    def __init__(self):
        self.cities_list = Field.cities.keys()
        self.city_indices = {city: i for i,
                                         city in enumerate(self.cities_list)}
        self.city_components = [i for i in range(len(self.cities_list))]
        self.component_sizes = [1 for i in range(len(self.cities_list))]

    def find(self, component: int):
        if component < 0 or component >= len(self.city_components):
            raise Exception("Component in 'find' function out of range")
        while component != self.city_components[component]:
            component = self.city_components[component]
        return component

    def is_connected(self, city1: City, city2: City):
        city1_component = self.city_indices[city1.name]
        city2_component = self.city_indices[city2.name]
        return self.find(city1_component) == self.find(city2_component)

    def connect_cities(self, city1: City, city2: City):
        city1_root = self.find(self.city_indices[city1.name])
        city2_root = self.find(self.city_indices[city2.name])
        if city1_root == city2_root:
            return
        if self.component_sizes[city1_root] < self.component_sizes[city2_root]:
            self.city_components[city1_root] = city2_root
            self.component_sizes[city2_root] += self.component_sizes[city1_root]
        else:
            self.city_components[city2_root] = city1_root
            self.component_sizes[city1_root] += self.component_sizes[city2_root]
