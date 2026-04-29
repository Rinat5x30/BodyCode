from dataclasses import dataclass, field

beginner_muscles = ["грудь", "спина", "квадрицепсы", "средняя дельта"]
fanat_only = ["бицепс", "трицепс", "пресс", "верх груди", "бицепс бедра"]
pro_only = ["передняя дельта", "задняя дельта", "икры", "приводящая ноги"]
legend_only = ["предплечья", "низ груди"]

exercise_list = {
    "грудь": ["Жим штанги лежа", "Жим штанги на наклонной скамье", "Сведение рук"],
    "спина": ["Тяга верхнего блока", "Тяга гантели в наклоне", "Горизонтальная тяга"],
    "квадрицепсы": ["Приседания со штангой", "Выпады с гантелями", "Разгибания ног"],
    "бицепс бедра": ["Сгибания ног лежа", "Румынская тяга"],
    "средняя дельта": ["Тяга к подбородку с EZ-грифом", "Махи гантелями в стороны"],
    "бицепс": ["Подъем гантелей на бицепс", "Подъем EZ-грифа на бицепс"],
    "трицепс": ["Разгибание рук на блоке", "Французский жим гантели сидя"],
    "пресс": ["Скручивания", "Подъем ног в висе"],
    "передняя дельта": ["Жим гантелей сидя", "Подъем гантелей перед собой"],
    "задняя дельта": ["Обратные разведения в тренажере", "Махи в наклоне"],
    "предплечья": ["Сгибание кистей", "Разгибание кистей"],
    "ягодицы": ["Ягодичный мост", "Разведение ног в тренажере"],
    "икры": ["Подъемы на носки стоя", "Подъемы на носки сидя"],
}

hernia_keywords = ("приседания", "выпады", "румынская тяга", "ягодичный мост", "скручивания", "подъем ног в висе")
back_keywords = ("присед", "румынская", "тяга штанги в наклоне")
baza_keywords = ("станов", "присед", "штанг")
knee_injury_keywords = ("присед", "выпад", "разгибание ног")
shoulder_injury_keywords = ("жим штанги лежа", "махи гантелями", "тяга к подбородку", "жим гантелей сидя")
elbow_exclude_keywords = ("французский жим",)

experience_to_level = {"lt1m": "beginner", "m1_3": "fanat", "m3_6": "pro", "gt6m": "legend"}
pause_to_level = {"lt2w": "pro", "w2_4": "fanat", "gt4w": "beginner"}
level_load = {"beginner": (2, "10-15"), "fanat": (2, "10-15"), "pro": (3, "8-12"), "legend": (3, "8-12")}

level_duration = {"beginner": 3, "fanat": 4, "pro": 4, "legend": 4}

# Кол-во упражнений на мышечную группу в зависимости от уровня
GROUP_COUNT: dict[str, dict[str, int]] = {
    "beginner": {
        "грудь": 1, "спина": 1, "квадрицепсы": 1, "средняя дельта": 1,
    },
    "fanat": {
        "грудь": 2, "спина": 2, "квадрицепсы": 2,
        "бицепс бедра": 1, "бицепс": 1, "трицепс": 1, "пресс": 1, "средняя дельта": 1,
    },
    "pro": {
        "грудь": 2, "спина": 2, "квадрицепсы": 2,
        "бицепс бедра": 2, "бицепс": 2, "трицепс": 2, "средняя дельта": 1,
        "передняя дельта": 1, "задняя дельта": 1, "икры": 1,
    },
    "legend": {
        "грудь": 3, "спина": 3, "квадрицепсы": 3,
        "бицепс бедра": 2, "бицепс": 2, "трицепс": 2, "средняя дельта": 1, "предплечья": 2,
        "передняя дельта": 1, "задняя дельта": 1, "икры": 1,
    },
}
# Переопределение числа подходов для конкретных групп (если отличается от level_load)
GROUP_SETS: dict[str, dict[str, int]] = {
    "fanat": {
        "грудь": 2, "спина": 2, "квадрицепсы": 2,
        "бицепс бедра": 2, "бицепс": 2, "трицепс": 2, "пресс": 2, "средняя дельта": 2,
    },
}

