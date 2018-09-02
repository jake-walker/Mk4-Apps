"""Default homescreen

This is the default homescreen for the Tilda Mk4.
It gets automatically installed when a badge is
newly activated or reset.
"""

___name___         = "Homescreen (Custom)"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = ["homescreen", "shared/avatar.png", "shared/sponsors.png"]
___launchable___   = False
___bootstrapped___ = True

import ugfx
from homescreen import *
import time

# Padding for name
intro_height = 30
intro_text = "Hi! I'm"
name_height = 60
extra_height = 30
extra_text = "www.jakew.me"
status_height = 20
info_height = 30
logo_path = "shared/avatar.png"
logo_height = 150
logo_width = 150

# Maximum length of name before downscaling
max_name = 8

# Background stuff
init()
ugfx.clear(ugfx.html_color(0x2274A6))

# Colour stuff
style = ugfx.Style()
style.set_enabled([ugfx.WHITE, ugfx.html_color(0x2274A6), ugfx.html_color(0x2274A6), ugfx.html_color(0x2274A6)])
style.set_background(ugfx.html_color(0x2274A6))
ugfx.set_default_style(style)

# Logo stuff
ugfx.display_image(
    int((ugfx.width() - logo_width) / 2),
    int((extra_height + name_height + intro_height + 10)),
    logo_path
)



# Draw for people to see
ugfx.orientation(90)
# Draw introduction
ugfx.set_default_font(ugfx.FONT_TITLE)
ugfx.Label(0, ugfx.height() - extra_height - name_height - intro_height, ugfx.width(), intro_height, intro_text, justification=ugfx.Label.CENTER)
ugfx.Label(0, ugfx.height() - extra_height, ugfx.width(), extra_height, extra_text, justification=ugfx.Label.CENTER)
# Process name
name_setting = name("Set your name in the settings app")
if len(name_setting) <= max_name:
    ugfx.set_default_font(ugfx.FONT_NAME)
else:
    ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
# Draw name
ugfx.Label(0, ugfx.height() - extra_height - name_height, ugfx.width(), name_height, name_setting, justification=ugfx.Label.CENTER)



# Draw for wearer to see
ugfx.orientation(270)

ugfx.set_default_font(ugfx.FONT_SMALL)
status = ugfx.Label(0, ugfx.height() - status_height, ugfx.width(), status_height, "", justification=ugfx.Label.CENTER)

# update loop
while True:
    text = "";
    value_wifi_strength = wifi_strength()
    value_battery = battery()
    if value_wifi_strength:
        text += "Wi-Fi: %s%%, " % int(value_wifi_strength)
    if value_battery:
        text += "Battery: %s%%" % int(value_battery)
    status.text(text)
    sleep_or_exit(0.5)
