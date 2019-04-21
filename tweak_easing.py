import bpy
from random import random

class TWEAK_EASING_OT_op(bpy.types.Operator):
    bl_idname = "anim.tweak_easing"
    bl_label = "Tweak keyframe easing"


    override_back: bpy.props.BoolProperty(name="Override back", default=True)
    back: bpy.props.FloatProperty(name="Back overshoot", default=0.0)

    override_period: bpy.props.BoolProperty(name="Override period", default=True)
    period: bpy.props.FloatProperty(name="Elastic period", default=0.0)

    override_amplitude: bpy.props.BoolProperty(name="Override amplitude", default=True)
    amplitude: bpy.props.FloatProperty(name="Bounce amplitude", default=0.0)

    override_interpolate: bpy.props.BoolProperty(name="Override interpolate", default=True)
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


    override_easing: bpy.props.BoolProperty(name="Override easing", default=True)
    easing_type: bpy.props.EnumProperty(items=[
        ('AUTO', 'AUTO', 'AUTO'),
        ('EASE_IN', 'EASE_IN', 'EASE_IN'),
        ('EASE_OUT', 'EASE_OUT', 'EASE_OUT'),
        ('EASE_IN_OUT', 'EASE_IN_OUT', 'EASE_IN_OUT')
        ], name="Easing type")


    override_keyframe_type: bpy.props.BoolProperty(name="Override keyframe type", default=True)
    keyframe_type: bpy.props.EnumProperty(items=[
        ('KEYFRAME', 'KEYFRAME', 'KEYFRAME'),
        ('BREAKDOWN', 'BREAKDOWN', 'BREAKDOWN'),
        ('MOVING_HOLD', 'MOVING_HOLD', 'MOVING_HOLD'),
        ('EXTREME', 'EXTREME', 'EXTREME'),
        ('JITTER', 'JITTER', 'JITTER')
        ], name="Keyframe type")

    horizontal_position_fudge: bpy.props.FloatProperty(name="Horizontal position fudge", default=0)
    vertical_position_fudge: bpy.props.FloatProperty(name="Vertical position fudge", default=0.0)

    def execute(self, context):

        message = "Popup Values"

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
