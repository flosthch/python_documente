from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()
grass_texture = load_texture('assets/grass.png')
stone_texture = load_texture('assets/stone2.png')
brick_texture = load_texture('assets/wood2.png')
dirt_texture  = load_texture('assets/dirt2.png')
sky_texture   = load_texture('assets/skybox.png')
bedrock_texture   = load_texture('assets/bedrock.png')
stamm_texture   = load_texture('assets/stamm2.png')
leaf_texture   = load_texture('assets/leaf.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1
grass = []
dirt = []
stone = []
brick = []



window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
	global block_pick, hand
	global grass, dirt, stone, brick

		
 
	
	if held_keys['1']: block_pick = 1 
	if held_keys['2']: block_pick = 2 
	if held_keys['3']: block_pick = 3 
	if held_keys['4']: block_pick = 4 
	if block_pick == 1 and len(grass) > 0: destroy(hand); hand = Hand(texture = grass_texture)
	elif block_pick == 2 and len(dirt) > 0: destroy(hand); hand = Hand(texture = dirt_texture)
	elif block_pick == 3 and len(stone) > 0: destroy(hand); hand = Hand(texture = stone_texture)
	elif block_pick == 4 and len(brick) > 0: destroy(hand); hand = Hand(texture = brick_texture)
	else: destroy(hand); hand = Hand(texture = arm_texture)

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

class Voxel(Button):
	#global grass, dirt, stone, brick
	def __init__(self, position = (0,0,0), texture = grass_texture ): #grass_texture
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block', 
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if  key == 'left mouse down':
				punch_sound.play()
				if block_pick == 1 and len(grass) > 0: grass.pop(0); voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2 and len(dirt) > 0: dirt.pop(0); voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 3 and len(stone) > 0: stone.pop(0); voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 4 and len(brick) > 0: brick.pop(0); voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				#if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = stamm_texture)
				#if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = leaf_texture)
				#voxel = Voxel(position = self.position + mouse.normal)

			if key == 'right mouse down' and not self.texture == bedrock_texture:
				if self.texture == grass_texture:
					grass.append('1')
				elif self.texture == dirt_texture:
					dirt.append('1')
				elif self.texture == stone_texture:
					stone.append('1')
				elif self.texture == stamm_texture:
					brick.append('1')
					brick.append('1')
					brick.append('1')
					brick.append('1')
				elif self.texture == brick_texture:
					brick.append('1')
				
				punch_sound.play()  
				destroy(self)

			


class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)


class Hand(Entity):
	def __init__(self,texture=arm_texture):
		super().__init__(
			parent = camera.ui,
			model = 'assets/block',
			texture = texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

def baum(pos = (1,2,1)):
	for i in range(5):
		voxel = Voxel(position=pos,texture=stamm_texture)
		pos = (pos[0],pos[1]+1,pos[2])
	voxel = Voxel(position=pos,texture=leaf_texture)
	
	for i in range(2):
		voxel = Voxel(position=(pos[0]+1,pos[1]-1-i,pos[2]),texture=leaf_texture)
		voxel = Voxel(position=(pos[0]-1,pos[1]-1-i,pos[2]),texture=leaf_texture)
		voxel = Voxel(position=(pos[0],pos[1]-1-i,pos[2]+1),texture=leaf_texture)
		voxel = Voxel(position=(pos[0],pos[1]-1-i,pos[2]-1),texture=leaf_texture)

	voxel = Voxel(position=(pos[0]+1,pos[1]-2,pos[2]+1),texture=leaf_texture)
	voxel = Voxel(position=(pos[0]+1,pos[1]-2,pos[2]-1),texture=leaf_texture)
	voxel = Voxel(position=(pos[0]-1,pos[1]-2,pos[2]+1),texture=leaf_texture)
	voxel = Voxel(position=(pos[0]-1,pos[1]-2,pos[2]-1),texture=leaf_texture)
		
	
	


for z in range(20):
	for x in range(20):
		hohe = 1 #randint(2,2)
		voxel = Voxel(position = (x-10,hohe,z-10))
		voxel = Voxel(position = (x-10,hohe-1,z-10), texture=dirt_texture)
		for q in range(hohe):
			voxel = Voxel(position = (x-10,hohe-2-q,z-10), texture=stone_texture)
			voxel =	Voxel(position = (x-10,-2 ,z-10), texture=bedrock_texture)
		if randint(1,50) == 1:
			baum(pos = (x-10,hohe+1,z-10))

"""baum(pos = (3,2,3))
baum(pos = (3,2,-3))
baum(pos = (-3,2,3))
baum(pos = (-3,2,-3))"""

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()