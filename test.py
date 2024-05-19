import flet as ft


def main(page: ft.Page):
    def tile_clicked(e):
        print("Tile clicked")

    page.add(
        ft.ListTile(
            leading=ft.Icon(name=ft.cupertino_icons.GAME_CONTROLLER),
            title=ft.Text("Control Hub"),
            subtitle=ft.Text("Click on tile to continue >>>"),
            on_click=tile_clicked
        )
    )


ft.app(target=main)