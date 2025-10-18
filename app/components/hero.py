import reflex as rx
from app.styles import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    FONT_FAMILY,
    contained_button_style,
    outlined_button_style,
    RIPPLE_CLASS,
)


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            class_name="absolute inset-0 bg-gradient-to-br from-orange-100/30 via-transparent to-gray-100/20"
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="/placeholder.svg",
                    alt="Profile Picture",
                    class_name="size-40 md:size-48 rounded-full object-cover border-4 border-white shadow-lg mx-auto mb-6",
                ),
                rx.el.h1(
                    "Your Name",
                    class_name="text-4xl md:text-5xl lg:text-6xl font-extrabold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "Creative Developer & UI/UX Enthusiast",
                    class_name=f"mt-4 text-lg md:text-xl text-center font-medium",
                    color=SECONDARY_COLOR,
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            "View Projects",
                            rx.icon("arrow_right", class_name="ml-2"),
                            style=contained_button_style,
                            class_name=RIPPLE_CLASS,
                        ),
                        href="#projects",
                    ),
                    rx.el.a(
                        rx.el.button(
                            "Contact Me",
                            rx.icon("mail", class_name="ml-2"),
                            style=outlined_button_style,
                            class_name=RIPPLE_CLASS,
                        ),
                        href="#contact",
                    ),
                    class_name="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4",
                ),
                class_name="relative z-10 w-full max-w-3xl",
            ),
            class_name="container mx-auto px-4 md:px-8 flex flex-col items-center justify-center min-h-[calc(100vh-80px)] text-center",
        ),
        id="home",
        position="relative",
        font_family=FONT_FAMILY,
    )