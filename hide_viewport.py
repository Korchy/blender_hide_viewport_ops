# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_hide_viewport_ops

class HideViewport:

    @staticmethod
    def hide_viewport(objects=None):
        # hide objects in viewport globally for all scenes
        objects = objects if objects else []
        for obj in objects:
            obj.hide_viewport = True

    @staticmethod
    def hide_viewport_clear(context):
        # show hidden objects in viewport globally for all scenes
        for obj in context.blend_data.objects:
            if obj.hide_viewport:
                obj.hide_viewport = False
                obj.select_set(True)
