"""
Demo for the NavBar component.
"""

import gradio as gr
from gradio_navbar import NavBar


example = NavBar().example_value()

demo = gr.Interface(
    lambda x: x,
    [
        NavBar(
            value={
                "company_logo_url": "https://avatars.githubusercontent.com/u/\
55248617?v=4",
                "company_name": "Gradio",
                "logout_link": "https://www.gradio.app",
                "username": "gradio",
                "profile_photo_url": "https://avatars.githubusercontent.com/u/\
55248607?v=4",
            }
        ),
    ],  # interactive version of your component
    NavBar(),  # static version of your component
    examples=[
        [example]
    ],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