goal_cardio = {
    "bulk": "Отсутствие кардио",
    "cut": "20-30 минут кардио 3-4 раза в неделю",
    "maintain": "5-10 минут лёгкого кардио",
}
week_plans = {
    "Фулбади": [
        {"day": "День 1 (Пн)", "focus": "Фулбади"},
        {"day": "День 2 (Чт)", "focus": "Фулбади"},
    ],
    "Тяни-толкай": [
        {"day": "День 1 (Пн)", "focus": "Тяни/Толкай (чередование)"},
        {"day": "День 2 (Ср)", "focus": "Толкай/Тяни (чередование)"},
        {"day": "День 3 (Пт)", "focus": "Тяни/Толкай (чередование)"},
    ],
    "Верх-низ": [
        {"day": "День 1 (Пн)", "focus": "Низ + ягодицы"},
        {"day": "День 2 (Ср)", "focus": "Верх"},
        {"day": "День 3 (Пт)", "focus": "Низ + ягодицы"},
    ],
    "Тяни-толкай-ноги": [
        {"day": "День 1 (Пн)", "focus": "Тяни"},
        {"day": "День 2 (Ср)", "focus": "Толкай"},
        {"day": "День 3 (Пт)", "focus": "Ноги"},
    ],
}
bro_split = [
    {"day": "День 1 (Пн)", "focus": "Грудь+бицепс"},
    {"day": "День 2 (Вт)", "focus": "Спина+трицепс"},
    {"day": "День 3 (Ср)", "focus": "Ноги+плечи"},
]


@dataclass
class QuizProfile:
    gender: str
    age: int
    weight: float
    height: float
    chest: float
    waist: float
    hips: float
    thigh: float
    calves: float
    biceps: float
    training_status: str
    training_experience: str | None = None
    training_pause: str | None = None
    goal: str = ""
    contraindications: list[str] = field(default_factory=list)


def normalize_profile_data(cleaned_data: dict) -> dict:
    data = dict(cleaned_data)

    # Support both old and new field names from forms.
    if "training_status" not in data:
        training_now = data.get("training_now")
        if training_now == "yes":
            data["training_status"] = "training"
        elif training_now == "no":
            data["training_status"] = "not_training"

    status = data.get("training_status")
    period = data.get("training_period")
    if status == "training":
        if "training_experience" not in data:
            data["training_experience"] = period if period in {"lt1m", "m1_3", "m3_6", "gt6m"} else None
        data.setdefault("training_pause", None)
    elif status == "not_training":
        if "training_pause" not in data:
            data["training_pause"] = period if period in {"lt2w", "w2_4", "gt4w"} else None
        data.setdefault("training_experience", None)

    # Form field `injury` may be one or many values; engine expects a flat list.
    if "contraindications" not in data:
        injury = data.get("injury")
        if isinstance(injury, list):
            data["contraindications"] = [i for i in injury if i]
        else:
            data["contraindications"] = [injury] if injury else []
    elif isinstance(data["contraindications"], str):
        data["contraindications"] = [data["contraindications"]]

    data.pop("injury", None)
    data.pop("training_now", None)
    data.pop("training_period", None)

    return data


def calculate_bmi(weight: float, height_cm: float) -> float:
    return round(weight / ((height_cm / 100) ** 2), 1)


def resolve_level(profile: QuizProfile) -> str:
    if profile.gender == "female":
        if profile.training_status == "training":
            return "beginner" if profile.training_experience == "lt1m" else "pro"
        if profile.training_status == "not_training":
            return "pro" if profile.training_pause == "lt2w" else "beginner"

    if profile.training_status == "training":
        return experience_to_level.get(profile.training_experience)
    if profile.training_status == "not_training":
        return pause_to_level.get(profile.training_pause)


def resolve_program_type(profile: QuizProfile, level: str) -> str:
    if level == "beginner":
        return "Фулбади"
    if profile.gender == "female":
        return "Верх-низ"
    return {"fanat": "Тяни-толкай", "pro": "Тяни-толкай-ноги"}.get(level, "Бро-сплит")


