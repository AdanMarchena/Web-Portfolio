import reflex as rx
from app.state import State
from app.components.navigation import navigation_bar
from app.components.hero import hero_section
from app.components.about import about_section
from app.components.skills import skills_section
from app.components.experience import experience_section
from app.components.projects import projects_section
from app.components.contact import contact_section
from app.components.footer import footer_section
from app.styles import BACKGROUND_COLOR, FONT_FAMILY


def index() -> rx.Component:
    return rx.el.div(
        navigation_bar(),
        rx.el.main(
            hero_section(),
            about_section(),
            skills_section(),
            experience_section(),
            projects_section(),
            contact_section(),
        ),
        footer_section(),
        style={"background_color": BACKGROUND_COLOR, "font_family": FONT_FAMILY},
        class_name="scroll-smooth",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin="anonymous"
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)