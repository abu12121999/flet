from flet import *
from flet import icons, colors

top = Row([
    # chap - rasm
    Container(
        width=200,
        height=200,
        margin=50,
        content=Image(
            src="./assets/images/profile_photo.png",
            # width=200,
            # height=200,
            border_radius=200,
        )
    ),
    # o'ng - ma'lumot
    Container(
        width=400,
        height=200,
        content=Column([
            # MrKadirov
            Row([
                Text(
                    "MrKadirov",
                    size=40,
                    color="#FFFFF3",
                    # weight="bold"
                )
            ]),
            # joylashuv
            Row([
                Container(
                    height=50,
                    width=300,
                    margin=5,
                    padding=5,
                    border_radius=50,
                    border=border.all(3, "#7979FF"),
                    content=Row([
                        Icon(
                            name=icons.LOCATION_ON,
                            color="#7979FF",
                        ),
                        Text(
                            "Samarkand, Uzbekistan",
                            size=20,
                            color="#7979FF",
                            weight="bold"
                        )
                    ], alignment="center")
                )

            ]),
            # Bio
            Row([
                Text(
                    "Date of birth: 12/12/1999\nMajor: Python Backend Developer\nEdu: Study at Samarkand branch of TUIT.",
                    color="#AFAFE1",
                    size=20,
                    # weight="bold"
                )
            ]),

        ])
    )
], alignment="center")
