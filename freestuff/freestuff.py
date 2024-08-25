
import reflex as rx
import requests
from rxconfig import config
from freestuff.components.select import select
from freestuff.components.card import card

class State(rx.State):
    results:list[dict[str,str]]
    def get_resullts(self):
        response = requests.get("https://www.gamerpower.com/api/giveaways")
        data = response.json()
        self.results.extend(data)
    exampleoptions = [
        {"value": "example", "label": "example"},
        {"value": "example", "label": "example"},
        {"value": "example", "label": "example"}
    ]


def index() -> rx.Component:
    
    return rx.vstack(
        rx.image(
            src="https://cloud-8yzqjfvxo-hack-club-bot.vercel.app/0frame_3.png"
        ),
        rx.hstack(
            select(
                options = State.exampleoptions,
                width="183px",
                height="66px",
                isSearchable=False,
                isClearable=True,
                placeholder = "Sort"
            ),
            select(
                options = State.exampleoptions,
                width="183px",
                height="66px",
                isSearchable=False,
                isClearable=True,
                placeholder="Platform"
                
            ),
            select(
                options = State.exampleoptions,
                width="183px",
                height="66px",
                isSearchable=False,
                isClearable=True,
                placeholder = "Type"
            ),
        ),
        
        rx.grid(
            rx.foreach(
                State.results,
                lambda info: card(info)
            ),
            columns="3",
            spacing_x= "9",
            spacing_y= "6"
        ),
        padding_right="81px",
        padding_left="81px",
        padding_top="20px",
        padding_bottom="20px"
    )


app = rx.App(stylesheets=["./styles.css"])
app.add_page(index)
