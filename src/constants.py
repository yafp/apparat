#!/usr/bin/python
"""apparat - an application launcher for linux"""

# -----------------------------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------------------------
# built-in modules
import os                           # for searching applications and file/folder/path handling



# -----------------------------------------------------------------------------------------------
# CONSTANTS (DEVELOPER)
# -----------------------------------------------------------------------------------------------
APP_NAME = 'Apparat'
APP_DESCRIPTION = 'An application launcher for linux'
APP_URL = 'https://github.com/yafp/apparat'
APP_LICENSE = 'GPL3'
APP_TRAY_TOOLTIP = 'apparat'
APP_TRAY_ICON = 'gfx/core/bt_appIcon_16.png'
APP_INI_FOLDER = os.environ['HOME']+'/.config/apparat/'
APP_INI_PATH = APP_INI_FOLDER+'apparat.ini'


## Plugins
#
#
# Internet-Search
APP_PLUGINS_INTERNET_SEARCH_TRIGGER = ('!a', '!b', '!e', '!g', '!l', '!m', '!o', '!r', '!s', '!t', '!v', '!w', '!y')
#
# Local search
APP_PLUGINS_SEARCH_LOCAL_TRIGGER = ('?')
#
# Misc
APP_PLUGINS_MISC_TRIGGER = ('!open')
#
# Nautilus
APP_PLUGINS_NAUTILUS_TRIGGER = ('!goto', '!recent', '!trash', '!network', '!net')
#
# Session
APP_PLUGINS_SESSION_TRIGGER = ('!hibernate', '!sleep', '!lock', '!logout', '!reboot', '!restart', '!shutdown', '!halt')
#
# Shell
APP_PLUGINS_SHELL_TRIGGER = ('!sh')




#APP_SEARCH_DIRS = ('/usr/bin', '~') # unused so far
