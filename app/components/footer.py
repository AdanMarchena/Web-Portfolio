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
        target="_blank",
    )


def footer_section() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                social_link("github", "https://github.com/AdanMarchena"),
                social_link("linkedin", "https://www.linkedin.com/in/ad%C3%A1n-marchena-romero-243826252/"),
                social_link("twitter", "https://x.com/AdanMarchenaDev?t=VBt9esCPINwcDV5M4pcUkQ&s=09 "),
                social_link("mail", "mailto:adanmarchena.dev@gmail.com"),
                class_name="flex items-center gap-6 mb-4 md:mb-0",
            ),
            rx.el.p(
                f"© 2024 Adán Marchena. All Rights Reserved.",
                class_name="text-sm",
                color=SECONDARY_COLOR,
            ),
            class_name="container mx-auto px-4 md:px-8 py-8 flex flex-col md:flex-row justify-between items-center",
        ),
        class_name="bg-gray-100 border-t border-gray-200",
    )