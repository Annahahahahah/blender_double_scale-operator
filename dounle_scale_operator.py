import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

class Object_Scale_Double(Operator):
    bl_idname = "object.double_scale"
    bl_label = "Object Scale Double"
    
    @classmethod
    def poll(self, context):
        return context.object is not None
    
    def execute(self, context):
        context.object.scale *= 2
        return {'FINISHED'}

classes = [Object_Scale_Double]

def register():
    for cl in classes:
        register_class(cl)
        
        
def unregister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == '__main__':
    register()
    bpy.ops.object.double_scale()