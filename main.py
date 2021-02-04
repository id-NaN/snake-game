import pygame
import random




class SnakeGame:
	def __init__(self, speed = 10, tail = 3, speed_multiplier = 1.001,
				size = (51, 31)):
		pygame.init()
		pygame.font.init()
		self.size = size
		self.tile_size = (20)
		self.display_size = (size[0] * self.tile_size, size[1] * self.tile_size + 50)
		self.clock = pygame.time.Clock()


		self.snake_position = [int(x / 2) for x in self.size]
		self.snake_direction = (0, 1)
		self.snake_segments = []
		self.speed_multiplier = speed_multiplier
		self.screen = pygame.display.set_mode(self.display_size)
		self.snake_tail_size = tail
		self.snake_speed = speed
		self.font = pygame.font.SysFont('Comic Sans MS', 30)
		pygame.display.set_caption("snake")
		self.new_apple()


		self.game_loop()




	class NewSnakeSegment:
		def __init__(self, position):
			self.position = position
			self.age = 0



		def update(self):
			self.age += 1



		def calc_position(self, tile_size, index):
			return self.position[index] * tile_size



	def game_loop(self):
		self.running = True
		while self.running:
			self.clock.tick(self.snake_speed)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False


				elif event.type == pygame.KEYDOWN:
					if event.key == 119:
						self.snake_direction = ( 0, -1)
					elif  event.key == 97:
						self.snake_direction = (-1,  0)
					elif  event.key == 115:
						self.snake_direction = ( 0,  1)
					elif  event.key == 100:
						self.snake_direction = ( 1,  0)


			self.snake_position = [self.snake_position[0] + self.snake_direction[0],
					self.snake_position[1] + self.snake_direction[1]]


			for snake_segment in self.snake_segments:
				snake_segment.update()
				if snake_segment.age > self.snake_tail_size:
					self.snake_segments.remove(snake_segment)
				if self.snake_position == snake_segment.position:
					self.running = False


			if self.snake_position[0] < 0:
				self.snake_position[0] = self.size[0] - 1
			if self.snake_position[1] < 0:
				self.snake_position[1] = self.size[1] - 1

			if self.snake_position[0] >= self.size[0]:
				self.snake_position[0] = 0
			if self.snake_position[1] >= self.size[1]:
				self.snake_position[1] = 0


			if self.snake_position == self.apple_position:
				self.snake_tail_size += 1
				self.snake_speed *= self.speed_multiplier
				self.new_apple()


			self.snake_segments.append(self.NewSnakeSegment(self.snake_position))
			self.draw()
		pygame.quit()



	def draw(self):
		self.screen.fill((20, 50, 20))
		for segment in self.snake_segments:
			pygame.draw.rect(self.screen, (0, 0, 0),
					(segment.calc_position(self.tile_size, 0), segment.calc_position(self.tile_size, 1),
					self.tile_size, self.tile_size))
		pygame.draw.circle(self.screen, (150, 0, 0), (int(self.apple_position[0] * self.tile_size + self.tile_size / 2),
				int(self.apple_position[1] * self.tile_size + self.tile_size / 2)), int(self.tile_size / 3))
		pygame.draw.rect(self.screen, (0, 0, 0),
				((0, self.size[1] * self.tile_size), (self.size[0] * self.tile_size, 50))
			)
		textsurface = self.font.render("length: " + str(self.snake_tail_size), False, (255, 255, 255))
		self.screen.blit(textsurface, (20, self.size[1] * self.tile_size))
		textsurface = self.font.render("speed: " + str(round(self.snake_speed, 2)), False, (255, 255, 255))
		self.screen.blit(textsurface, (self.size[0] * self.tile_size / 2, self.size[1] * self.tile_size))
		pygame.display.flip()



	def new_apple(self):
		apple_valid = False
		while not apple_valid:
			self.apple_position = [random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)]
			apple_valid = True
			for segment in self.snake_segments:
				if segment.position == self.apple_position:
					apple_valid = False
			if self.snake_position == self.apple_position:
				apple_valid = False



SnakeGame()