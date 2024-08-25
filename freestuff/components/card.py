import reflex as rx
def card(info):
    return rx.hstack(
        rx.vstack(
            rx.image(
                src="https://cloud-9stmoqu74-hack-club-bot.vercel.app/066c7530484a53.jpg",
                object_fit="cover",
                width="100%",
                height="247px",
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        info["titles"],
                        font_size="22px",
                        font_weight="700",
                    ),
                ),
                rx.box(
                    rx.text(
                        "Save $59.99"  ,
                        font_size="24px",
                        line_height="27px",
                        font_weight="900"
                        
                    ),
                ),
                rx.box(
                    rx.text(
                        'Don’t miss your shot to grab The Callisto Protocol, the spiritual successor to Dead Space, for free on the Epic Games Store. The Callisto Protocol is a narrative-driven, third-person survival horror game set 300 years in the future',
                        font_size="18px",
                        line_height="20px",
                        color="rbga(255,255,255,0.7)"

                    ),
                ),
                rx.box(
                    rx.text(
                        "Ends: Tommorow at 3PM",
                        font_size="18px"
                    ),
                ),
                
                spacing="2",
                width="100%",
                
            ),
            rx.button(
                rx.image(
                    src="/getnow.png",
                    width="150px",
                    height="60px",
                ),
                as_child=True,
                variant="ghost"
            ),
            
            width="550px",
            height="557px",
            padding="16px",
            spacing="4",
            border = "1px solid #444444",
            border_radius="8px"
        )
    ),