from flet import *


def main(page: Page):
    page.client_storage.clear()


if __name__ == '__main__':
    app(target=main)
