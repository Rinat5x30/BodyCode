from django import forms

_PARAM = {"class": "param-input__el"}


class QuizForm(forms.Form):
    gender = (
        ("male", "Мужчина"),
        ("female", "Женщина"),
    )

    traning_status = (
        ("yes", "Да"),
        ("no", "Нет"),
    )
    experience = (
        # training options
        ("lt1m", "< 1 месяца"),
        ("m1_3", "1-3 месяца"),
        ("m3_6", "3-6 месяцев"),
        ("gt6m", "> 6 месяцев"),
        # not_training options
        ("lt2w", "< 2 недель"),
        ("w2_4", "2-4 недели"),
        ("gt4w", "> 4 недель"),
    )

    goal = (
        ("cut", "Похудение"),
        ("bulk", "Набор массы"),
        ("maintenance", "Поддержание"),
    )

    injury = (
        ("spine_disc", "Протрузии / грыжа позвоночника"),
        ("hernia", "Паховая грыжа"),
        ("hernia", "Пупочная грыжа"),
        ("hernia", "Бедренная грыжа"),
        ("hernia", "Грыжа белой линии живота"),
        ("injury_knee", "Травма колена"),
        ("injury_elbow", "Травма локтя"),
        ("injury_shoulder", "Травма плеча"),
    )

    gender = forms.ChoiceField(
        label="Пол",
        choices=gender,
        widget=forms.RadioSelect,
    )

    age = forms.IntegerField(
        label="Возраст",
        min_value=12,
        max_value=90,
        widget=forms.NumberInput(
            attrs={**_PARAM, "placeholder": "28", "min": "12", "max": "90"}),
    )

    weight = forms.FloatField(
        label="Вес (кг)",
        min_value=36,
        max_value=250,
        widget=forms.NumberInput(
            attrs={**_PARAM, "placeholder": "75", "step": "0.1"}),
    )

    height = forms.FloatField(
        label="Рост (см)",
        min_value=148,
        max_value=220,
        widget=forms.NumberInput(
            attrs={**_PARAM, "placeholder": "178", "step": "0.1"}),
    )

    chest = forms.FloatField(
        label="Обхват груди (см)",
        min_value=60,
        max_value=180,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "60", "max": "180"}),
    )

    waist = forms.FloatField(
        label="Обхват талии (см)",
        min_value=40,
        max_value=180,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "40", "max": "180"}),
    )
    
    hips = forms.FloatField(
        label="Обхват бедер (см)",
        min_value=60,
        max_value=190,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "60", "max": "190"}),
    )

    thigh = forms.FloatField(
        label="Обхват бедра (см)",
        min_value=30,
        max_value=115,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "30", "max": "115"}),
    )

    calves = forms.FloatField(
        label="Обхват икры (см)",
        min_value=25,
        max_value=60,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "25", "max": "60"}),
    )

    biceps = forms.FloatField(
        label="Обхват бицепса (см)",
        min_value=20,
        max_value=70,
        widget=forms.NumberInput(attrs={**_PARAM, "step": "0.1", "min": "20", "max": "70"}),
    )

    training_now = forms.ChoiceField(
        label="Тренируется ли сейчас",
        choices=traning_status,
        widget=forms.RadioSelect,
    )

    training_period = forms.ChoiceField(
        label="Период тренировок / перерыва",
        choices=experience,
        widget=forms.RadioSelect,
    )

    goal = forms.ChoiceField(
        label="Цель", 
        choices=goal, 
        widget=forms.RadioSelect,
        )

    injury = forms.MultipleChoiceField(
        label="Противопоказания", 
        choices=injury, 
        required=False,
        widget=forms.CheckboxSelectMultiple,
        )
