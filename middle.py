from flet import *

# facebook
facebook = Row([
    Container(
        width=650,
        height=90,
        border_radius=20,
        bgcolor="#1778f2",
        content=Row([
            Container(
                width=90,
                height=90,
                border=border.only(right=border.BorderSide(1, "#1B1B38")),
                content=Icon(
                    name="FACEBOOK",
                    color="#FFFFF3",
                    size=60
                ),
            ),
            Text(
                "Facebook",
                color="#FFFFF3",
                size=28,
                weight="w600"
            )

        ], alignment="start")
    )

], alignment="center")

# telegram
telegram = Row([
    Container(
        width=650,
        height=90,
        border_radius=20,
        bgcolor="#0088cc",
        content=Row([
            Container(
                width=90,
                height=90,
                border=border.only(right=border.BorderSide(1, "#1B1B38")),
                content=Icon(
                    name="TELEGRAM_SHARP",
                    color="#FFFFF3",
                    size=60
                ),
            ),
            Text(
                "Telegram",
                color="#FFFFF3",
                size=28,
                weight="w600"
            )

        ], alignment="start")
    )

], alignment="center")

# instagram
instagram = Row([
    Container(
        width=650,
        height=90,
        border_radius=20,
        bgcolor="#c32aa3",
        content=Row([
            Container(
                width=90,
                height=90,
                border=border.only(right=border.BorderSide(1, "#1B1B38")),
                content=Image(
                    src="./assets/images/instagram.png",
                )
            ),
            Text(
                "Instagram",
                color="#FFFFF3",
                size=28,
                weight="w600"
            )

        ], alignment="start")
    )

], alignment="center")

# Linkedin
linkedin = Row([
    Container(
        width=650,
        height=90,
        border_radius=20,
        bgcolor="#0288D1",
        content=Row([
            Container(
                width=90,
                height=90,
                border=border.only(right=border.BorderSide(1, "#1B1B38")),
                content=Image(
                    src="./assets/images/linkedin.png",
                )
            ),
            Text(
                "Linkedin",
                color="#FFFFF3",
                size=28,
                weight="w600"
            )

        ], alignment="start")
    )

], alignment="center")

# Github
github = Row([
    Container(
        width=650,
        height=90,
        border_radius=20,
        bgcolor="#333333",
        content=Row([
            Container(
                width=90,
                height=90,
                border=border.only(right=border.BorderSide(1, "#1B1B38")),
                content=Image(
                    src="./assets/images/github.png",
                )
            ),
            Text(
                "Github",
                color="#FFFFF3",
                size=28,
                weight="w600"
            )

        ], alignment="start")
    )

], alignment="center")

middle = (linkedin, github, facebook, instagram, telegram)
