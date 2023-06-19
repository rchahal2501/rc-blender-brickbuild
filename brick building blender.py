#rc- brick building blender -- Spring 2023

import bpy

# Create 4x4x4 cube 
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.active_object
cube.dimensions = (4, 4, 4)

# Add a brick texture to the cube ** Note: load brick texture file, get path
mat = bpy.data.materials.new('brick')
cube.data.materials.append(mat)
tex = bpy.data.textures.new('brick', type='IMAGE')
img = bpy.data.images.load('/path/to/brick_texture.jpg') #path varies
tex.image = img
slot = mat.texture_slots.add()
slot.texture = tex
slot.texture_coords = 'GLOBAL'
slot.mapping = 'CUBE'

# Render the scene
bpy.ops.render.render(write_still=True)
