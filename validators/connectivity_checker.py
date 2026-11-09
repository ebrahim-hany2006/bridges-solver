from models.solution import Solution

def find_connected_components(islands: list, candidate_bridges: list, solution) -> list:
    """
    تحسب المكونات المتصلة (Connected Components) بناءً على الجسور الفعلية التي عددها > 0.
    ترجع قائمة من المكونات، وكل مكون عبارة عن قائمة island ids، مرتبة بشكل قياسي.
    """
    # استخراج الـ bridge_counts من الـ solution object أو الـ dict
    if hasattr(solution, 'bridge_counts'):
        counts = solution.bridge_counts
    elif isinstance(solution, dict):
        counts = solution
    else:
        counts = {}

    # بناء Adjacency List للجزر
    adj = {island.id: [] for island in islands}
    bridge_map = {b.id: b for b in candidate_bridges}

    for b_id, count in counts.items():
        if count > 0 and b_id in bridge_map:
            cb = bridge_map[b_id]
            u = cb.from_island_id
            v = cb.to_island_id
            # إضافة الاتصال في الاتجاهين ( undirected graph )
            if v not in adj[u]:
                adj[u].append(v)
            if u not in adj[v]:
                adj[v].append(u)

    visited = set()
    components = []

    # ترتيب الجزر افتراضياً حسب row ثم col لضمان حتمية الترتيب (deterministic)
    sorted_islands = sorted(islands, key=lambda isl: (isl.row, isl.col))

    for island in sorted_islands:
        island_id = island.id
        if island_id not in visited:
            # تنفيذ BFS أو DFS لإيجاد كل الجزر المتصلة بهذا المكون
            component = []
            queue = [island_id]
            visited.add(island_id)

            while queue:
                curr = queue.pop(0)
                component.append(curr)

                for neighbor in adj.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            # ترتيب عناصر المكون داخلياً لتكون ثابتة
            component.sort()
            components.append(component)

    return components


def is_connected(islands: list, candidate_bridges: list, solution) -> bool:
    """
    ترجع True لو الشبكة كلها مكوّن واحد متصل (connected_components == 1)، وترجع False غير ذلك.
    """
    if not islands:
        return True
    
    components = find_connected_components(islands, candidate_bridges, solution)
    return len(components) == 1