def circumference_focus(profile: QuizProfile, level: str) -> dict:
    if level == "beginner":
        return {"weakest": [], "add_sets": {}}

    is_female = profile.gender == "female"
    chest_ref = profile.hips * (0.97 if is_female else 1.0)
    calves_ref = profile.thigh * 0.6
    hips_ref = profile.waist * (1.25 if is_female else 1.1)
    thigh_ref = profile.hips * 0.58
    biceps_ref = profile.chest * (0.34 if is_female else 0.36)

    weakest = []
    add_sets = {}

    if profile.chest < chest_ref:
        weakest.append("грудь")
        add_sets["грудь"] = add_sets.get("грудь", 0) + 1
        add_sets["спина"] = add_sets.get("спина", 0) + 1

    if profile.calves < calves_ref:
        weakest.append("икры")
        if level not in ("beginner", "fanat"):
            add_sets["икры"] = add_sets.get("икры", 0) + 1

    if profile.hips < hips_ref:
        weakest.append("бедра")
        if is_female:
            add_sets["ягодицы"] = add_sets.get("ягодицы", 0) + 1

    if profile.thigh < thigh_ref:
        weakest.append("бедро")
        add_sets["бицепс бедра"] = add_sets.get("бицепс бедра", 0) + 1
        add_sets["квадрицепсы"] = add_sets.get("квадрицепсы", 0) + 1

    if profile.biceps < biceps_ref:
        weakest.append("бицепс")
        add_sets["бицепс"] = add_sets.get("бицепс", 0) + 1
        add_sets["трицепс"] = add_sets.get("трицепс", 0) + 1

    return {"weakest": sorted(set(weakest)), "add_sets": add_sets}


def build_muscle_groups(level: str) -> list[str]:
    groups = beginner_muscles.copy()
    if level in ("fanat", "pro", "legend"):
        groups += fanat_only
    if level in ("pro", "legend"):
        groups += pro_only
    if level == "legend":
        groups += legend_only
    return groups


def apply_contra_filters(exercises: list[str], contraindications: list[str]) -> list[str]:
    if not contraindications:
        return exercises

    selected_contra = set(contraindications)
    has_hernia = "hernia" in selected_contra
    has_spine_disc = "spine_disc" in selected_contra
    filtered = []
    for exercise in exercises:
        ex = exercise.lower()
        if has_hernia and (any(k in ex for k in hernia_keywords) or any(k in ex for k in baza_keywords)):
            continue
        if has_spine_disc and any(k in ex for k in back_keywords):
            continue
        if "injury_knee" in selected_contra and any(k in ex for k in knee_injury_keywords):
            continue
        if "injury_shoulder" in selected_contra and any(k in ex for k in shoulder_injury_keywords):
            continue
        if "injury_elbow" in selected_contra and any(k in ex for k in elbow_exclude_keywords):
            continue
        filtered.append(exercise)
    return filtered


def get_available_exercises_for_group(group: str, contraindications: list[str], count: int = 2) -> list[str]:
    return apply_contra_filters(exercise_list.get(group, []), contraindications)[:count]


def resolve_load(profile: QuizProfile, level: str, bmi: float) -> dict:
    sets, reps = level_load.get(level, (2, "10-15"))

    if profile.training_status == "not_training" and profile.training_pause == "w2_4":
        sets = max(2, sets - 1)

    cardio = goal_cardio.get(profile.goal, "10-15 минут после силовой")
    axial_load = (
        "Замените приседания со штангой на жим ногами, становую тягу — на тягу в наклоне или в блоке"
        if bmi >= 25 else None
    )

    if profile.age >= 40 and sets > 2:
        sets = sets - 1

    return {"sets": sets, "reps": reps, "cardio": cardio, "axial_load": axial_load}


def build_week_plan(program_type: str, gender: str) -> list[dict]:
    return week_plans.get(program_type, bro_split)


