def validate_degrees(islands, bridges):

    bridge_count = {island.id: 0 for island in islands}

    for bridge in bridges:
        bridge_count[bridge.island1.id] += bridge.count
        bridge_count[bridge.island2.id] += bridge.count

    for island in islands:
        if bridge_count[island.id] > island.degree:
            return False

    return True


def is_solution_complete(islands, bridges):

    bridge_count = {island.id: 0 for island in islands}

    for bridge in bridges:
        bridge_count[bridge.island1.id] += bridge.count
        bridge_count[bridge.island2.id] += bridge.count

    for island in islands:
        if bridge_count[island.id] != island.degree:
            return False

    return True