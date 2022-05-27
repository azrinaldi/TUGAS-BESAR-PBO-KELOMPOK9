import random
import pygame
import sys

# kelas point untuk koordinat pada game
class Point:
  # inisialisasi variabel koordinat x dan y
  def __init__(self, x, y):
    self.x = x
    self.y = y
  # method penjumlahan untuk menjumlahkan point koordinat (polymorphism)
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  # method equal untuk membandingkan point koordinat (polymorphism)
  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y

# kelas Square sebagai body untuk snake dan food
class Square:
  # inisialisasi variabel color (private) dan posisi
  def __init__(self, color, posisi):
    self.__color = color
    self.posisi = posisi

  # method equal untuk membandingkan posisisi (polymorphism)
  def __eq__(self, other):
    return self.__class__ == other.__class__ and self.posisi == other.posisi

  # method tampilkan untuk membuat square
  def tampilkan(self, surface):
    # menggunakan rect dari module pygame untuk memanipulasi square
    pygame.draw.rect(surface, self.__color, (
      self.posisi.x * self.keliling_square + self.lebar_square,
      self.posisi.y * self.keliling_square + self.lebar_square,
      self.panjang_square,
      self.panjang_square
    ))
  # size dari square
  lebar_square = 1
  panjang_square = 15
  keliling_square = panjang_square + lebar_square * 2

# kelas Snake sebagai objek yang digerakkan oleh player
class Snake:
  # warna dari snake
  color = '#00FF00'
  # menggunakan direction dari module pygame
  directions = {
    pygame.K_UP: {'name': 'up', 'movement': Point(0, -1), 'opposite': 'down'},
    pygame.K_RIGHT: {'name': 'right', 'movement': Point(1, 0), 'opposite': 'left'},
    pygame.K_DOWN: {'name': 'down', 'movement': Point(0, 1), 'opposite': 'up'},
    pygame.K_LEFT: {'name': 'left', 'movement': Point(-1, 0), 'opposite': 'right'}
  }

  # inisialisasi variabel posisi dan arah(arah awal ke kanan)
  def __init__(self, posisi, arah = 'right'):
    self.__squares = [Square(self.color, posisi)]
    self.__arah = self.directions[pygame.K_RIGHT]
    # atribut is_alive untuk mendeklarasikan ular hidup
    self.is_alive = True

  # method move untuk mengatur directions
  def move(self, key):
    # mengubah arah sesuai dengan key
    if (key in self.directions and self.directions[key]['name'] != self.__arah['opposite']):
      self.__arah = self.directions[key]
    # membuat new_square sesuai dengan direction menggunakan method __add___ dari point class
    new_square = Square(self.color, self.__squares[-1].posisi + self.__arah['movement'])

    # fungsi if untuk pengecekan apakah ular masih hidup atau tidak
    if (new_square in self.__squares or
    new_square.posisi.x < 0 or new_square.posisi.x >= Game_play.lebar or
    new_square.posisi.y < 0 or new_square.posisi.y >= Game_play.panjang):
      self.is_alive = False
    
    # menambahkan squares ke dalam list/ular
    self.__squares.append(new_square)

    # mengembalikan posisi terbaru ular
    return new_square.posisi

  # method shrink untuk menghilangkan ekor ular setiap bergerak
  def shrink(self):
    self.__squares.pop(0)

  # method tampilkan untuk menampilkan square atau ular
  def tampilkan(self, surface):
    for square in self.__squares:
      square.tampilkan(surface)
      