def pick_exercises_for_day(
    focus: str,
    groups: list[str],
    contraindications: list[str],
    level: str,
    base_sets: int = 3,
    base_reps: str = "10-15",
    add_sets: dict[str, int] | None = None,
) -> list[dict]:
    focus_l = focus.lower()

    # Бро-сплит: точные совпадения идут первыми, иначе "ног" поглощает "Ноги+плечи"
    if focus_l == "грудь+бицепс":
        requested_groups = ["грудь", "бицепс", "предплечья"]
    elif focus_l == "спина+трицепс":
        requested_groups = ["спина", "трицепс", "пресс"]
    elif focus_l == "ноги+плечи":
        requested_groups = ["квадрицепсы", "бицепс бедра", "икры", "средняя дельта", "передняя дельта", "задняя дельта"]
    elif focus_l == "тяни":
        # Тяни-толкай-ноги: есть отдельный день ног
        requested_groups = ["спина", "бицепс", "средняя дельта", "задняя дельта"]
    elif focus_l == "толкай":
        # Тяни-толкай-ноги: есть отдельный день ног
        requested_groups = ["грудь", "трицепс", "передняя дельта", "пресс"]
    elif focus_l.startswith("тяни"):
        # Тяни/Толкай (чередование) — фанат, нет отдельного дня ног
        requested_groups = ["спина", "бицепс", "средняя дельта", "задняя дельта", "бицепс бедра"]
    elif focus_l.startswith("толкай"):
        # Толкай/Тяни (чередование) — фанат, нет отдельного дня ног
        requested_groups = ["грудь", "трицепс", "передняя дельта", "пресс", "квадрицепсы"]
    elif "ног" in focus_l or "низ" in focus_l:
        requested_groups = ["квадрицепсы", "бицепс бедра", "ягодицы", "икры", "пресс"]
    elif "груд" in focus_l:
        requested_groups = ["грудь", "трицепс"]
    elif "спина" in focus_l:
        requested_groups = ["спина", "бицепс", "задняя дельта"]
    elif "плеч" in focus_l:
        requested_groups = ["средняя дельта", "передняя дельта", "задняя дельта", "предплечья"]
    else:
        requested_groups = [g for g in groups if g in beginner_muscles]

    selected_groups = [g for g in requested_groups if g in groups]
    level_counts = GROUP_COUNT.get(level, {})
    group_sets_table = GROUP_SETS.get(level, {})
    result = []

    for group in selected_groups:
        count = min(level_counts.get(group, 1), 1 if group == "икры" else 999)
        names = get_available_exercises_for_group(group, contraindications, count=count)
        group_base = group_sets_table.get(group, base_sets)
        extra = (add_sets.get(group, 0) if add_sets else 0)
        for i, name in enumerate(names):
            sets = group_base + (extra if i == 0 else 0)
            result.append({"name": name, "sets": sets, "reps": base_reps})

    return result


def generate_program(cleaned_data: dict) -> dict:
    normalized_data = normalize_profile_data(cleaned_data)
    profile = QuizProfile(**normalized_data)
    bmi = calculate_bmi(profile.weight, profile.height)
    level = resolve_level(profile)
    program_type = resolve_program_type(profile, level)
    load = resolve_load(profile, level, bmi)
    focus = circumference_focus(profile, level)
    groups = build_muscle_groups(level)
    week_plan = build_week_plan(program_type, profile.gender)

    exercises_by_day = []
    for day in week_plan:
        day_exercises = pick_exercises_for_day(
            day["focus"],
            groups,
            profile.contraindications,
            level,
            base_sets=load["sets"],
            base_reps=load["reps"],
            add_sets=focus.get("add_sets"),
        )
        exercises_by_day.append({"day": day["day"], "focus": day["focus"], "exercises": day_exercises})

    duration_weeks = level_duration.get(level, 4)

    recommendations = []
    if bmi < 18.5:
        recommendations.append("Недостаток веса: сфокусируйтесь на наборе силы и умеренном профиците калорий. Кардио сводите к минимуму.")
    elif bmi >= 25:
        recommendations.append("Избыток веса: увеличьте кардио нагрузку сверх базовой программы и контролируйте дефицит калорий. Снизьте осевую нагрузку на позвоночник.")
    else:
        recommendations.append("Сохраняйте стабильный режим питания и восстановления.")

    if focus["weakest"]:
        recommendations.append(f"Отстающие зоны для акцента: {', '.join(focus['weakest'])}.")

    training_period = normalized_data.get("training_period")
    if profile.training_status == "not_training" and training_period == "w2_4":
        recommendations.append("Первые 1-2 недели после перерыва держите нагрузку ниже обычной.")
    if profile.training_status == "not_training" and training_period == "gt1m":
        recommendations.append("После длительного перерыва начинайте как новичок и увеличивайте объем постепенно.")

    return {
        "bmi": bmi,
        "level": level,
        "program_type": program_type,
        "duration_weeks": duration_weeks,
        "sets": load["sets"],
        "reps": load["reps"],
        "cardio": load["cardio"],
        "week_plan": week_plan,
        "exercises_by_day": exercises_by_day,
        "recommendations": recommendations,
        "focus": focus,
        "contraindications": profile.contraindications,
    }
