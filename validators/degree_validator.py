def compute_degrees(islands: list, candidate_bridges: list, solution) -> dict:
    """
    بتحسب الدرجة الفعلية (actual degree) لكل جزيرة.
    تستقبل إما Solution object أو dict لخريطة bridge_counts أو قائمة Bridges قديمة.
    """
    actual_degrees = {island.id: 0 for island in islands}

    # التعامل مع الكباري المحددة في الـ solution
    if hasattr(solution, 'bridge_counts'):
        counts = solution.bridge_counts
    elif isinstance(solution, dict):
        counts = solution
    else:
        # التعامل التوافقي القديم لو مررت قائمة Bridge objects direct
        counts = {}
        for b in solution:
            b_id = getattr(b, 'id', None)
            if b_id:
                counts[b_id] = b.count
            else:
                actual_degrees[b.island1.id] += b.count
                actual_degrees[b.island2.id] += b.count
        if not counts and len(solution) > 0 and not hasattr(solution[0], 'island1'):
            counts = {}

    if counts:
        bridge_map = {b.id: b for b in candidate_bridges}
        for b_id, count in counts.items():
            if b_id in bridge_map:
                cb = bridge_map[b_id]
                actual_degrees[cb.from_island_id] += count
                actual_degrees[cb.to_island_id] += count

    return actual_degrees


def check_degrees(islands: list, candidate_bridges: list, solution, mode="partial") -> list:
    """
    بتفحص درجات الجزر وترجع قائمة degree_violations حسب الشكل المطلوب في DATA_MODEL.md:
    [{"island": "A", "required": 2, "actual": 1}]
    """
    actual_degrees = compute_degrees(islands, candidate_bridges, solution)
    violations = []

    # ترتيب الجزر افتراضياً: حسب الـ row ثم الـ col كما هو مذكور في التوثيق
    sorted_islands = sorted(islands, key=lambda isl: (isl.row, isl.col))

    for island in sorted_islands:
        actual = actual_degrees[island.id]
        required = island.required_bridges

        if mode == "partial":
            if actual > required:
                violations.append({
                    "island": island.id,
                    "required": required,
                    "actual": actual
                })
        elif mode == "final":
            if actual != required:
                violations.append({
                    "island": island.id,
                    "required": required,
                    "actual": actual
                })

    return violations


