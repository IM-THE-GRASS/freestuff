
import reflex as rx

from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    
    return rx.vstack(
        rx.image(
            src="https://cloud-8yzqjfvxo-hack-club-bot.vercel.app/0frame_3.png"
        ),
        padding_right="81px",
        padding_left="81px",
        padding_top="20px",
        padding_bottom="20px"
    )


app = rx.App()
app.add_page(index)
