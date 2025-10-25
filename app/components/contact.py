import reflex as rx
from app.state import State
from app.styles import contained_button_style, RIPPLE_CLASS


def form_field(
    label: str, name: str, placeholder: str, type: str, value: rx.Var[str]
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            name=name,
            placeholder=placeholder,
            type=type,
            on_change=value,
            required=True,
            class_name="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-orange-500 focus:border-orange-500 transition",
        ),
        class_name="mb-4",
    )


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Get In Touch",
                class_name="text-3xl md:text-4xl font-bold text-gray-900 mb-8 text-center",
            ),
            
            # Mostrar mensaje de éxito
            rx.cond(
                State.form_success,
                rx.el.div(
                    rx.icon("check-circle", class_name="text-green-500 text-4xl mb-4 mx-auto"),
                    rx.el.p(
                        "¡Message sent successfully! I'll contact you soon.",
                        class_name="text-green-700 text-lg text-center"
                    ),
                    class_name="bg-green-50 p-6 rounded-lg text-center mb-6"
                ),
            ),
            
            # Mostrar mensaje de error
            rx.cond(
                State.form_error,
                rx.el.div(
                    rx.icon("alert-circle", class_name="text-red-500 text-4xl mb-4 mx-auto"),
                    rx.el.p(
                        State.form_error,
                        class_name="text-red-700 text-center"
                    ),
                    class_name="bg-red-50 p-4 rounded-lg mb-6 text-center"
                ),
            ),
            
            rx.el.div(
                rx.el.form(
                    form_field("Name", "name", "Your Name", "text", State.set_name),
                    form_field(
                        "Email",
                        "email",
                        "your.email@example.com",
                        "email",
                        State.set_email,
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Message",
                            class_name="block text-sm font-medium text-gray-700 mb-1",
                        ),
                        rx.el.textarea(
                            name="message",
                            placeholder="Your message...",
                            on_change=State.set_message,
                            required=True,
                            class_name="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:ring-orange-500 focus:border-orange-500 transition h-32",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        rx.cond(
                            State.form_is_loading,
                            rx.el.div(  # ← Usar div nativo en lugar de chakra.stack
                                rx.icon("loader", class_name="animate-spin"),
                                "Sending...",
                                class_name="flex items-center gap-2 justify-center"
                            ),
                            "Send Message",
                        ),
                        type="submit",
                        style=contained_button_style,
                        class_name=RIPPLE_CLASS,
                        disabled=State.form_is_loading,
                    ),
                    on_submit=State.handle_submit,
                    class_name="max-w-xl mx-auto",
                ),
                class_name="bg-white p-8 rounded-xl shadow-md",
            ),
            class_name="container mx-auto px-4 md:px-8 py-16 md:py-24",
        ),
        id="contact",
        class_name="bg-gray-100",
    )