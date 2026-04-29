from __future__ import annotations

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

from pathlib import Path
import re

from .forms import QuizForm
from .program_generator import generate_program


def quiz_view(request):
    program = None
    form = QuizForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        program = generate_program(form.cleaned_data)

    return render(
        request,
        "main/quiz.html",
        {
            "form": form,
            "program": program,
        },
    )


def animated_quiz_view(request):
    program = None
    form = QuizForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        program = generate_program(form.cleaned_data)

    return render(
        request,
        "main/animated_quiz.html",
        {
            "form": form,
            "program": program,
        },
    )


_WEEK_RE = re.compile(r"^\s*(\d+)\s+НЕДЕЛЯ\s*[—-]\s*(.+?)\s*$", re.IGNORECASE)
_DAY_RE = re.compile(r"^\s*(Пн|Вт|Ср|Чт|Пт|Сб|Вс)\s*:\s*$", re.IGNORECASE)


def _parse_bench_guide(text: str) -> dict:
    lines = [ln.strip() for ln in (text or "").splitlines()]
    lines = [ln for ln in lines if ln]

    intro: list[str] = []
    legend: list[str] = []
    weeks: list[dict] = []

    # Intro/legend: everything before the first "N НЕДЕЛЯ"
    first_week_idx = None
    for i, ln in enumerate(lines):
        if _WEEK_RE.match(ln):
            first_week_idx = i
            break

    head = lines if first_week_idx is None else lines[:first_week_idx]
    if head:
        # Try to split intro vs legend around "Обозначения"
        legend_start = None
        for i, ln in enumerate(head):
            if ln.lower().startswith("обозначения"):
                legend_start = i
                break
        if legend_start is None:
            intro = head
        else:
            intro = head[:legend_start]
            legend = head[legend_start:]

    current_week = None
    current_day = None

    def flush_day():
        nonlocal current_day, current_week
        if current_week is None or current_day is None:
            return
        current_week["days"].append(current_day)
        current_day = None

    def flush_week():
        nonlocal current_week, current_day
        if current_week is None:
            return
        flush_day()
        weeks.append(current_week)
        current_week = None

    tail = [] if first_week_idx is None else lines[first_week_idx:]
    for ln in tail:
        m = _WEEK_RE.match(ln)
        if m:
            flush_week()
            num = int(m.group(1))
            title = m.group(2).strip()
            current_week = {"num": num, "title": title, "days": []}
            continue

        m = _DAY_RE.match(ln)
        if m and current_week is not None:
            flush_day()
            current_day = {"name": m.group(1).capitalize(), "items": []}
            continue

        if current_week is None:
            # Stray content before first week (shouldn't happen)
            continue
        if current_day is None:
            # Content in a week before first day label
            current_day = {"name": "", "items": []}
        current_day["items"].append(ln)

    flush_week()
    return {"intro": intro, "legend": legend, "weeks": weeks}


def bench_press_guide_view(request):
    guide_text_path = Path(__file__).resolve().parent / "guides" / "bench_press_guide_ru.txt"
    guide_text = ""
    if guide_text_path.exists():
        guide_text = guide_text_path.read_text(encoding="utf-8", errors="replace")
    guide = _parse_bench_guide(guide_text)

    return render(
        request,
        "main/guide_bench_press.html",
        {"guide": guide},
    )


def _resolve_sw_band_program_file() -> Path:
    base_dir = Path(settings.BASE_DIR)
    candidates = [
        base_dir / "main" / "static" / "main" / "guides" / "sw_band_program.pdf",
        base_dir / "main" / "static" / "main" / "guides" / "sw_band_program.docx",
        base_dir / "[SW.BAND] Программа.docx",
    ]
    for file_path in candidates:
        if file_path.exists() and file_path.is_file():
            return file_path
    raise Http404("Файл программы не найден")


def _program_content_type(file_path: Path) -> str:
    if file_path.suffix.lower() == ".pdf":
        return "application/pdf"
    if file_path.suffix.lower() == ".docx":
        return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    return "application/octet-stream"


def bench_press_source_open_view(request):
    file_path = _resolve_sw_band_program_file()
    return FileResponse(
        file_path.open("rb"),
        content_type=_program_content_type(file_path),
        as_attachment=False,
        filename=file_path.name,
    )


def bench_press_source_download_view(request):
    file_path = _resolve_sw_band_program_file()
    return FileResponse(
        file_path.open("rb"),
        content_type=_program_content_type(file_path),
        as_attachment=True,
        filename=file_path.name,
    )
