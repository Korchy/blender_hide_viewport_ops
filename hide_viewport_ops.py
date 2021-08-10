# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_hide_viewport_ops

from bpy.props import EnumProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .hide_viewport import HideViewport

class OBJECT_OT_hide_viewport(Operator):
    bl_idname = 'object.hide_viewport'
    bl_label = 'Hide Viewport'
    bl_description = 'Globally hide objects in viewport for all scenes'
    bl_options = {'UNDO'}

    mode: EnumProperty(
        name='mode',
        items=[
            ('HIDE', 'Hide', 'Hide'),
            ('UNHIDE', 'Unhide', 'Unhide')
        ],
        default='HIDE'
    )

    def execute(self, context):
        if self.mode == 'HIDE':
            HideViewport.hide_viewport(
                objects=context.selected_objects
            )
        elif self.mode == 'UNHIDE':
            HideViewport.hide_viewport_clear(
                context=context
            )
        return {'FINISHED'}


def register():
    register_class(OBJECT_OT_hide_viewport)


def unregister():
    unregister_class(OBJECT_OT_hide_viewport)
