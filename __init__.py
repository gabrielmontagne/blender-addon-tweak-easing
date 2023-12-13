import bpy
from random import random

bl_info = {
    'name': 'Select and tweak keyframe interpolations',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Select and tweak easings and interpolations of animation keyframes',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-tweak-easing/issues',
    'category': 'Render'
}

class CENTER_2D_CURSOR_VALUE_OT_op(bpy.types.Operator):
    bl_idname = "rojored.center_2d_cursor_value"
    bl_label = "Center 2D cursor value on graph editor"

    @classmethod
    def poll(cls, context):
        return contex.space_data_.type == 'GRAPH_EDITOR'

    def execute(self, context):
        context.space_data.cursor_position_y = 0
        return {'FINISHED'}

class RANDOM_KEYFRAME_OT_select(bpy.types.Operator):
    bl_idname = "rojored.random_select"
    bl_label = "Select random keyframe"
    bl_options = {'PRESET'}

    probability: bpy.props.FloatProperty(name="Selection probabilty", default=0.5, min=0.0, max=1.0)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        for a in bpy.data.actions:
            for f in a.fcurves:
                points = f.keyframe_points
                for p in points:
                    p.select_control_point = self.probability >= random()
        return {'FINISHED'}

class TWEAK_EASING_OT_op(bpy.types.Operator):
    bl_idname = "rojored.tweak_easing"
    bl_label = "Tweak keyframe easing"
    bl_options = {'PRESET'}

    override_back: bpy.props.BoolProperty(name="Override back", default=False)
    back: bpy.props.FloatProperty(name="Back overshoot", default=0.0)

    override_period: bpy.props.BoolProperty(name="Override period", default=False)
    period: bpy.props.FloatProperty(name="Elastic period", default=0.0)

    override_amplitude: bpy.props.BoolProperty(name="Override amplitude", default=False)
    amplitude: bpy.props.FloatProperty(name="Bounce amplitude", default=0.0)

    override_interpolation: bpy.props.BoolProperty(name="Override interpolate", default=False)
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
        ], name="Interpolation type", default='LINEAR')

    override_easing: bpy.props.BoolProperty(name="Override easing", default=False)
    easing: bpy.props.EnumProperty(items=[
        ('AUTO', 'AUTO', 'AUTO'),
        ('EASE_IN', 'EASE_IN', 'EASE_IN'),
        ('EASE_OUT', 'EASE_OUT', 'EASE_OUT'),
        ('EASE_IN_OUT', 'EASE_IN_OUT', 'EASE_IN_OUT')
        ], name="Easing type")

    override_type: bpy.props.BoolProperty(name="Override keyframe type", default=False)
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
        return wm.invoke_props_dialog(self)

class SET_LOCROT_KEYING_SET_OT(bpy.types.Operator):
    bl_idname = "rojored.set_locrot_keying_set"
    bl_label = "Set Loc Rot keying set"

    def execute(self, context):
        bpy.ops.anim.keying_set_active_set(type='BUILTIN_KSI_LocRot')
        return {'FINISHED'}

class SET_LOCROTSCALE_KEYING_SET_OT(bpy.types.Operator):
    bl_idname = "rojored.set_locrotsca_keying_set"
    bl_label = "Set Loc Rot Scale keying set"

    def execute(self, context):
        bpy.ops.anim.keying_set_active_set(type='LocRotScale')
        return {'FINISHED'}

def register():
    bpy.utils.register_class(TWEAK_EASING_OT_op)
    bpy.utils.register_class(RANDOM_KEYFRAME_OT_select)
    bpy.utils.register_class(CENTER_2D_CURSOR_VALUE_OT_op)
    bpy.utils.register_class(SET_LOCROTSCALE_KEYING_SET_OT)
    bpy.utils.register_class(SET_LOCROT_KEYING_SET_OT)

def unregister():
    bpy.utils.unregister_class(TWEAK_EASING_OT_op)
    bpy.utils.unregister_class(RANDOM_KEYFRAME_OT_select)
    bpy.utils.unregister_class(CENTER_2D_CURSOR_VALUE_OT_op)
    bpy.utils.unregister_class(SET_LOCROTSCALE_KEYING_SET_OT)
    bpy.utils.unregister_class(SET_LOCROT_KEYING_SET_OT)

if __name__ == "__main__":
    register()
