from models.solution import Solution
from validators.degree_validator import check_degrees
from validators.connectivity_checker import find_connected_components

def validate_solution(islands: list, candidate_bridges: list, solution) -> dict:
    """
    الحَكَم الوحيد على صحة حل لغز الـ Hashiwokakero.
    يتحقق من:
    1. صحة القيم (0, 1, 2) ومطابقة الـ IDs.
    2. درجات الجزر بنمط final (check_degrees).
    3. التقاطعات بين الجسور (crossings - يتم دمجها أو عمل stub لها).
    4. اتصال الشبكة بالكامل في مكون واحد (find_connected_components).
    ويُرجع تقريراً شاملاً يحتوي على كل المخالفات دفعة واحدة.
    """
    # استخراج الـ bridge_counts من الـ solution object أو الـ dict
    if hasattr(solution, 'bridge_counts'):
        counts = solution.bridge_counts
    elif isinstance(solution, dict):
        counts = solution
    else:
        counts = {}

    valid_bridge_ids = {b.id for b in candidate_bridges}
    invalid_values = []
    normalized_counts = {}

    # 1. التحقق من صحة القيم والـ IDs
    for b_id, val in counts.items():
        if b_id not in valid_bridge_ids:
            invalid_values.append(b_id)
        elif val not in [0, 1, 2]:
            invalid_values.append(b_id)
        else:
            normalized_counts[b_id] = val

    # تجهيز كائن Solution موحد للاستخدام
    sol_obj = Solution(normalized_counts)

    # 2. فحص الدرجات (Degree Violations) بنمط final
    degree_violations = check_degrees(islands, candidate_bridges, sol_obj, mode="final")

    # 3. فحص التقاطعات (Crossings) - استدعاء لو متوفرة أو stub فارغ لحين تكامل S1-05
    # crossings = []
    # try:
    #     from validators.crossing_detector import detect_crossings
    #     crossings = detect_crossings(candidate_bridges, sol_obj)
    # except ImportError:
    #     pass  # في حال عدم وجود ملف التقاطعات بعد، يتم تركه فارغاً

    # 4. فحص الاتصال (Connectivity Check)
    components = find_connected_components(islands, candidate_bridges, sol_obj)
    connected_components_count = len(components)

    # 5. تحديد هل الحل صحيح بالكامل؟
    # يجب ألا توجد أي أخطاء في القيم، ولا درجات خاطئة، ولا تقاطعات، وأن تكون الشبكة مكوناً واحداً فقط.
    is_valid = (
        len(invalid_values) == 0 and
        len(degree_violations) == 0 and
        # len(crossings) == 0 and
        connected_components_count == 1
    )

    return {
        "valid": is_valid,
        "degree_violations": degree_violations,
        # "crossings": crossings,
        "connected_components": connected_components_count,
        "invalid_values": invalid_values
    }