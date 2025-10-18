import reflex as rx
from app.state import State, Experience
from app.styles import (
    ELEVATION_1_SHADOW,
    ELEVATION_HOVER_SHADOW,
    RIPPLE_CLASS,
    PRIMARY_COLOR,
)


def experience_card(exp: Experience, is_left: rx.Var[bool]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("briefcase", class_name="text-white"),
            class_name=f"absolute w-12 h-12 rounded-full flex items-center justify-center text-white left-1/2 -translate-x-1/2 bg-orange-600 ring-8 ring-gray-50",
        ),
        rx.el.div(
            rx.el.time(
                exp["date"],
                class_name="mb-1 text-sm font-normal leading-none text-gray-500",
            ),
            rx.el.h3(exp["title"], class_name="text-xl font-bold text-gray-900"),
            rx.el.p(
                exp["company"], class_name="text-md font-semibold text-orange-700 mb-2"
            ),
            rx.el.p(
                exp["description"], class_name="text-base font-normal text-gray-600"
            ),
            class_name=f"{RIPPLE_CLASS} p-6 bg-white rounded-xl transition-shadow duration-300 relative",
            box_shadow=ELEVATION_1_SHADOW,
            _hover={"box_shadow": ELEVATION_HOVER_SHADOW},
        ),
        class_name="mb-10 ml-16 md:ml-0",
    )


def experience_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Work Experience",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-12 text-center",
            ),
            rx.el.div(
                rx.foreach(
                    State.experience,
                    lambda exp, index: experience_card(exp, index % 2 == 0),
                ),
                class_name="relative border-l-4 border-orange-200 md:border-l-0 md:border-t-4 md:flex md:flex-col md:items-center",
            ),
            class_name="container mx-auto px-4 md:px-8 py-16 md:py-24",
        ),
        id="experience",
        class_name="bg-gray-50",
    )