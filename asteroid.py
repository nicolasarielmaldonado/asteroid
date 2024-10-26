import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
        
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)
	
	def update(self, dt):
		self.position.x += self.velocity.x * dt
		self.position.y += self.velocity.y * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		ran_angle = random.uniform(20, 50)

		self.__create_children_asteroid(ran_angle)
		self.__create_children_asteroid(ran_angle * -1)

	
	def __create_children_asteroid(self, ang):
		new_vector = self.velocity.copy()
		new_vector = new_vector.rotate(ang)
		new_vector *= 1.2
		
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid.velocity = new_vector
