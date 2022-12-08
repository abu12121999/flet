from flet import *
from flet import icons, colors

appmenu = AppBar(
    bgcolor="#32324C",
    leading=IconButton(
        icon=icons.MENU,
        icon_color="white",
        icon_size=30,
        tooltip="Menyu"
    ),
    title=Text(
        "MyInfo",
        size=30,
        color="white",
        weight="bold"
    ),
    actions=[
        IconButton(
            icon=icons.SETTINGS,
            icon_color="white",
            icon_size=30,
            tooltip="settings"
        )
    ]

)
