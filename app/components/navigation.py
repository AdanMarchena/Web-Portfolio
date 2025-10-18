import reflex as rx
from app.state import State
from app.styles import (
    PRIMARY_COLOR,
    ELEVATION_4_SHADOW,
    FONT_FAMILY,
    RIPPLE_CLASS,
    SURFACE_COLOR,
)


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=f"font-medium text-gray-600 hover:text-orange-600 transition-colors py-2 px-4 rounded-full",
    )


def mobile_nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        on_click=State.toggle_mobile_menu,
        class_name="block w-full text-left px-4 py-3 text-lg font-semibold text-gray-700 hover:bg-orange-50 rounded-lg",
    )


def navigation_bar() -> rx.Component:
    nav_items = [
        ("Home", "#home"),
        ("About", "#about"),
        ("Skills", "#skills"),
        ("Experience", "#experience"),
        ("Projects", "#projects"),
        ("Contact", "#contact"),
    ]
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("code", color=PRIMARY_COLOR, size=32),
                        rx.el.span(
                            "DevPortfolio",
                            class_name=f"text-xl font-bold text-gray-800 ml-2",
                        ),
                        class_name="flex items-center",
                    ),
                    href="#home",
                ),
                class_name="flex items-center",
            ),
            rx.el.nav(
                rx.foreach(nav_items, lambda item: nav_link(item[0], item[1])),
                class_name="hidden md:flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("menu", size=28, class_name="text-gray-700"),
                    on_click=State.toggle_mobile_menu,
                    class_name="md:hidden p-2 rounded-full hover:bg-gray-100",
                ),
                class_name="md:hidden",
            ),
            rx.cond(
                State.is_mobile_menu_open,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "Navigation",
                                class_name="text-xl font-bold text-gray-800",
                            ),
                            rx.el.button(
                                rx.icon("x", size=24),
                                on_click=State.toggle_mobile_menu,
                                class_name="p-2 rounded-full hover:bg-gray-200",
                            ),
                            class_name="flex justify-between items-center p-4 border-b border-gray-200",
                        ),
                        rx.el.nav(
                            rx.foreach(
                                nav_items,
                                lambda item: mobile_nav_link(item[0], item[1]),
                            ),
                            class_name="p-4 space-y-2",
                        ),
                        class_name="flex flex-col bg-white rounded-lg shadow-lg w-full max-w-sm mx-auto",
                    ),
                    class_name="fixed inset-0 bg-black/40 z-50 p-4 pt-20 flex flex-col items-center",
                    on_click=State.toggle_mobile_menu,
                ),
            ),
            class_name="container mx-auto px-4 md:px-8 flex justify-between items-center",
        ),
        position="sticky",
        top="0",
        z_index=40,
        width="100%",
        padding="1rem 0",
        background_color=f"{SURFACE_COLOR}E6",
        backdrop_filter="blur(10px)",
        box_shadow=ELEVATION_4_SHADOW,
        font_family=FONT_FAMILY,
    )