# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_hide_viewport_ops

import bpy


class HIDE_VIEWPORT_KeyMap:

    _keymaps = []

    @classmethod
    def register(cls, context):
        # add new key map
        if context.window_manager.keyconfigs.addon:
            keymap = context.window_manager.keyconfigs.addon.keymaps.new(
                name='Object Mode'
            )
            # add keys
            keymap_item = keymap.keymap_items.new('object.hide_viewport', 'Y', 'PRESS')
            keymap_item.properties.mode = 'HIDE'
            keymap_item = keymap.keymap_items.new('object.hide_viewport', 'Y', 'PRESS', alt=True)
            keymap_item.properties.mode = 'UNHIDE'
            cls._keymaps.append((keymap, keymap_item))

    @classmethod
    def unregister(cls):
        for keymap, keymap_item in cls._keymaps:
            keymap.keymap_items.remove(keymap_item)
        cls._keymaps.clear()


def register():
    HIDE_VIEWPORT_KeyMap.register(context=bpy.context)


def unregister():
    HIDE_VIEWPORT_KeyMap.unregister()
