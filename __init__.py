# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_hide_viewport_ops

from . import hide_viewport_keymap
from . import hide_viewport_ops
from .addon import Addon


bl_info = {
    'name': 'Hide Viewport Ops',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-hide-viewport-ops/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-hide-viewport-ops/',
    'description': 'Enable shortcodes and operators for globally hide objects in viewport in all scenes'
}


def register():
    if not Addon.dev_mode():
        hide_viewport_ops.register()
        hide_viewport_keymap.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] +
              ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        hide_viewport_keymap.unregister()
        hide_viewport_ops.unregister()


if __name__ == '__main__':
    register()
