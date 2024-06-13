from flet import *


# bruh

def main(page: Page):
    selected_device = "none"
    page.fonts = {
        "MontserratRegular": "fonts\Montserrat-Regular.ttf",
        "MontserratRegularBoldItalic": "fonts\Montserrat-BoldItalic.ttf",
        "InterMedium": "fonts\Inter-Medium.ttf",
        "RubikRegular": "fonts\Rubik-Regular.ttf"
    }

    page.window_resizable = True
    page.window_maximized = True
    page.window_min_height = 650
    page.window_min_width = 450

    page.bgcolor = "#0a0a0a"
    page.title = "MyProgram"
    page.theme_mode = 'dark'
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    def configuration_dropdown_changed(e):
        print(e.control.value)
        print(e.control.parent.parent.controls[1])

    def device_tile_clicked(e):
        e.control.title.color = "#f4c430"
        selected_device = e.control.title.value

        _configure_device_column.controls[1].value = selected_device
        _configure_device_column.controls[1].color = ColorScheme.primary

        if selected_device == "Control Hub":
            _home_create_body.controls[0].tabs[0].content.controls[1].content.controls[
                1].title.color = ColorScheme.primary
        else:
            _home_create_body.controls[0].tabs[0].content.controls[1].content.controls[
                2].title.color = ColorScheme.primary
        page.update()

    def tile_clicked(e):
        if _configure_device_column.controls[1].value != "No devices selected":
            _select_device_to_configure_container.content.controls.clear()
            _select_device_to_configure_container.content.controls.append(_edit_configuration_column)
            _select_device_to_configure_container.content.controls[0].controls[0].controls.append(
                _config_control_buttons)
            device_configure_title.value = e.control.title.value
            _configure_device_column.controls[1].color = ColorScheme.primary
        else:
            _configure_device_column.controls[1].color = "#ce2029"

        if len(_edit_configuration_column.controls) > 1:
            _edit_configuration_column.controls.pop()

        if device_configure_title.value == "Motors":
            _edit_configuration_column.controls.append(_motor_tile_row)
        elif device_configure_title.value == "Servos":
            _edit_configuration_column.controls.append(_servo_tile_row)
        elif device_configure_title.value == "Digital Devices":
            _edit_configuration_column.controls.append(_digital_devices_tile_row)

        page.update()

    device_configure_title = Text("Configure Device:", font_family="InterMedium", size=20)

    _edit_configuration_column = Column(
        [
            Column([device_configure_title]),
        ],
        expand=True,
    )

    save_configuration = ElevatedButton(icon=icons.SAVE_SHARP, color="#fad201", text="Save")
    cancel_configuration = ElevatedButton(color="#fad201", text="Cancel")

    _config_control_buttons = Row(
        [
            save_configuration,
            cancel_configuration
        ],
    )

    _motor_tile_row = Column(
        [
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("0", size=18, font_family="InterMedium"),
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("1", size=18, font_family="InterMedium"),
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("2", size=18, font_family="InterMedium"),
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("3", size=18, font_family="InterMedium"),
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
        ],
        expand=True,
        scroll="auto"
    )

    _servo_tile_row = Column(
        [
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("0", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("1", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("2", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("3", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("4", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("5", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Continuous Rotation Servo"),
                                            dropdown.Option("REV Blinkin LED Driver"),
                                            dropdown.Option("REV SPARKmini Controller"),
                                            dropdown.Option("Servo")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
        ],
        expand=True,
        scroll="auto"
    )

    _digital_devices_tile_row = Column(
        [
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("0", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("1", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("2", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("3", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("4", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("5", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("6", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
            Divider(thickness=20),
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text("7", size=18, font_family="InterMedium"),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Digital Device"),
                                            dropdown.Option("LED"),
                                            dropdown.Option("REV Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="Enter a device name")
                        ]
                    )
                ]
            ),
        ],
        expand=True,
        scroll="auto"
    )

    configure_motors = ListTile(
        title=Text("Motors"),
        subtitle=Text("Configure Motors"),
        on_click=tile_clicked
    )

    configure_servos = ListTile(
        title=Text("Servos"),
        subtitle=Text("Configure Servos"),
        on_click=tile_clicked
    )

    configure_dig_devices = ListTile(
        title=Text("Digital Devices"),
        subtitle=Text("Configure Digital Devices"),
        on_click=tile_clicked
    )

    configure_pvm = ListTile(
        title=Text("PVM Devices"),
        subtitle=Text("Configure PVM Devices"),
        on_click=tile_clicked
    )

    configure_analog = ListTile(
        title=Text("Analog Input Devices"),
        subtitle=Text("Configure Analog Input Devices"),
        on_click=tile_clicked
    )

    configure_i2c0 = ListTile(
        title=Text("I2C Bus 0"),
        subtitle=Text("Configure I2C Bus 0"),
        on_click=tile_clicked
    )

    configure_i2c1 = ListTile(
        title=Text("I2C Bus 1"),
        subtitle=Text("Configure I2C Bus 1"),
        on_click=tile_clicked
    )

    configure_i2c2 = ListTile(
        title=Text("I2C Bus 2"),
        subtitle=Text("Configure I2C Bus 2"),
        on_click=tile_clicked
    )

    configure_i2c3 = ListTile(
        title=Text("I2C Bus 3"),
        subtitle=Text("Configure I2C Bus 3"),
        on_click=tile_clicked
    )

    _device_list_column = Column(
        [
            configure_motors,
            Divider(thickness=2, height=8),
            configure_servos,
            Divider(thickness=2, height=8),
            configure_dig_devices,
            Divider(thickness=2, height=8),
            configure_pvm,
            Divider(thickness=2, height=8),
            configure_analog,
            Divider(thickness=2, height=8),
            configure_i2c0,
            Divider(thickness=2, height=8),
            configure_i2c1,
            Divider(thickness=2, height=8),
            configure_i2c2,
            Divider(thickness=2, height=8),
            configure_i2c3
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True,
        scroll="auto"
    )

    device_name_during_configuration = Text("No devices selected")
    select_device_to_configure_title = Text("Select a device to configure:", font_family="InterMedium", size=20)
    device_configure_title = Text("Configure Device:", font_family="InterMedium", size=20)

    _expansion_hub_tile = CupertinoListTile(
        leading=Icon(name=icons.SMARTPHONE),
        title=Text("Expansion Hub"),
        subtitle=Text("Click on tile to continue >>>"),
        on_click=device_tile_clicked,
        notched=True
    )

    _control_hub_tile = CupertinoListTile(
        leading=Icon(name=icons.SMARTPHONE),
        title=Text("Control Hub"),
        subtitle=Text("Click on tile to continue >>>"),
        on_click=device_tile_clicked,
        notched=True
    )

    _configure_device_column = Column(
        [
            device_configure_title,
            device_name_during_configuration,
            _device_list_column
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True,
    )

    _select_device_to_configure_column = Column(
        [
            select_device_to_configure_title,
            _expansion_hub_tile,
            _control_hub_tile
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    _select_device_to_configure_container = Container(
        border=border.all(width=4, color="#b5b5b5"),
        width=page.window_width / 2.5,
        height=page.window_height - 250,
        border_radius=20,
        padding=20,
        adaptive=True,
        content=_select_device_to_configure_column,
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )

    _configure_device_container = Container(
        border=border.all(width=4, color="#b5b5b5"),
        width=page.window_width / 2.5,
        height=page.window_height - 250,
        border_radius=20,
        padding=20,
        adaptive=True,
        content=_configure_device_column,
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )

    create_program_tabs = Tabs(
        selected_index=0,
        animation_duration=300,
        scrollable=False,
        tabs=[
            Tab(
                text="Configuration",
                content=Row(
                    controls=[
                        VerticalDivider(width=100, color="surface,0"),
                        _select_device_to_configure_container,
                        _configure_device_container,
                        VerticalDivider(width=100, color="surface,0")
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER
                )
            ),
        ],
        expand=1,
    )

    _home_create_body = Row(
        [
            Column(
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
                CupertinoListTile(title="first", subtitle="someinfo"),
            )
        ],
        expand=True,
        alignment=MainAxisAlignment.CENTER,
        vertical_alignment=CrossAxisAlignment.CENTER
    )

    def change_route(e: RouteChangeEvent):
        page.views.clear()

        page.views.append(
            View(
                route='/start',
                controls=[
                    AppBar(
                        bgcolor=colors.SURFACE_VARIANT,
                        # trailing=IconButton(icons.CLOSE, on_click=exit_app),
                        # middle=home_title,
                    ),
                    _home_create_body
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=25
            )
        )

        page.update()

    page.on_route_change = change_route
    page.go(page.route)

    page.update()


if __name__ == '__main__':
    app(target=main, assets_dir="assets")
