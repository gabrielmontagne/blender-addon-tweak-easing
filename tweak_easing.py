import bpy
from random import random

class TWEAK_EASING_OT_op(bpy.types.Operator):
    bl_idname = "anim.tweak_easing"
    bl_label = "Tweak keyframe easing"

    my_float: bpy.props.FloatProperty(name="Some Floating×Γ ---- nt")
    my_bool: bpy.props.BoolProperty(name="Toggle OOOO")
    my_string: bpy.props.StringProperty(name="StringyValue")

    interpolate_type: bpy.props.EnumProperty(items=[
        ('CONSTANT', 'CONSTANT', 'CONSTANT'),
        ('LINEAR', 'LINEAR', 'LINEAR'),
        ('BEZIER', 'BEZIER', 'BEZIER'),
        ('SINE', 'SINE', 'SINE'),
        ('QUAD', 'QUAD', 'QUAD'),
        ('CUBIC', 'CUBIC', 'CUBIC'),
        ('QUART', 'QUART', 'QUART'),
        ('QUINT', 'QUINT', 'QUINT'),
        ('EXPO', 'EXPO', 'EXPO'),
        ('CIRC', 'CIRC', 'CIRC'),
        ('BACK', 'BACK', 'BACK'),
        ('BOUNCE', 'BOUNCE', 'BOUNCE'),
        ('ELASTIC', 'ELASTIC', 'ELASTIC')
        ], name="Interpolation type")


    easing_type: bpy.props.EnumProperty(items=[
        ('AUTO', 'AUTO', 'AUTO'),
        ('EASE_IN', 'EASE_IN', 'EASE_IN'),
        ('EASE_OUT', 'EASE_OUT', 'EASE_OUT'),
        ('EASE_IN_OUT', 'EASE_IN_OUT', 'EASE_IN_OUT')
        ], name="Easing type")


    keyframe_type: bpy.props.EnumProperty(items=[
        ('KEYFRAME', 'KEYFRAME', 'KEYFRAME'),
        ('BREAKDOWN', 'BREAKDOWN', 'BREAKDOWN'),
        ('MOVING_HOLD', 'MOVING_HOLD', 'MOVING_HOLD'),
        ('EXTREME', 'EXTREME', 'EXTREME'),
        ('JITTER', 'JITTER', 'JITTER')
        ], name="Keyframe type")

    def execute(self, context):

        message = "Popup Values: %f, %d, '%s'" % \
            (self.my_float, self.my_bool, self.my_string)

        print('tons?', self.fixed_items)

        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        print('invoke', self)
        return wm.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(TWEAK_EASING_OT_op)

def unregister():
    bpy.utils.unregister_class(TWEAK_EASING_OT_op)

if __name__ == "__main__":
    register()
