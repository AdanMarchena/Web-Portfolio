import reflex as rx
from app.styles import SECONDARY_COLOR


def social_link(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon,
            size=24,
            class_name="text-gray-500 hover:text-orange-600 transition-colors",
        ),
        href=href,
        is_external=True,
    )


def footer_section() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                social_link("github", "https://github.com"),
                social_link("linkedin", "https://linkedin.com"),
                social_link("twitter", "https://twitter.com"),
                social_link("mail", "mailto:your.email@example.com"),
                class_name="flex items-center gap-6 mb-4 md:mb-0",
            ),
            rx.el.p(
                f"© 2024 Your Name. All Rights Reserved.",
                class_name="text-sm",
                color=SECONDARY_COLOR,
            ),
            class_name="container mx-auto px-4 md:px-8 py-8 flex flex-col md:flex-row justify-between items-center",
        ),
        class_name="bg-gray-100 border-t border-gray-200",
    )