import flet as ft
from flet import *


def main(page: Page):
    page.fonts = {
        "MontserratRegular": "fonts\Montserrat-Regular.ttf",
        "MontserratRegularBoldItalic": "fonts\Montserrat-BoldItalic.ttf",
        "InterMedium": "fonts\Inter-Medium.ttf",
        "RubikRegular": "fonts\Rubik-Regular.ttf"
    }

    """CONFIGURATION CLASSES"""

    motors = ['', '', '', '']
    servos = []
    digital_devices = []
    analog_input_devices = []
    i2c0 = []
    i2c1 = []
    i2c2 = []
    i2c3 = []

    expansion_dict = {
        "motors": motors,
        "servos": servos,
        "digital_devices": digital_devices,
        "i2c0": i2c0,
        "i2c1": i2c1,
        "i2c2": i2c2,
        "i2c3": i2c3
    }

    control_dict = {
        "motors": motors,
        "servos": servos,
        "digital_devices": digital_devices,
        "i2c0": i2c0,
        "i2c1": i2c1,
        "i2c2": i2c2,
        "i2c3": i2c3
    }

    """NECESSARY VARIABLES"""
    adaptive_size = 0
    delta_y = 0
    delta_x = 0

    is_position_changed = False
    is_rotation_changed = False
    selected_device = "none"

    english_phrases = ["Confirm",
                       "Hi!",
                       "Before starting work, please select a language:",
                       "Terms of Use",
                       "1.1. The User undertakes to comply with this Terms of Use without exceptions. \n1.2. There must be a Terms of Use here.",
                       "I agree with Terms of Use",
                       "Continue",
                       "Welcome!",
                       "Top Secret",
                       "Let's start!"]
    russian_phrases = ["Подтвердить",
                       "Здравствуйте!",
                       "Перед началом работы, пожалуйста выберите язык:",
                       "Пользовательское соглашение",
                       "1.1. Пользователь обязуется соблюдать настоящее Пользовательское соглашение без исключений. \n1.2. Здесь должно быть Пользовательское соглашение.",
                       "Я согласен (-на) с Пользовательским соглашением",
                       "Продолжить",
                       "Добро пожаловать!",
                       "Top Secret",
                       "Давай начнем!"]
    user_phrases = english_phrases

    home_title = Text(user_phrases[7], font_family="MontserratRegularBoldItalic")

    img = Image(src="pictures\main_dark_theme.jpg")

    if not page.client_storage.contains_key("programsCount"):
        page.client_storage.set("programsCount", 0)
        programs_count = 0
    else:
        programs_count = page.client_storage.get("programsCount")

    if not page.client_storage.contains_key("isFirstStart"):
        page.client_storage.set("isFirstStart", True)
        is_first_start = True
    else:
        is_first_start = page.client_storage.get("isFirstStart")

    if not page.client_storage.contains_key("programs"):
        page.client_storage.set("programs", [])
        programs = []
    else:
        programs = page.client_storage.get("programs")

    page.window_resizable = True
    page.window_maximized = True
    page.window_min_height = 650
    page.window_min_width = 450

    page.bgcolor = "#0a0a0a"
    page.title = "MyProgram"
    page.theme_mode = 'dark'
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    def set_eng(e):
        user_phrases = english_phrases
        confirm_language.text = user_phrases[0]
        user_greetings.value = user_phrases[1]
        user_info_language.value = user_phrases[2]
        terms_of_use_title.value = user_phrases[3]
        terms_of_use.value = user_phrases[4]
        terms_agree_checkbox.label = user_phrases[5]
        confirm_terms_agree.text = user_phrases[6]
        home_title.value = user_phrases[7]
        title.value = user_phrases[8]
        go.text = user_phrases[9]
        confirm_language.disabled = False
        page.update()

    def set_rus(e):
        user_phrases = russian_phrases
        confirm_language.text = user_phrases[0]
        user_greetings.value = user_phrases[1]
        user_info_language.value = user_phrases[2]
        terms_of_use_title.value = user_phrases[3]
        terms_of_use.value = user_phrases[4]
        terms_agree_checkbox.label = user_phrases[5]
        confirm_terms_agree.text = user_phrases[6]
        home_title.value = user_phrases[7]
        title.value = user_phrases[8]
        go.text = user_phrases[9]
        confirm_language.disabled = False
        page.update()

    def start_work(e):
        if is_first_start:
            page.go('/greet')
        else:
            page.go('/home')

    def terms_agree(e):
        confirm_terms_agree.disabled = False if terms_agree_checkbox.value else True
        page.update()

    def exit_app(e):
        page.window_destroy()

    def home(e):
        page.go('/home')
        page.client_storage.set("isFirstStart", False)

    def change_theme(e):
        if page.theme_mode == 'dark':
            page.bgcolor = "#f2e8c9"
            page.theme_mode = 'light'
            _main_container.bgcolor = "white"
            _terms_container.bgcolor = "#f2e8c9"
            _main_container.image_src = "pictures\main_light_theme.jpg"
        else:
            page.bgcolor = "#0a0a0a"
            page.theme_mode = 'dark'
            _main_container.bgcolor = "dark"
            _terms_container.bgcolor = "black"
            _main_container.image_src = "pictures\main_dark_theme.jpg"

        # page.bgcolor = "#f5f5dc"
        page.update()

    page_body_arrays = [
        Column(
            [Text("You haven't any programs now. It's time to create first one!", font_family="InterMedium", size=24)],
            alignment=MainAxisAlignment.START, expand=True),
        Column(
            [Text("Faves", font_family="InterMedium", size=24)],
            alignment=MainAxisAlignment.START, expand=True),
        Column(
            [Text("Info", font_family="InterMedium", size=24)],
            alignment=MainAxisAlignment.START, expand=True),
        Column(
            [Text("Settings", font_family="InterMedium", size=24)],
            alignment=MainAxisAlignment.START, expand=True),
    ]

    page_body = Column(
        [Text("You haven't any programs now. It's time to create first one!", font_family="InterMedium", size=24)],
        alignment=MainAxisAlignment.START, expand=True)

    def validate_name(e):
        if new_program_title.value != "":
            continue_create.disabled = False
        else:
            continue_create.disabled = True
        page.update()

    def name_new_program(e):
        current_program_title = new_program_title.value
        prog_set.value = new_program_title.value
        page.update()
        page.go("/create/home")

    def enable_rotation_arrow():
        if rotation_button.icon == icons.ARROW_FORWARD:

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].visible = True

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].visible = False

            rotation_button.icon = icons.ARROW_DOWNWARD

        elif rotation_button.icon == icons.ARROW_DOWNWARD:
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].visible = True

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].visible = False

            rotation_button.icon = icons.ARROW_BACK

        elif rotation_button.icon == icons.ARROW_BACK:

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].visible = True

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].visible = False

            rotation_button.icon = icons.ARROW_UPWARD
        elif rotation_button.icon == icons.ARROW_UPWARD:

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].visible = True

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].visible = False
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].visible = False

            rotation_button.icon = icons.ARROW_FORWARD

        page.update()

    def check_create_status(e):
        if create_program_tabs.selected_index > 0 and button_advanced_settings.disabled:
            create_program_tabs.disabled = True
        else:
            create_program_tabs.disabled = False

        page.update()

    def direction_pos_change():
        if position_dropdown.value == "Blue Near":
            delta_x = 0
            delta_y = 0
        elif position_dropdown.value == "Blue Far":
            delta_x = 0
            delta_y = 180
        elif position_dropdown.value == "Red Near":
            delta_x = 440
            delta_y = 0
        else:
            delta_x = 440
            delta_y = 180

        adaptive_size = page.window_height - 700
        if adaptive_size > 262:
            adaptive_size = 262
        print(adaptive_size)
        if rotation_button.icon == icons.ARROW_FORWARD:
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[0].x = -1080 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[1].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[2].x = -1080 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[3].x = -1095 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[4].x = -1080 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[5].x = -1095 + delta_x

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                0].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                1].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                2].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                3].y = 40 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                4].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
                5].y = 68 - adaptive_size / 2 + delta_y
        elif rotation_button.icon == icons.ARROW_DOWNWARD:
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[0].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[1].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[2].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[3].x = -1120 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[4].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[5].x = -1090 + delta_x

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                0].y = 83 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                1].y = 55 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                2].y = 83 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                3].y = 68 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                4].y = 83 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
                5].y = 68 - adaptive_size / 2 + delta_y

        elif rotation_button.icon == icons.ARROW_BACK:
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[0].x = -1130 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[1].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[2].x = -1130 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[3].x = -1115 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[4].x = -1130 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[5].x = -1115 + delta_x

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                0].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                1].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                2].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                3].y = 40 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                4].y = 54 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
                5].y = 68 - adaptive_size / 2 + delta_y

        else:
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[0].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[1].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[2].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[3].x = -1120 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[4].x = -1105 + delta_x
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[5].x = -1090 + delta_x

            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                0].y = 25 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                1].y = 55 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                2].y = 25 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                3].y = 40 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                4].y = 25 - adaptive_size / 2 + delta_y
            _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
                5].y = 40 - adaptive_size / 2 + delta_y

        page.update()

    def square_change():
        if position_dropdown.value:
            is_position_changed = True

            if position_dropdown.value == "Blue Near":
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].paint = selected_paint

                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].paint = unselected_paint

            elif position_dropdown.value == "Blue Far":
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].paint = selected_paint

                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].paint = unselected_paint

            elif position_dropdown.value == "Red Near":
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].paint = selected_paint

                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].paint = unselected_paint

            elif position_dropdown.value == "Red Far":
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].paint = selected_paint

                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].paint = unselected_paint
                _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].paint = unselected_paint

        page.update()

    def position_change(e):
        square_change()
        direction_pos_change()

    def button_advanced_settings_on():
        if is_position_changed and is_rotation_changed:
            button_advanced_settings.disabled = False

    def switch_start_rotation(e):
        enable_rotation_arrow()
        direction_pos_change()

        is_rotation_changed = True

        if position_dropdown.value is not None:
            is_position_changed = True

        if is_position_changed and is_rotation_changed:
            button_advanced_settings.disabled = False

    def configuration_dropdown_changed(e):
        if e.control.value != "Nothing":
            e.control.parent.parent.controls[1].disabled = False
            e.control.parent.parent.controls[1].label = "Enter a device name"
        else:
            e.control.parent.parent.controls[1].disabled = True
            e.control.parent.parent.controls[1].label = "NO DEVICE ATTACHED"
            e.control.parent.parent.controls[1].value = ''

        page.update()

    def close_configuration(e):
        _expansion_hub_tile.title.color = ColorScheme.primary
        _control_hub_tile.title.color = ColorScheme.primary
        _configure_device_column.controls[0].value = "Configure Device:"
        _configure_device_column.controls[1].value = "No device selected"
        _select_device_to_configure_container.content.controls[0] = Column(
            [
                select_device_to_configure_title,
                _expansion_hub_tile,
                _control_hub_tile
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

        page.update()

    def save_config_data(e):
        global motors, servos, digital_devices, analog_input_devices, i2c0, i2c1, i2c2, i2c3, control_dict, expansion_dict

        motors = [
            _motor_tile_row.controls[0].controls[0].controls[1].value,
            _motor_tile_row.controls[2].controls[0].controls[1].value,
            _motor_tile_row.controls[4].controls[0].controls[1].value,
            _motor_tile_row.controls[6].controls[0].controls[1].value,
        ]

        servos = [
            [_servo_tile_row.controls[0].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[0].controls[0].controls[1].value],
            [_servo_tile_row.controls[2].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[2].controls[0].controls[1].value],
            [_servo_tile_row.controls[4].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[4].controls[0].controls[1].value],
            [_servo_tile_row.controls[6].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[6].controls[0].controls[1].value],
            [_servo_tile_row.controls[8].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[8].controls[0].controls[1].value],
            [_servo_tile_row.controls[10].controls[0].controls[0].controls[1].value,
             _servo_tile_row.controls[10].controls[0].controls[1].value]
        ]

        digital_devices = [
            [_digital_devices_tile_row.controls[0].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[0].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[2].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[2].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[4].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[4].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[6].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[6].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[8].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[8].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[10].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[10].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[12].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[12].controls[0].controls[1].value],
            [_digital_devices_tile_row.controls[14].controls[0].controls[0].controls[1].value,
             _digital_devices_tile_row.controls[14].controls[0].controls[1].value]
        ]

        analog_input_devices = [
            [_analog_input_tile_row.controls[0].controls[0].controls[0].controls[1].value,
             _analog_input_tile_row.controls[0].controls[0].controls[1].value],
            [_analog_input_tile_row.controls[2].controls[0].controls[0].controls[1].value,
             _analog_input_tile_row.controls[2].controls[0].controls[1].value],
            [_analog_input_tile_row.controls[4].controls[0].controls[0].controls[1].value,
             _analog_input_tile_row.controls[4].controls[0].controls[1].value],
            [_analog_input_tile_row.controls[6].controls[0].controls[0].controls[1].value,
             _analog_input_tile_row.controls[6].controls[0].controls[1].value],
        ]

        i2c0, i2c1, i2c2, i2c3 = [], [], [], []

        for control in range(len(_i2c0_tile_row.controls)):
            i2c0.append([_i2c0_tile_row.controls[control].controls[0].controls[0].controls[1].value,
                         _i2c0_tile_row.controls[control].controls[0].controls[1].value])

        for control in range(len(_i2c1_tile_row.controls)):
            i2c1.append([_i2c1_tile_row.controls[control].controls[0].controls[0].controls[1].value,
                         _i2c1_tile_row.controls[control].controls[0].controls[1].value])

        for control in range(len(_i2c2_tile_row.controls)):
            i2c2.append([_i2c2_tile_row.controls[control].controls[0].controls[0].controls[1].value,
                         _i2c2_tile_row.controls[control].controls[0].controls[1].value])

        for control in range(len(_i2c3_tile_row.controls)):
            i2c3.append([_i2c3_tile_row.controls[control].controls[0].controls[0].controls[1].value,
                         _i2c3_tile_row.controls[control].controls[0].controls[1].value])

        if device_name_during_configuration.value == "Control Hub":
            control_dict = {
                "motors": motors,
                "servos": servos,
                "digital_devices": digital_devices,
                "i2c0": i2c0,
                "i2c1": i2c1,
                "i2c2": i2c2,
                "i2c3": i2c3
            }
        else:
            expansion_dict = {
                "motors": motors,
                "servos": servos,
                "digital_devices": digital_devices,
                "i2c0": i2c0,
                "i2c1": i2c1,
                "i2c2": i2c2,
                "i2c3": i2c3
            }

        close_configuration(None)
        page.update()

    def load_config_data():
        if device_name_during_configuration.value == "Control Hub":
            for i in range(0, 7, 2):
                _motor_tile_row.controls[i].controls[0].controls[1].value = control_dict['motors'][int(i / 2)]
        else:
            for i in range(0, 7, 2):
                _motor_tile_row.controls[i].controls[0].controls[1].value = expansion_dict['motors'][int(i / 2)]

        page.update()

    def i2c_device_add(e):
        _edit_configuration_column.controls[len(_edit_configuration_column.controls) - 1].controls.append(
            Row(
                [
                    Column(
                        [
                            Row(
                                [
                                    Text(
                                        value=(len(_edit_configuration_column.controls[
                                                       len(_edit_configuration_column.controls) - 1].controls)),
                                        size=18,
                                        font_family="InterMedium"
                                    ),
                                    Dropdown(
                                        options=[
                                            dropdown.Option("Nothing"),
                                            dropdown.Option("Adafruit Color Sensor"),
                                            dropdown.Option("HuskyLens"),
                                            dropdown.Option("MR Color Sensor"),
                                            dropdown.Option("MR Compass Sensor"),
                                            dropdown.Option("MR Gyro"),
                                            dropdown.Option("MR IR Seeker v3"),
                                            dropdown.Option("MR Range Sensor"),
                                            dropdown.Option("REV 2M Distance Sensor"),
                                            dropdown.Option("REV Color Sensor V3"),
                                            dropdown.Option("REV Color/Range Sensor"),
                                            dropdown.Option("REV internal IMU")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    ),
                                    IconButton(icon=icons.DELETE_SHARP, icon_color="#fad201")
                                ]
                            ),
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
                        ]
                    )
                ]
            )
        )

        page.update()

    def device_tile_clicked(e):
        e.control.title.color = "#f4c430"
        selected_device = e.control.title.value

        _configure_device_column.controls[1].value = selected_device
        _configure_device_column.controls[1].color = ColorScheme.primary

        if selected_device == "Control Hub":
            _expansion_hub_tile.title.color = ColorScheme.primary
        else:
            _control_hub_tile.title.color = ColorScheme.primary

        load_config_data()
        page.update()

    def tile_clicked(e):
        if _expansion_hub_tile.title.color == "#f4c430" or _control_hub_tile.title.color == "#f4c430":
            _select_device_to_configure_container.content.controls.clear()
            _select_device_to_configure_container.content.controls.append(_edit_configuration_column)
            _select_device_to_configure_container.content.controls[0].controls[0].controls.append(
                _config_control_buttons)
            _edit_configuration_column.controls[0].controls[0].value = e.control.title.value
            _configure_device_column.controls[1].color = ColorScheme.primary
        else:
            _configure_device_column.controls[1].color = "#ce2029"

        if len(_edit_configuration_column.controls) > 1:
            _edit_configuration_column.controls.pop()

        if len(_edit_configuration_column.controls[0].controls) > 2:
            _edit_configuration_column.controls[0].controls.pop()

        if "I2C" in device_configure_title.value and len(_config_control_buttons.controls) < 3:
            _config_control_buttons.controls.append(add_configuration)
        elif ("I2C" not in device_configure_title.value and len(_config_control_buttons.controls) == 3) or len(
                _config_control_buttons.controls) > 3:
            _config_control_buttons.controls.pop()


        if device_configure_title.value == "Motors":
            _edit_configuration_column.controls.append(_motor_tile_row)
        elif device_configure_title.value == "Servos":
            _edit_configuration_column.controls.append(_servo_tile_row)
        elif device_configure_title.value == "Digital Devices":
            _edit_configuration_column.controls.append(_digital_devices_tile_row)
        elif device_configure_title.value == "Analog Input Devices":
            _edit_configuration_column.controls.append(_analog_input_tile_row)
        elif device_configure_title.value == "I2C Bus 0":
            _edit_configuration_column.controls.append(_i2c0_tile_row)
        elif device_configure_title.value == "I2C Bus 1":
            _edit_configuration_column.controls.append(_i2c1_tile_row)
        elif device_configure_title.value == "I2C Bus 2":
            _edit_configuration_column.controls.append(_i2c2_tile_row)
        elif device_configure_title.value == "I2C Bus 3":
            _edit_configuration_column.controls.append(_i2c3_tile_row)

        page.update()

    selected_paint = ft.Paint(stroke_width=5, style=ft.PaintingStyle.STROKE, color="#009900")
    unselected_paint = ft.Paint(style=ft.PaintingStyle.FILL, color=colors.TRANSPARENT)
    cp = ft.canvas.Canvas(
        [
            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1150, 9),
                    ft.canvas.Path.LineTo(-1060, 9),
                    ft.canvas.Path.LineTo(-1060, 99),
                    ft.canvas.Path.LineTo(-1150, 99),
                    ft.canvas.Path.LineTo(-1150, 9)
                ],
                paint=unselected_paint,
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-710, 9),
                    ft.canvas.Path.LineTo(-620, 9),
                    ft.canvas.Path.LineTo(-620, 99),
                    ft.canvas.Path.LineTo(-710, 99),
                    ft.canvas.Path.LineTo(-710, 9)
                ],
                paint=unselected_paint
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1150, 189),
                    ft.canvas.Path.LineTo(-1060, 189),
                    ft.canvas.Path.LineTo(-1060, 288),
                    ft.canvas.Path.LineTo(-1150, 288),
                    ft.canvas.Path.LineTo(-1150, 189)
                ],
                paint=unselected_paint
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-710, 189),
                    ft.canvas.Path.LineTo(-620, 189),
                    ft.canvas.Path.LineTo(-620, 288),
                    ft.canvas.Path.LineTo(-710, 288),
                    ft.canvas.Path.LineTo(-710, 189)
                ],
                paint=unselected_paint
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1105, 25),
                    ft.canvas.Path.LineTo(-1105, 55),
                    ft.canvas.Path.MoveTo(-1105, 25),
                    ft.canvas.Path.LineTo(-1120, 40),
                    ft.canvas.Path.MoveTo(-1105, 25),
                    ft.canvas.Path.LineTo(-1090, 40),
                ],
                paint=selected_paint,
                visible=False
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1130, 54),
                    ft.canvas.Path.LineTo(-1105, 54),
                    ft.canvas.Path.MoveTo(-1130, 54),
                    ft.canvas.Path.LineTo(-1115, 40),
                    ft.canvas.Path.MoveTo(-1130, 54),
                    ft.canvas.Path.LineTo(-1115, 68),
                ],
                paint=selected_paint,
                visible=False
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1105, 83),
                    ft.canvas.Path.LineTo(-1105, 55),
                    ft.canvas.Path.MoveTo(-1105, 83),
                    ft.canvas.Path.LineTo(-1120, 68),
                    ft.canvas.Path.MoveTo(-1105, 83),
                    ft.canvas.Path.LineTo(-1090, 68),
                ],
                paint=selected_paint,
                visible=False
            ),

            ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(-1080, 54),
                    ft.canvas.Path.LineTo(-1105, 54),
                    ft.canvas.Path.MoveTo(-1080, 54),
                    ft.canvas.Path.LineTo(-1095, 40),
                    ft.canvas.Path.MoveTo(-1080, 54),
                    ft.canvas.Path.LineTo(-1095, 68),
                ],
                paint=selected_paint,
                visible=False
            ),
        ],
        width=float("inf"),
        expand=True,
    )

    user_greetings = Text(user_phrases[1], size=24, font_family="MontserratRegular")
    title = Text(user_phrases[8], size=24, font_family="InterMedium")
    go = ElevatedButton(user_phrases[9], on_click=start_work, width=350, height=60)
    user_info_language = Text(user_phrases[2], size=24, font_family="MontserratRegular")
    english = ElevatedButton("English", on_click=set_eng, width=350, height=60)
    russian = ElevatedButton("Русский", on_click=set_rus, width=350, height=60)
    confirm_language = FilledButton(user_phrases[0], disabled=True, on_click=lambda _: page.go('/terms'))
    terms_of_use_title = Text(user_phrases[3], font_family="MontserratRegularBoldItalic")
    terms_of_use = Text(user_phrases[4], size=18, font_family="MontserratRegular")
    terms_agree_checkbox = Checkbox(user_phrases[5], False, on_change=terms_agree)
    confirm_terms_agree = FilledButton(user_phrases[6], disabled=True, on_click=home)
    create_page_title = Text("Введите название новой программы:", size=24, font_family="RubikRegular")
    new_program_title = TextField(label="Title", hint_text="Please enter title here", on_change=validate_name,
                                  autofocus=True)
    continue_create = FilledTonalButton("Continue", icon=icons.CHECK, on_click=name_new_program, disabled=True)

    start_position = Text("Выберите стартовую позицию", size=18, font_family="RubikRegular")
    position_dropdown = Dropdown(
        options=[
            ft.dropdown.Option("Blue Near"),
            ft.dropdown.Option("Blue Far"),
            ft.dropdown.Option("Red Near"),
            ft.dropdown.Option("Red Far")
        ],
        on_change=position_change
    )

    def switch_create_tabs(e):
        create_program_tabs.selected_index = 1
        page.update()

    start_rotation = Text("Выберите начальное положение", size=18, font_family="RubikRegular")
    rotation_button = FloatingActionButton(icon=icons.ARROW_FORWARD, on_click=switch_start_rotation)
    button_advanced_settings = ElevatedButton(text="Продолжить", disabled=True, on_click=switch_create_tabs)

    _position_column = Column(
        [
            start_position,
            position_dropdown,
            Divider(height=20, color="surface,0.0"),
            Row([start_rotation, rotation_button]),
            Divider(height=100, color="surface,0.0"),
            button_advanced_settings
        ],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=MainAxisAlignment.CENTER
    )

    def create_program(e):
        programs.append(new_program_title)
        page.client_storage.set("programs", programs)

    page.appbar = CupertinoAppBar(
        bgcolor=colors.SURFACE_VARIANT,
        trailing=IconButton(icons.CLOSE, on_click=exit_app),
        middle=Text("My Program | Version 1", font_family="MontserratRegularBoldItalic"),
        leading=IconButton(icons.SUNNY, on_click=change_theme)
    )

    create_program = Column(
        [Text("Введите название новой программы:", size=20, font_family="RubikRegular"),
         new_program_title,
         continue_create],
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        expand=True
    )

    select_device_to_configure_title = Text("Select a device to configure:", font_family="InterMedium", size=20)
    device_configure_title = Text("Configure Device:", font_family="InterMedium", size=20)

    _expansion_hub_tile = CupertinoListTile(
        leading=ft.Icon(name=ft.icons.SMARTPHONE),
        title=ft.Text("Expansion Hub"),
        subtitle=ft.Text("Click on tile to continue >>>"),
        on_click=device_tile_clicked,
        notched=True
    )

    _control_hub_tile = CupertinoListTile(
        leading=ft.Icon(name=ft.icons.SMARTPHONE),
        title=ft.Text("Control Hub"),
        subtitle=ft.Text("Click on tile to continue >>>"),
        on_click=device_tile_clicked,
        notched=True
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

    device_name_during_configuration = Text("No devices selected")
    configure_motors = ListTile(
        title=ft.Text("Motors"),
        subtitle=ft.Text("Configure Motors"),
        on_click=tile_clicked
    )

    configure_servos = ListTile(
        title=ft.Text("Servos"),
        subtitle=ft.Text("Configure Servos"),
        on_click=tile_clicked
    )

    configure_dig_devices = ListTile(
        title=ft.Text("Digital Devices"),
        subtitle=ft.Text("Configure Digital Devices"),
        on_click=tile_clicked
    )

    configure_analog = ListTile(
        title=ft.Text("Analog Input Devices"),
        subtitle=ft.Text("Configure Analog Input Devices"),
        on_click=tile_clicked
    )

    configure_i2c0 = ListTile(
        title=ft.Text("I2C Bus 0"),
        subtitle=ft.Text("Configure I2C Bus 0"),
        on_click=tile_clicked
    )

    configure_i2c1 = ListTile(
        title=ft.Text("I2C Bus 1"),
        subtitle=ft.Text("Configure I2C Bus 1"),
        on_click=tile_clicked
    )

    configure_i2c2 = ListTile(
        title=ft.Text("I2C Bus 2"),
        subtitle=ft.Text("Configure I2C Bus 2"),
        on_click=tile_clicked
    )

    configure_i2c3 = ListTile(
        title=ft.Text("I2C Bus 3"),
        subtitle=ft.Text("Configure I2C Bus 3"),
        on_click=tile_clicked
    )

    save_configuration = ElevatedButton(icon=icons.SAVE_SHARP, color="#fad201", text="Save", on_click=save_config_data)
    cancel_configuration = ElevatedButton(color="#fad201", text="Cancel", on_click=close_configuration)
    add_configuration = ElevatedButton(icon=icons.ADD_SHARP, color="#fad201", text="Add", on_click=i2c_device_add)

    _config_control_buttons = Row(
        [
            save_configuration,
            cancel_configuration
        ],
    )

    _device_list_column = Column(
        [
            configure_motors,
            Divider(thickness=2, height=8),
            configure_servos,
            Divider(thickness=2, height=8),
            configure_dig_devices,
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
        scroll="auto",
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
                        ]
                    )
                ]
            ),
        ],
        expand=True,
        scroll="auto"
    )

    _analog_input_tile_row = Column(
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
                                            dropdown.Option("Analog Input"),
                                            dropdown.Option("MR Optical Distance Sensor"),
                                            dropdown.Option("MR Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                                            dropdown.Option("Analog Input"),
                                            dropdown.Option("MR Optical Distance Sensor"),
                                            dropdown.Option("MR Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                                            dropdown.Option("Analog Input"),
                                            dropdown.Option("MR Optical Distance Sensor"),
                                            dropdown.Option("MR Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
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
                                            dropdown.Option("Analog Input"),
                                            dropdown.Option("MR Optical Distance Sensor"),
                                            dropdown.Option("MR Touch Sensor")
                                        ],
                                        value="Nothing",
                                        on_change=configuration_dropdown_changed
                                    )
                                ]
                            ),
                            TextField(label="NO DEVICE ATTACHED", disabled=True)
                        ]
                    )
                ]
            ),
        ],
        expand=True,
        scroll="auto"
    )

    _i2c0_tile_row = Column(expand=True, scroll="auto")
    _i2c1_tile_row = Column(expand=True, scroll="auto")
    _i2c2_tile_row = Column(expand=True, scroll="auto")
    _i2c3_tile_row = Column(expand=True, scroll="auto")

    _edit_configuration_column = Column(
        [
            Column([device_configure_title]),
        ],
        expand=True,
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
            color=ft.colors.BLUE_GREY_300,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
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
            color=ft.colors.BLUE_GREY_300,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
    )

    prog_set = Text("New Program", font_family="InterMedium")
    text_upd = [confirm_language, user_greetings, user_info_language, terms_of_use_title]
    base_column = Column([title, go])
    _main_column = Column([user_greetings, user_info_language, english, russian, confirm_language])
    _main_container = Container(
        width=400,
        height=600,
        content=_main_column,
        border_radius=20,
        padding=20,
        adaptive=True,
        image_src="pictures\main_dark_theme.jpg",
        bgcolor="black",
        image_opacity=0.25
    )

    _terms_column = Column([terms_of_use, terms_agree_checkbox, confirm_terms_agree])
    _terms_container = Container(
        width=600,
        height=600,
        border_radius=20,
        padding=20,
        bgcolor="black",
        content=_terms_column
    )

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Create", on_click=lambda _: page.go('/create')),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FILE_OPEN_OUTLINED, selected_icon=ft.icons.FILE_OPEN, label="Your Programs"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.FAVORITE_BORDER),
                selected_icon_content=ft.Icon(ft.icons.FAVORITE),
                label="Favorite",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.INFO_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.INFO_SHARP),
                label="Info",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    _create_body_container = Container(
        width=800,
        height=800,
        border_radius=20,
        padding=20,
        adaptive=True,
        image_src="pictures\centerstage_field.png",
        bgcolor="black",
    )
    _create_body = Column([Row([_create_body_container])],
                          alignment=MainAxisAlignment.CENTER,
                          horizontal_alignment=CrossAxisAlignment.CENTER)

    create_program_tabs = Tabs(
        selected_index=0,
        animation_duration=300,
        scrollable=False,
        tabs=[
            Tab(
                text="Set StartPos",
                content=Row(
                    controls=[_create_body,
                              VerticalDivider(width=100, color="surface,0"),
                              _position_column, cp],
                    alignment=MainAxisAlignment.CENTER
                )
            ),
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
            Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
        on_change=check_create_status
    )

    page_create_tab1 = [_create_body,
                        VerticalDivider(width=100, color="surface,0"),
                        _position_column]

    _home_create_body = Row(
        [
            create_program_tabs
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
                    Container(
                        width=400,
                        height=600,
                        content=base_column,
                        border_radius=20,
                        padding=20,
                        adaptive=True,
                        image_opacity=0.25
                    )
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=25
            )
        )

        if page.route == "/greet":
            page.views.append(
                View(
                    route='/greet',
                    controls=[
                        CupertinoAppBar(
                            bgcolor=colors.SURFACE_VARIANT,
                            trailing=IconButton(icons.CLOSE, on_click=exit_app),
                            middle=Text("My Program | Version 1", font_family="MontserratRegularBoldItalic"),
                            leading=IconButton(icons.SUNNY, on_click=change_theme)
                        ),
                        _main_container
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )

        if page.route == '/terms':
            page.views.append(
                View(
                    route='/terms',
                    controls=[
                        CupertinoAppBar(
                            bgcolor=colors.SURFACE_VARIANT,
                            trailing=IconButton(icons.CLOSE, on_click=exit_app),
                            middle=terms_of_use_title,
                            leading=IconButton(icons.SUNNY, on_click=change_theme)
                        ),
                        _terms_container
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )

        if page.route == '/home':
            page.views.append(
                View(
                    route='/home',
                    controls=[
                        AppBar(
                            bgcolor=colors.SURFACE_VARIANT,
                            title=Text("Top Secret", font_family="InterMedium"),
                            # trailing=IconButton(icons.CLOSE, on_click=exit_app),
                            # middle=home_title,
                            leading=IconButton(icons.SUNNY, on_click=change_theme)
                        ),
                        Row(
                            [
                                rail,
                                VerticalDivider(width=1),
                                page_body
                            ],
                            expand=True,
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.CENTER
                        )
                    ]
                )
            )

        if page.route == '/create':
            page.views.append(
                View(
                    route='/create',
                    controls=[
                        AppBar(
                            bgcolor=colors.SURFACE_VARIANT,
                            title=Text("Create Program", font_family="InterMedium"),
                            # trailing=IconButton(icons.CLOSE, on_click=exit_app),
                            # middle=home_title,
                            leading=IconButton(icons.SUNNY, on_click=change_theme)
                        ),
                        create_program
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )

        page.update()

        if page.route == '/create/home':
            page.views.append(
                View(
                    route='/create/home',
                    controls=[
                        AppBar(
                            bgcolor=colors.SURFACE_VARIANT,
                            title=prog_set,
                            # trailing=IconButton(icons.CLOSE, on_click=exit_app),
                            # middle=home_title,
                            leading=IconButton(icons.SUNNY, on_click=change_theme)
                        ),
                        _home_create_body
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )

        page.update()

    def page_adaptive(e):
        print("New page size: x =", page.window_width, ",y =", page.window_height)

        adaptive_size = (page.window_height - 700)
        if adaptive_size > 262:
            adaptive_size = 262

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].elements[0].y = 9 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].elements[1].y = 9 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].elements[2].y = 99 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].elements[3].y = 99 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[0].elements[4].y = 9 - adaptive_size / 2

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].elements[0].y = 9 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].elements[1].y = 9 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].elements[2].y = 99 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].elements[3].y = 99 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[1].elements[4].y = 9 - adaptive_size / 2

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].elements[0].y = 186 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].elements[1].y = 186 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].elements[2].y = 276 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].elements[3].y = 276 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[2].elements[4].y = 186 - adaptive_size / 2

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].elements[0].y = 186 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].elements[1].y = 186 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].elements[2].y = 276 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].elements[3].y = 276 - adaptive_size / 2
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[3].elements[4].y = 186 - adaptive_size / 2

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            0].y = 25 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            1].y = 55 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            2].y = 25 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            3].y = 40 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            4].y = 25 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[4].elements[
            5].y = 40 - adaptive_size / 2 + delta_y

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            0].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            1].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            2].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            3].y = 40 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            4].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[5].elements[
            5].y = 68 - adaptive_size / 2 + delta_y

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            0].y = 83 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            1].y = 55 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            2].y = 83 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            3].y = 68 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            4].y = 83 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[6].elements[
            5].y = 68 - adaptive_size / 2 + delta_y

        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            0].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            1].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            2].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            3].y = 40 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            4].y = 54 - adaptive_size / 2 + delta_y
        _home_create_body.controls[0].tabs[0].content.controls[3].shapes[7].elements[
            5].y = 68 - adaptive_size / 2 + delta_y

        _home_create_body.controls[0].tabs[1].content.controls[1].width = page.window_width / 2.5
        _home_create_body.controls[0].tabs[1].content.controls[1].height = page.window_height - 250
        _home_create_body.controls[0].tabs[1].content.controls[2].width = page.window_width / 2.5
        _home_create_body.controls[0].tabs[1].content.controls[2].height = page.window_height - 250

        _home_create_body.controls[0].tabs[1].content.controls[0].width = page.window_width / 15
        _home_create_body.controls[0].tabs[1].content.controls[3].width = page.window_width / 15

        page.update()

    page.on_route_change = change_route
    page.go(page.route)

    page.on_resize = page_adaptive


if __name__ == '__main__':
    app(target=main, assets_dir="assets")
