import random
import numpy as np
from crazyserv import Arena


class PackageGenerator:
    def __init__(self):
        self.coordinate_pool = self.define_coordinate_pool()
        self.pool_size = self.coordinate_pool.shape[0]
        self.package_weight = 3
        self.rng = {}

    def define_coordinate_pool(self):
        arena = Arena(0)
        z = arena.min_z
        return np.array([
            [2.6, 0.6, z],
            [2.4, 3.4, z],
            [0.6, 2.2, z],
            [1.4, 3.2, z],
            [1., 1.6, z],
            [3.6, 0.6, z],
            [3.2, 3.2, z],
            [3.4, 1.4, z]
        ])

    def initialize_swarm(self, swarm_id, seed):
        self.rng[swarm_id] = random.Random()
        self.rng[swarm_id].seed(seed)
        return True

    def generate_number(self, swarm_id, lower_limit, upper_limit):
        if (swarm_id in self.rng):
            return self.rng[swarm_id].randint(lower_limit, upper_limit)

    def get_package(self, swarm_id):
        rand = self.generate_number(swarm_id, 0, self.pool_size - 1)
        weight = self.generate_number(swarm_id, 1, self.package_weight)
        x = self.coordinate_pool[rand].tolist()[0]
        y = self.coordinate_pool[rand].tolist()[1]
        return {'id': swarm_id + '-' + x + '-' + y, 'coordinates': self.coordinate_pool[rand].tolist(), 'weight': weight}
