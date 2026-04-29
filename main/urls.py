from django.urls import path

from .views import (
    quiz_view,
    animated_quiz_view,
    bench_press_guide_view,
    bench_press_source_open_view,
    bench_press_source_download_view,
)

app_name = "main"

urlpatterns = [
    path("", quiz_view, name="quiz"),
    path("animated/", animated_quiz_view, name="animated_quiz"),
    path("guides/bench-press/", bench_press_guide_view, name="guide_bench_press"),
    path(
        "guides/bench-press/source/open/",
        bench_press_source_open_view,
        name="guide_bench_press_source_open",
    ),
    path(
        "guides/bench-press/source/download/",
        bench_press_source_download_view,
        name="guide_bench_press_source_download",
    ),
]
