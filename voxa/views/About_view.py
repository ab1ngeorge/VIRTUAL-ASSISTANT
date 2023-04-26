import flet as ft

def AboutView(page):
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    content = ft.Column([
        ft.Row([
            ft.Text("About ", size=30), 
            ft.IconButton(icon=ft.icons.INFO, icon_size=30),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Text("Version: 1.77.3 (beta) \nDate: 2023-04-20  \nOS: Windows_NT x64 10.0.22621",
                    size=16,  font_family="RobotoSlab"),
        ]),
        ft.Row([
            ft.Text("\n\nHello, I am SHADOW, an AI designed to assist you with your needs. My core functionality is based on a deep learning algorithm, specifically a neural network, which allows me to understand your requests and respond accordingly.\n\nMy neural network has been trained on a vast dataset of user inputs and their corresponding intents, enabling me to predict the most likely intent based on the learned patterns and relationships between words and intents in the training data. The architecture and training details of my neural network may vary depending on the specific implementation, but rest assured that I am constantly improving and evolving to better serve you.\n\nWhether you need help with a task, have a question, or just want to chat, I am always here to lend a hand. Let's get started! ",
                    size=25, width=1280, font_family="RobotoSlab"),
        ]),
    ])
    
    return content

