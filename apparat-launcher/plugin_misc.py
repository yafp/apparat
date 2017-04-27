#!/usr/bin/python
"""apparat - plugin: misc"""

## general
import os
import wx

## apparat
import config
import tools



# -----------------------------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------------------------
TRIGGER = ('!open')


# -----------------------------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------------------------
def prepare_general(current_search_string, main_window):
    """Prepare General"""
    tools.debug_output('prepare_general', 'starting', 1)

    # Reset status notification back to OK
    main_window.status_notification_reset()

    if current_search_string.startswith('!open'):
        tools.debug_output('prepare_general', 'Case: Open', 1)
        prepare_plugin_misc_open(main_window)

    else:
        tools.debug_output('prepare_general', 'Error: Unexpected misc plugin command', 3)
        main_window.status_notification_display_error('Unexpected misc plugin command')

    tools.debug_output('prepare_general', 'finished', 1)


def prepare_plugin_misc_open(main_window):
    """Plugin Misc - Open - Opens file or location using xdg-open"""
    tools.debug_output('prepare_plugin_misc_open', 'starting', 1)
    main_window.plugin__update_general_ui_information('Misc (Open)') ## update plugin info

    ## application buttons
    main_window.ui__bt_selected_app_img = wx.Image('gfx/plugins/misc/'+str(config.TARGET_ICON_SIZE)+'/open.png', wx.BITMAP_TYPE_PNG)
    main_window.ui__bt_selected_app.SetBitmap(main_window.ui__bt_selected_app_img.ConvertToBitmap())
    main_window.ui__bt_selected_app.SetToolTipString('Open')

    if(len(main_window.ui__cb_search.GetValue()) > 6) and  (main_window.ui__cb_search.GetValue()[6:] != ''):
        ## parameter buttons
        main_window.ui__bt_selected_parameter.SetToolTipString('Open')
        main_window.ui__bt_selected_parameter_img = wx.Image('gfx/core/'+str(config.TARGET_ICON_SIZE)+'/execute.png', wx.BITMAP_TYPE_PNG)
        main_window.ui__bt_selected_parameter.SetBitmap(main_window.ui__bt_selected_parameter_img.ConvertToBitmap())

        ## set parameter
        if (main_window.ui__cb_search.GetValue()[6:7] == '~'):
            tools.debug_output('prepare_plugin_misc_open', 'Replacing ~', 1)
            home = os.environ['HOME']
            main_window.ui__txt_selected_parameter.SetValue(home+main_window.ui__cb_search.GetValue()[7:]) # possible parameter
        else:
            main_window.ui__txt_selected_parameter.SetValue(main_window.ui__cb_search.GetValue()[6:]) # possible parameter

        ## set command
        main_window.ui__txt_selected_app.SetValue('xdg-open')
    else:
        tools.debug_output('prepare_plugin_misc_open', 'Incomplete input, waiting for more...', 2)