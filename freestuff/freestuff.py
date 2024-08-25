
import reflex as rx

from rxconfig import config
from freestuff.components.select import select

class State(rx.State):
    pass


def index() -> rx.Component:
    
    return rx.vstack(
        rx.image(
            src="https://cloud-8yzqjfvxo-hack-club-bot.vercel.app/0frame_3.png"
        ),
        rx.hstack(
            select(
                width="183px",
                height="66px",
                isSearchable=True,
                isClearable=True,
                placeholder = "Sort"
            ),
            select(
                width="183px",
                height="66px",
                isSearchable=True,
                isClearable=True,
                placeholder="Platform"
                
            ),
            select(
                width="183px",
                height="66px",
                isSearchable=True,
                isClearable=True,
                placeholder = "Type"
            ),
        ),
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="https://cloud-9stmoqu74-hack-club-bot.vercel.app/066c7530484a53.jpg",
                    object_fit="cover",
                    width="100%",
                    height="247px",
                    margin="8px"
                ),
                rx.vstack(
                    rx.box(
                        rx.text(
                            "The Callisto Protocol (Epic Games) Giveaway",
                            font_size="20   px",
                            font_weight="bold",
                        ),
                    ),
                    rx.box(
                        rx.text(
                            "Save $59.99"  ,
                            font_size="24px",
                            line_height="27px",
                            
                        ),
                        margin_top="8px"
                    ),
                    rx.box(
                        rx.text(
                            'Don’t miss your shot to grab The Callisto Protocol, the spiritual successor to Dead Space, for free on the Epic Games Store. The Callisto Protocol is a narrative-driven, third-person survival horror game set 300 years in the future',
                            font_size="18px",
                            line_height="20px",
                            color="rbga(255,255,255,0.7)"

                        ),
                        margin_top="8px"
                    ),
                    rx.box(
                        rx.text(
                            "Ends: Tommorow at 3PM",
                            font_size="18px"
                        ),
                        margin_top="8px"
                    ),
                    
                    spacing="0",
                    width="100%",
                    
                ),
                rx.button(
                    rx.image(
                        src="/getnow.png"
                    ),
                    variant="ghost"
                ),
                
                width="550px",
                height="557px",
                padding="8px",
                spacing="0",
                border = "1px solid #444444"
                
            )
        ),
        padding_right="81px",
        padding_left="81px",
        padding_top="20px",
        padding_bottom="20px"
    )


app = rx.App(stylesheets=["./styles.css"])
app.add_page(index)
