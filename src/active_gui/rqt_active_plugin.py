#!/usr/bin/python
import rospy
from qt_gui.plugin import Plugin
from active_gui.active_widgets import ActiveEUPWidget


class ActiveGUIPlugin(Plugin):
    def __init__(self, context):
        super(ActiveGUIPlugin, self).__init__(context)
        self._widget = ActiveEUPWidget()
        context.add_widget(self._widget)

    def shutdown_plugin(self):
        self._widget.log_loaded_program()
