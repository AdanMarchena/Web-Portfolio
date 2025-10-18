import reflex as rx
from typing import TypedDict


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
            "name": "E-commerce Platform",
            "description": "A full-stack web application for online shopping with a modern UI.",
            "image": "/placeholder.svg",
            "tags": ["React", "Python", "SQL"],
            "category": "Web",
        },
        {
            "name": "Task Management App",
            "description": "A mobile-first application to help users organize their daily tasks.",
            "image": "/placeholder.svg",
            "tags": ["Reflex", "Python", "Mobile"],
            "category": "Mobile",
        },
        {
            "name": "Branding Redesign",
            "description": "A complete redesign of a corporate brand identity and style guide.",
            "image": "/placeholder.svg",
            "tags": ["Figma", "UI/UX"],
            "category": "Design",
        },
        {
            "name": "Social Media Dashboard",
            "description": "A web-based dashboard for managing multiple social media accounts.",
            "image": "/placeholder.svg",
            "tags": ["JavaScript", "APIs", "Web"],
            "category": "Web",
        },
        {
            "name": "Portfolio Website",
            "description": "A personal portfolio website to showcase my work and skills.",
            "image": "/placeholder.svg",
            "tags": ["Reflex", "Python", "Web"],
            "category": "Web",
        },
        {
            "name": "Recipe Finder App",
            "description": "A mobile app for discovering new recipes based on available ingredients.",
            "image": "/placeholder.svg",
            "tags": ["React Native", "Mobile"],
            "category": "Mobile",
        },
    ]
    name: str = ""
    email: str = ""
    message: str = ""
    form_is_loading: bool = False

    @rx.var
    def filtered_projects(self) -> list[Project]:
        if self.active_filter == "All":
            return self.projects
        return [p for p in self.projects if p["category"] == self.active_filter]

    @rx.event
    def set_filter(self, category: str):
        self.active_filter = category

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_is_loading = True
        yield
        import asyncio

        await asyncio.sleep(2)
        self.form_is_loading = False
        if (
            not form_data.get("name")
            or not form_data.get("email")
            or (not form_data.get("message"))
        ):
            yield rx.toast.error("Please fill out all fields.")
            return
        self.name = ""
        self.email = ""
        self.message = ""
        yield rx.toast.success("Message sent successfully!")

    about_me_text: str = "As a Creative Developer and UI/UX enthusiast, I specialize in building beautiful, functional, and user-centric web applications. With a strong foundation in both design principles and modern frontend/backend technologies, I bridge the gap between aesthetics and performance. I thrive on solving complex problems and turning innovative ideas into reality through clean, efficient code and intuitive interfaces."
    technical_skills: list[Skill] = [
        {"name": "Python", "icon": "code"},
        {"name": "JavaScript", "icon": "code"},
        {"name": "React", "icon": "atom"},
        {"name": "Reflex", "icon": "zap"},
        {"name": "SQL", "icon": "database"},
        {"name": "APIs", "icon": "webhook"},
    ]
    design_skills: list[Skill] = [
        {"name": "UI/UX Design", "icon": "figma"},
        {"name": "Figma", "icon": "figma"},
        {"name": "Prototyping", "icon": "drafting_compass"},
        {"name": "User Research", "icon": "users"},
    ]
    tools: list[Skill] = [
        {"name": "Git & GitHub", "icon": "git_branch"},
        {"name": "Docker", "icon": "box"},
        {"name": "VS Code", "icon": "code"},
        {"name": "Jira", "icon": "check_circle"},
    ]
    experience: list[Experience] = [
        {
            "title": "Senior Frontend Developer",
            "company": "Tech Solutions Inc.",
            "date": "Jan 2021 - Present",
            "description": "Leading the development of a new client-facing dashboard using React and TypeScript. Improved application performance by 30% and mentored junior developers.",
        },
        {
            "title": "UI/UX Designer",
            "company": "Creative Minds LLC",
            "date": "Jun 2019 - Dec 2020",
            "description": "Designed and prototyped user interfaces for various mobile and web applications. Conducted user research sessions to gather feedback and iterate on designs.",
        },
        {
            "title": "Software Engineer Intern",
            "company": "Innovate Co.",
            "date": "May 2018 - Aug 2018",
            "description": "Assisted the backend team in developing REST APIs using Python and Flask. Wrote unit tests to ensure code quality and reliability.",
        },
    ]

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open