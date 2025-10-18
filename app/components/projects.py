import reflex as rx
from app.state import State, Project
from app.styles import (
    ELEVATION_1_SHADOW,
    ELEVATION_HOVER_SHADOW,
    RIPPLE_CLASS,
    PRIMARY_COLOR,
    SURFACE_COLOR,
)


def project_tag(tag: str) -> rx.Component:
    return rx.el.span(
        tag,
        class_name="text-xs font-semibold text-orange-800 bg-orange-100 px-2.5 py-1 rounded-full",
    )


def project_card(project: Project) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=project["image"],
            alt=project["name"],
            class_name="rounded-t-xl h-48 w-full object-cover",
        ),
        rx.el.div(
            rx.el.h3(
                project["name"], class_name="font-bold text-lg text-gray-800 mb-2"
            ),
            rx.el.p(
                project["description"], class_name="text-sm text-gray-600 mb-4 h-16"
            ),
            rx.el.div(
                rx.foreach(project["tags"], project_tag),
                class_name="flex flex-wrap gap-2",
            ),
            class_name="p-5",
        ),
        class_name=f"{RIPPLE_CLASS} bg-white rounded-xl overflow-hidden transition-shadow duration-300",
        box_shadow=ELEVATION_1_SHADOW,
        _hover={"box_shadow": ELEVATION_HOVER_SHADOW},
    )


def filter_button(category: str) -> rx.Component:
    is_active = State.active_filter == category
    return rx.el.button(
        category,
        on_click=lambda: State.set_filter(category),
        class_name=rx.cond(
            is_active,
            f"px-4 py-2 rounded-full font-semibold text-white bg-orange-600 shadow-md",
            f"px-4 py-2 rounded-full font-semibold text-gray-600 bg-gray-200 hover:bg-gray-300",
        ),
    )


def projects_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Projects",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-8 text-center",
            ),
            rx.el.div(
                rx.foreach(["All", "Web", "Mobile", "Design"], filter_button),
                class_name="flex justify-center gap-4 mb-12",
            ),
            rx.el.div(
                rx.foreach(State.filtered_projects, project_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 md:px-8 py-16 md:py-24",
        ),
        id="projects",
        class_name="bg-white",
    )