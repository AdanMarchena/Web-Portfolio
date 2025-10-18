import reflex as rx
from app.state import State
from app.styles import (
    ELEVATION_1_SHADOW,
    ELEVATION_HOVER_SHADOW,
    SECONDARY_COLOR,
    RIPPLE_CLASS,
)


def info_card(icon: str, text: str, subtext: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=24, class_name="text-orange-600"),
        rx.el.div(
            rx.el.p(text, class_name="font-semibold text-gray-800"),
            rx.el.p(subtext, class_name="text-sm text-gray-500"),
            class_name="ml-4",
        ),
        class_name=f"{RIPPLE_CLASS} flex items-center p-4 bg-white rounded-xl transition-shadow duration-300",
        box_shadow=ELEVATION_1_SHADOW,
        _hover={"box_shadow": ELEVATION_HOVER_SHADOW},
    )


def about_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "About Me",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-8 text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="/placeholder.svg",
                        alt="About Me Image",
                        class_name="rounded-2xl object-cover w-full h-full shadow-lg",
                    ),
                    class_name="lg:w-1/3 mb-8 lg:mb-0",
                ),
                rx.el.div(
                    rx.el.p(
                        State.about_me_text,
                        class_name=f"text-lg mb-8 leading-relaxed",
                        color=SECONDARY_COLOR,
                    ),
                    rx.el.div(
                        info_card("map_pin", "Location", "New York, USA"),
                        info_card("mail", "Email", "your.email@example.com"),
                        info_card("phone", "Phone", "+1 (234) 567-890"),
                        info_card("calendar", "Availability", "Open to Work"),
                        class_name="grid grid-cols-1 sm:grid-cols-2 gap-6",
                    ),
                    class_name="lg:w-2/3 lg:pl-12",
                ),
                class_name="flex flex-col lg:flex-row items-start",
            ),
            class_name="container mx-auto px-4 md:px-8 py-16 md:py-24",
        ),
        id="about",
        class_name="bg-gray-50",
    )