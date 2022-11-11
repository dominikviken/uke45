'''
Pygame må installeres før å begynne oppgavene!!!!!!!!!!!

Last ned Praktisk_arv_subklasse og kjør koden. Du skal se et sett objekter laget av subklasser definerte 
i fila subclass_practical_exercise.py. 

'''
'''
Oppgave 1

Forklar med egne ord hva betyr begrepet "objekt" i objektorientert programmering.

'''

#Begrepet objekt i objektorientert programmering betyr at flere variabler, eller klasser er strukturert innenfor en klasse. Dette skaper da et objekt.

'''
Oppgave 2
implementer EGET program med 2 superklasser og 1 subklasse for hver superklasse.
opprett 2 objekter for hver subklasse. disse objektene skal bytte farge hvis de kolliderer med andre objekter 
'''

import pygame
import random #importerer pygame og random

screenX = 640
screenY = 360 #skjermstørrelsen
bgimg = "img/puffa.png" #bakgrunn bilde

pygame.init() #starter pygame
screen = pygame.display.set_mode((screenX, screenY), 0, 32) #setter skjermen opp med skjermstørrelsen
background = pygame.image.load(bgimg) #laster inn bakgrunnsbilde
background = background.convert() #setter bakgrunnen

class Sirklerbevege:
    def __init__(self):
        self.x = 42 #setter objektet sitt x posisjon
        self.y = 200 #setter ojektet sitt y posisjon
        self.speed = [50 + 60 * random.random(),
                      50 + 60 * random.random()] #får fart variabelen
        self.size = 30

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed #oppdaterer x og y verdiene

        if self.x < 0: #om objekten koliderer med venstre delen av skjermen..
            self.speed[0] = abs(self.speed[0]) #gjør fart int-en positiv
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #setter tilfeldig farge på figuren
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.x > screenX - self.size: #om objekten koliderer med høyre delen av skjermen..
            self.speed[0] = -abs(self.speed[0]) #gjør fart int-en negativ
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #setter tilfeldig farge på figuren
        if self.y > screenY - self.size:
            self.speed[1] = -abs(self.speed[1])
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Rektangelbevege:
    def __init__(self):
        self.x = 16
        self.y = 136
        self.speed = [80 + 90 * random.random(),
                      80 + 90 * random.random()]
        self.size = 65

    def move(self, time_passed):
        self.x += self.speed[0] * time_passed
        self.y += self.speed[1] * time_passed

        if self.x < 0:
            self.speed[0] = abs(self.speed[0])
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.y < 0:
            self.speed[1] = abs(self.speed[1])
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.x > screenX - self.size:
            self.speed[0] = -abs(self.speed[0])
            self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.y > screenY - self.size:
            self.speed[1] = -abs(self.speed[1])
            self.col = (224, random.randint(0, 255), random.randint(0, 255))

class sirkel(Sirklerbevege):
    def __init__(self):
        Sirklerbevege.__init__(self)
        self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #setter tilfeldig farge

    def draw(self):
        pygame.draw.circle(screen, self.col, (round(self.x), round(self.y)),
                           round(self.size / 2)) #tegner en sirkel på skjermen, på x og y posisjonen dens, og størelsen dens
    
class kvadrat(Rektangelbevege):
    def __init__(self):
        Rektangelbevege.__init__(self)
        self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(screen, self.col, pygame.Rect(self.x, self.y,30,30)) #tegner rektangel på skjermen, med random farge, på posisjonene til x og y

objs = [
    sirkel(),
    sirkel(),
    kvadrat(),
    kvadrat() #tegner de 4 objektene
]

clock = pygame.time.Clock() #lager variabel for pc-klokken
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    time_passed = clock.tick(30) / 1000.0 

    screen.blit(background, (0, 0))
    
    for obj in objs: #for hvert objekt i objs
        obj.move(time_passed) #kjør move funksjonen innenfor superklassen

    for obj in objs:
        obj.draw() #tegn objektet på nytt

    pygame.display.update() #oppdater skjermen