#class game berfungsi untuk mengatur game play
class Game_play:
  # warna background
  background_color = '#152238'
  # warna food
  food_color = '#ff0000'

  # size dari background untuk bermain
  panjang = 30
  lebar = 40
  panjang_screen = panjang * Square.keliling_square
  lebar_screen = lebar * Square.keliling_square

  # inisialisasi variabel dengan memanggil module pygame
  def __init__(self):
    # atribut screen
    self.__screen = pygame.display.set_mode((self.lebar_screen, self.panjang_screen))
    # menampilkan judul game
    pygame.display.set_caption("Snake")
    # backsound
    pygame.mixer.init()
    self.play_background_music()
    # atribut font
    pygame.font.init()
    self.__font = pygame.font.Font(pygame.font.get_default_font(), 30)
    # atribut clock dengan menggunakan module
    self.__clock = pygame.time.Clock()
    self.__reset()
    self.score = 0
  #method run berfungsi untuk mengatur kecepatan 
  def run(self):   
    while True:
      pygame.time.delay(90)
      self.__clock.tick(90)
	# memanggil beberapa method untuk running game
      self.__cek_events()
      self.__cek_eat()
      self.__tampilkan()
  
  # method reset untuk me-reset game
  def __reset(self):
    self.__arah_key = None
    self.__snake = Snake(Point(self.lebar / 2, self.panjang / 2))
    self.__generate_food()
    # fungsi memulai ulang music
    pygame.mixer.music.unpause()
    pygame.mixer.music.rewind()
  # method generate_food berfungsi untuk memunculkan makanan secara random/acak
  def __generate_food(self):
    self.__food = Square(self.food_color, Point(random.randrange(0, self.lebar), random.randrange(0, self.panjang)))
  #-------------------------------------------------------------------------------------------------------------------------------  
  # method __cek_events menggunakan pygame.event.get untuk mendeteksi kejadian dalam game
  def __cek_events(self):
    for event in pygame.event.get():
      # jika quit dari game
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      # jika menekan tombol maka akan mendeteksi apakah itu key yang benar  
      elif event.type == pygame.KEYDOWN:  
        # berfungsi agar pemain bisa keluar dari game dengan menekan tombol esc  
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          quit()
        # jika ular masih hidup maka akan memasukkan event.key ke direction_key
        elif self.__snake.is_alive and event.key in Snake.directions:
          self.__arah_key = event.key
        # reset game ketika ular mati dan player menekan "SPACE"
        elif not self.__snake.is_alive and event.key == pygame.K_SPACE:
          self.__reset()
  # method cek untuk memanggil generate_food atau shrink
  def __cek_eat(self):
    if self.__snake.is_alive:
      # jika direction key sama dengan posisi food maka akan memanggil generate_food  
      if self.__snake.move(self.__arah_key) == self.__food.posisi:
        self.__generate_food()
        # menghitung score
        self.score+=1
        # backsound eat food
        eating_sound = pygame.mixer.Sound("Resources/Eating.wav")
        pygame.mixer.Sound.play(eating_sound)
      # memanggil shrink untuk menyusutkan ekor ular  
      else:
        self.__snake.shrink()
  def play_background_music(self):
    pygame.mixer.music.load("Resources/BakgroundMusic.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
  # method tampilkan untuk menampilkan screen dan semua method tampilkan
  def __tampilkan(self):
    self.__screen.fill(self.background_color)
	# jika ular masih hidup akan menampilkan ular dan food
    if self.__snake.is_alive:
      self.__snake.tampilkan(self.__screen)
      self.__food.tampilkan(self.__screen)
    else:
      # menghentikan music    
      pygame.mixer.music.pause()    
      # menampilkan perintah "Press Space to restart" untuk reset game 
      text_label = pygame.font.SysFont('Courier New',30).render("YOUR SCORE",True,'#ffffff')
      self.__screen.blit(text_label, (self.lebar_screen / 2 - text_label.get_width() / 2, 200))
      text_score = pygame.font.SysFont('Courier New',30).render(str(self.score),True,'#ffffff')
      self.__screen.blit(text_score, (self.lebar_screen / 2 - text_score.get_width() / 2, 230))
      text_space = pygame.font.SysFont('Courier New',20).render("Press 'SPACE' for restart",True,'#ffffff')
      self.__screen.blit(text_space, (self.lebar_screen / 2 - text_space.get_width() / 2, 450))

    pygame.display.update()
    
  
# method run untuk memainkan game
Game_play().run()
