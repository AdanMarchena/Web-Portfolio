import reflex as rx

PRIMARY_COLOR = "#FF6F00"
SECONDARY_COLOR = "#757575"
BACKGROUND_COLOR = "#FDF8F3"
SURFACE_COLOR = "#FFFFFF"
ON_SURFACE_COLOR = "#1C1B1F"
RIPPLE_CLASS = "relative overflow-hidden transition-all duration-300 ease-in-out hover:scale-[1.02]"
ELEVATION_1_SHADOW = "0px 1px 3px rgba(0,0,0,0.12)"
ELEVATION_2_SHADOW = "0px 3px 6px rgba(0,0,0,0.15)"
ELEVATION_4_SHADOW = "0px 4px 8px rgba(0,0,0,0.2)"
ELEVATION_HOVER_SHADOW = "0px 6px 12px rgba(0,0,0,0.2)"
FONT_FAMILY = "'Montserrat', sans-serif"
base_button_style = {
    "height": "40px",
    "padding": "0 24px",
    "border_radius": "20px",
    "font_weight": "600",
    "font_size": "14px",
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "transition": "box-shadow 0.2s ease, background-color 0.2s ease",
}
contained_button_style = {
    **base_button_style,
    "background_color": PRIMARY_COLOR,
    "color": SURFACE_COLOR,
    "box_shadow": ELEVATION_2_SHADOW,
    "_hover": {"box_shadow": ELEVATION_4_SHADOW, "background_color": "#E66300"},
}
outlined_button_style = {
    **base_button_style,
    "background_color": "transparent",
    "color": PRIMARY_COLOR,
    "border": f"1px solid {PRIMARY_COLOR}",
    "_hover": {"background_color": f"{PRIMARY_COLOR}1A"},
}