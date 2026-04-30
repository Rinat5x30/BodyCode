from django.test import TestCase

from main.program_generator import (
    apply_contra_filters,
    get_available_exercises_for_group,
    generate_program,
    exercise_list,
    knee_injury_keywords,
    shoulder_injury_keywords,
)


class ContraFilterTests(TestCase):
    def test_shoulder_injury_excludes_bench_press_and_takes_next(self):
        """При травме плеча жим лёжа исключается, следующее подходящее берётся вместо него."""
        result = get_available_exercises_for_group("грудь", ["injury_shoulder"], count=1)
        self.assertNotIn("Жим штанги лежа", result)
        self.assertEqual(result, ["Жим штанги на наклонной скамье"])

    def test_shoulder_injury_fills_up_to_count_with_next_suitable(self):
        """При count=2 и одном запрещённом упражнении функция добирает до count из оставшихся."""
        result = get_available_exercises_for_group("грудь", ["injury_shoulder"], count=2)
        self.assertNotIn("Жим штанги лежа", result)
        self.assertEqual(len(result), 2)
        self.assertIn("Жим штанги на наклонной скамье", result)
        self.assertIn("Сведение рук", result)

    def test_knee_injury_quad_group_has_no_forbidden_exercises(self):
        """При травме колена из квадрицепсов исключаются все запрещённые упражнения."""
        all_count = len(exercise_list["квадрицепсы"])
        result = get_available_exercises_for_group("квадрицепсы", ["injury_knee"], count=all_count)
        self.assertNotIn("Приседания со штангой", result)
        self.assertNotIn("Выпады с гантелями", result)
        self.assertNotIn("Разгибание ног", result)
        for ex in result:
            ex_l = ex.lower()
            self.assertFalse(
                any(k in ex_l for k in knee_injury_keywords),
                msg=f"Запрещённое упражнение попало в результат: '{ex}'",
            )

    def test_generated_program_contains_no_forbidden_exercises(self):
        """Сгенерированная программа не содержит упражнений, запрещённых по противопоказаниям."""
        data = {
            "gender": "male",
            "age": 25,
            "weight": 80.0,
            "height": 180.0,
            "chest": 100.0,
            "waist": 80.0,
            "hips": 95.0,
            "thigh": 55.0,
            "calves": 38.0,
            "biceps": 35.0,
            "training_status": "training",
            "training_experience": "gt6m",
            "goal": "maintain",
            "contraindications": ["injury_shoulder"],
        }
        program = generate_program(data)
        forbidden_found = []
        for day in program["exercises_by_day"]:
            for ex in day["exercises"]:
                ex_l = ex["name"].lower()
                if any(k in ex_l for k in shoulder_injury_keywords):
                    forbidden_found.append(ex["name"])
        self.assertListEqual(
            forbidden_found,
            [],
            msg=f"Программа содержит запрещённые упражнения: {forbidden_found}",
        )
