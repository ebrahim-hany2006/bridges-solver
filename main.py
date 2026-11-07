from models.island import Island
from models.bridge import Bridge

from validators.degree_validator import (
    validate_degrees,
    is_solution_complete
)

a = Island(1, 0, 0, 2)
b = Island(2, 0, 5, 2)

bridges = [
    Bridge(a, b, 2)
]

print(validate_degrees([a, b], bridges))
print(is_solution_complete([a, b], bridges))
