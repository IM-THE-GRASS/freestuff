import reflex as rx
def card(info):
    return rx.hstack(
        rx.vstack(
            rx.image(
                src=info["image"],
                object_fit="cover",
                width="100%",
                height="247px",
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        info["title"],
                        font_size="22px",
                        font_weight="700",
                    ),
                ),
                rx.hstack(
                    rx.text(
                        "Save "  ,
                        font_size="24px",
                        line_height="27px",
                        font_weight="900"
                        
                    ),
                    rx.text(
                        info["worth"],
                        font_size="24px",
                        line_height="27px",
                        font_weight="900"
                        
                    ),
                ),
                rx.scroll_area(
                    rx.text(
                        info["description"],
                        font_size="18px",
                        line_height="20px",
                        color="rbga(255,255,255,0.7)"

                    ),
                    max_height="15vh"
                ),
                
                
                spacing="2",
                width="100%",
                
            ),
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Ends:",
                            font_size="18px"
                        ),
                        rx.text(
                            info["end_date"],
                            font_size="18px"
                        ),
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
                    spacing="4"
                ),
                wrap="nowrap",
                direction="row",
                align="end",
                justify="start",
                height="100%"
            ),
            width="550px",
            height="700px",
            padding="16px",
            spacing="4",
            border = "1px solid #444444",
            border_radius="8px"
        )
    )