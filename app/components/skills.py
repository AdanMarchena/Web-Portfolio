import reflex as rx
from app.state import State, Skill
from app.styles import ELEVATION_1_SHADOW, ELEVATION_HOVER_SHADOW, RIPPLE_CLASS


def skill_card(skill: Skill) -> rx.Component:
    return rx.el.div(
        rx.icon(skill["icon"], size=28, class_name="text-orange-600 mb-3"),
        rx.el.p(skill["name"], class_name="font-semibold text-gray-700"),
        class_name=f"{RIPPLE_CLASS} flex flex-col items-center justify-center text-center p-6 bg-white rounded-xl transition-shadow duration-300",
        box_shadow=ELEVATION_1_SHADOW,
        _hover={"box_shadow": ELEVATION_HOVER_SHADOW},
    )


def skills_category(title: str, skills: rx.Var[list[Skill]]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="text-xl font-bold text-gray-800 mb-6 text-center md:text-left",
        ),
        rx.el.div(
            rx.foreach(skills, skill_card),
            class_name="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-5",
        ),
    )


def skills_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Skills",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-12 text-center",
            ),
            rx.el.div(
                skills_category("Technical Skills", State.technical_skills),
                skills_category("Data Science Skills", State.data_science_skills),
                #skills_category("Design Skills", State.design_skills),
                skills_category("Tools & Platforms", State.tools),
                class_name="space-y-12",
            ),
            class_name="container mx-auto px-4 md:px-8 py-16 md:py-24",
        ),
        id="skills",
        class_name="bg-white",
    )