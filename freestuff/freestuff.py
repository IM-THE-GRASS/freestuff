
import reflex as rx
import requests
from rxconfig import config
from freestuff.components.select import select
from freestuff.components.card import card

class State(rx.State):
    results:list[dict[str,str]]
    sort_option:str = ""
    platform_option:str = ""
    type_option:str = ""
    @rx.var()
    def search_url(self):
        return "https://www.gamerpower.com/api/giveaways?" + self.sort_option + self.type_option + self.platform_option
    def get_results(_="", url = "https://www.gamerpower.com/api/giveaways?"):
        response = requests.get(url)
        data = response.json()
        print(response)
        return data
    results = get_results()
    typeoptions = [
        {"value": "&type=game", "label": "Game"},
        {"value": "&type=loot", "label": "Loot"},
        {"value": "&type=beta", "label": "Beta"}
    ]
    sortoptions = [
        {"value": "&sort=date", "label": "Date"},
        {"value": "&sort=value", "label": "Value"},
        {"value": "&sort=popularity", "label": "Popularity"}
    ]
    def changetype(self, thing):
        self.type_option = thing["value"]
        print(self.search_url)
        # url = self.search_url
        # url = str(url)
        # self.get_results(url)
        self.results = self.get_results(self.search_url)
    def changesort(self, thing):
        self.sort_option = thing["value"]
        print(self.search_url)
        self.results = self.get_results(self.search_url)
        
        
        
    
    

def index() -> rx.Component:
    
    return rx.vstack(
        rx.image(
            src="https://cloud-8yzqjfvxo-hack-club-bot.vercel.app/0frame_3.png"
        ),
        rx.hstack(
            select(
                options = State.sortoptions,
                width="183px",
                height="66px",
                isSearchable=False,
                isClearable=True,
                placeholder = "Sort"
            ),
            # select(
            #     options = State.exampleoptions,
            #     width="183px",
            #     height="66px",
            #     isSearchable=False,
            #     isClearable=True,
            #     placeholder="Platform"
                
            # ),
            select(
                options = State.typeoptions,
                width="183px",
                height="66px",
                isSearchable=False,
                isClearable=True,
                placeholder = "Type",
                onChange=State.changetype
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
