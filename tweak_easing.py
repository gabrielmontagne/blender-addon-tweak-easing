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

    override_interpolation: bpy.props.BoolProperty(name="Override interpolate", default=True)
    interpolation: bpy.props.EnumProperty(items=[
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
    easing: bpy.props.EnumProperty(items=[
        ('AUTO', 'AUTO', 'AUTO'),
        ('EASE_IN', 'EASE_IN', 'EASE_IN'),
        ('EASE_OUT', 'EASE_OUT', 'EASE_OUT'),
        ('EASE_IN_OUT', 'EASE_IN_OUT', 'EASE_IN_OUT')
        ], name="Easing type")

    override_type: bpy.props.BoolProperty(name="Override keyframe type", default=True)
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
        for a in bpy.data.actions:
            for f in a.fcurves:
                points = f.keyframe_points
                for p in points:
                    if not p.select_control_point:
                        continue

                    if self.override_easing:
                        p.easing =  self.easing

                    if self.override_interpolation:
                        p.interpolation = self.interpolation

                    if self.override_back:
                        p.back = self.back

                    if self.override_period:
                        p.period = self.period

                    if self.override_amplitude:
                        p.amplitude = self.amplitude

                    if self.override_type:
                        p.type = self.keyframe_type

                    t,v = p.co

                    p.co = (t + random() * self.horizontal_position_fudge - (self.horizontal_position_fudge / 2), v + random() * self.vertical_position_fudge - (self.vertical_position_fudge / 2))

        f.update()

        self.report({'INFO'}, 'Done!')
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
