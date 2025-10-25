import reflex as rx
from typing import TypedDict
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Skill(TypedDict):
    name: str
    icon: str


class Experience(TypedDict):
    title: str
    company: str
    date: str
    description: str


class Project(TypedDict):
    name: str
    description: str
    image: str
    tags: list[str]
    category: str


class State(rx.State):
    """The base state for the app."""

    is_mobile_menu_open: bool = False
    active_filter: str = "All"
    projects: list[Project] = [
        {
            "name": "2D warehouse inventory display (under development)",
            "description": "Development of an interactive application that allows 2D visualization of the layout of materials within a warehouse, facilitating quick search and location.",
            "image": "/Warehouse-app.jpg",
            "tags": ["React", "FastAPI", "konva", "SQL"],
            "category": "Web",
        },
        {
            "name": "Portfolio Website",
            "description": "A personal portfolio website to showcase my work and skills.",
            "image": "/web-portfolio.png",
            "tags": ["Reflex", "Python", "Web"],
            "category": "Web",
        },
        
    ]
    name: str = ""
    email: str = ""
    message: str = ""
    form_is_loading: bool = False
    form_success: bool = False
    form_error: str = ""

    @rx.var
    def filtered_projects(self) -> list[Project]:
        if self.active_filter == "All":
            return self.projects
        return [p for p in self.projects if p["category"] == self.active_filter]

    @rx.event
    def set_filter(self, category: str):
        self.active_filter = category
    
    def set_name(self, name: str):
        self.name = name

    def set_email(self, email: str):
        self.email = email

    def set_message(self, message: str):
        self.message = message

    @rx.event
    async def handle_submit(self):
        """Maneja el envío del formulario con envío real de email"""
        # Validar campos
        if not all([self.name, self.email, self.message]):
            self.form_error = "Please fill out all fields."
            return

        self.form_is_loading = True
        self.form_error = ""
        self.form_success = False

        try:
            # Enviar email
            success = await self.send_email()
            
            if success:
                self.form_success = True
                # Limpiar formulario
                self.name = ""
                self.email = ""
                self.message = ""
                yield rx.toast.success("Message sent successfully! I'll contact you soon.")
            else:
                self.form_error = "Error sending message. Please try again."
                yield rx.toast.error("Error sending message. Please try again.")
                
        except Exception as e:
            self.form_error = f"Server error: {str(e)}"
            yield rx.toast.error("Server error. Please try again.")
        finally:
            self.form_is_loading = False
        
    async def send_email(self) -> bool:
        """Envía el formulario por email"""
        try:
            # Configuración SMTP desde variables de entorno
            smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("SMTP_PORT", "587"))
            email_user = os.getenv("EMAIL_USER", "")
            email_password = os.getenv("EMAIL_PASSWORD", "")

            # Validar que tenemos las credenciales
            if not email_user or not email_password:
                print("ERROR: Email credentials not configured")
                return False

            # Crear mensaje
            msg = MimeMultipart()
            msg['From'] = email_user
            msg['To'] = email_user  # Lo recibes tú
            msg['Subject'] = f"📧 Nuevo mensaje de {self.name} - Portfolio"

            body = f"""
            🔔 NUEVO MENSAJE DESDE TU PORTFOLIO

            📋 Información del contacto:
            • Nombre: {self.name}
            • Email: {self.email}

            💬 Mensaje:
            {self.message}

            ---
            🕐 Enviado automáticamente desde tu portfolio.
            """
            
            msg.attach(MimeText(body, 'plain', 'utf-8'))

            # Enviar email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_user, email_password)
                server.send_message(msg)

            print("✅ Email enviado exitosamente")
            return True

        except smtplib.SMTPAuthenticationError:
            print("❌ Error de autenticación SMTP - Verifica usuario y contraseña")
            return False
        except Exception as e:
            print(f"❌ Error enviando email: {e}")
            return False

    about_me_text: str = "As a creative and enthusiastic UI/UX developer, I specialize in creating attractive, functional, and user-centered web applications. With a solid foundation in both design principles and modern frontend/backend technologies, I bridge the gap between aesthetics and performance. In addition, I apply my knowledge of data science to transform complex information into clear insights and interactive visualizations, supporting data-driven decision-making. I am passionate about solving complex problems and turning innovative ideas into reality through clean, efficient code and intuitive interfaces."
    
    technical_skills: list[Skill] = [
        {"name": "FastAPI", "icon": "server"},
        {"name": "JavaScript", "icon": "code"},
        {"name": "React", "icon": "atom"},
        {"name": "Reflex", "icon": "zap"},
        {"name": "APIs", "icon": "webhook"},
    ]
    data_science_skills: list[Skill] = [
        {"name": "Python", "icon": "code"},
        {"name": "Streamlit", "icon": "crown"},
        {"name": "Pandas", "icon": "panda"},
        {"name": "NumPy", "icon": "combine"},
        {"name": "SQL", "icon": "database"},
        {"name": "Scikit-learn", "icon": "brain"},
    ]
    #design_skills: list[Skill] = [
     #   {"name": "UI/UX Design", "icon": "figma"},
     #   {"name": "Figma", "icon": "figma"},
     #   {"name": "Prototyping", "icon": "drafting_compass"},
     #   {"name": "User Research", "icon": "users"},
    #]
    tools: list[Skill] = [
        {"name": "Git & GitHub", "icon": "git_branch"},
        {"name": "Docker", "icon": "box"},
        {"name": "VS Code", "icon": "code"},
        #{"name": "Jira", "icon": "check_circle"},
        {"name": "Notion", "icon": "box"},
        {"name": "Jupyter Notebook", "icon": "book-open"}
    ]
    experience: list[Experience] = [
        {
            "title": "Junior Python developer",
            "company": "Spread",
            "date": "2018 - 2019",
            "description": "I developed scripts for different areas of the company with the aim of visualizing operational information, such as delivery routes and working hours. I implemented connections to the corporate database to automate the extraction and analysis of daily work records.",
        },
    ]

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open