import random
from tkinter import *

UNITE = 10
WIDTH = 50 * UNITE
HEIGHT = 50 * UNITE
WIDTH_VOIE = 10 * UNITE
SPACE_SIZE = 20

VT = 5
VG = VT*150

colors = ['cyan', 'red',
              '#ffd700',
              'magenta',
              'violet']
list_car = []

dic_car = {0: [], 1: [], 2: [], 3: []}

dic_cpe = {0: [], 1: [], 2: [], 3: []}

dic_cpr = {0: [], 1: [], 2: [], 3: []}
dic_prio = {0: 1, 1: 2, 2: 3, 3: 0}
list_cpe = []
list_cpa = set()
list_cpr = []
list_stats= [True, True, True, True]
state = False
mode = True


class Voie:
  def __init__(self, orientation):
    self.orientation = orientation
    if orientation == "w":

      self.voie = canvas.create_rectangle(0, (HEIGHT + WIDTH_VOIE) / 2, WIDTH + 4, (HEIGHT - WIDTH_VOIE) / 2,
                                          fill="black")


      self.vf1 = canvas.create_rectangle(0, (HEIGHT + WIDTH_VOIE ) / 2,
                                        8, HEIGHT/2, fill="black", outline="black")
      self.vf2 = canvas.create_rectangle(WIDTH, (HEIGHT - WIDTH_VOIE) / 2,
                                         WIDTH-8, HEIGHT / 2, fill="black", outline="black")

      entree1 = 0, (HEIGHT + WIDTH_VOIE / 2) / 2
      sortie1 = WIDTH, (HEIGHT + WIDTH_VOIE / 2) / 2

      self.pe1 = WIDTH / 2 - WIDTH_VOIE, (HEIGHT + WIDTH_VOIE / 2) / 2
      self.pa1 = WIDTH / 2 - WIDTH_VOIE / 2, (HEIGHT + WIDTH_VOIE / 2) / 2
      self.vp1 = canvas.create_rectangle((WIDTH - WIDTH_VOIE) / 2 - 15, (HEIGHT + WIDTH_VOIE ) / 2,
                                        (WIDTH - WIDTH_VOIE) / 2, (HEIGHT + WIDTH_VOIE ) / 2 + 8, fill="black",
                                         outline="red")
      self.ps1 = WIDTH / 2 + WIDTH_VOIE / 2, (HEIGHT + WIDTH_VOIE / 2) / 2

      entree2 = WIDTH, (HEIGHT - WIDTH_VOIE / 2) / 2


      sortie2 = 0, (HEIGHT - WIDTH_VOIE / 2) / 2

      self.pe2 = WIDTH / 2 + WIDTH_VOIE, (HEIGHT - WIDTH_VOIE / 2) / 2
      self.pa2 = WIDTH / 2 + WIDTH_VOIE / 2, (HEIGHT - WIDTH_VOIE / 2) / 2
      self.vp2 = canvas.create_rectangle((WIDTH + WIDTH_VOIE) / 2 + 15, (HEIGHT - WIDTH_VOIE) / 2,
                                         (WIDTH + WIDTH_VOIE) / 2, (HEIGHT - WIDTH_VOIE) / 2 - 8, fill="black",
                                         outline="red")
      self.ps2 = WIDTH / 2 - WIDTH_VOIE / 2, (HEIGHT - WIDTH_VOIE / 2) / 2

      self.entree = (entree1, entree2)
      self.sortie = (sortie1, sortie2)

    else:
      self.voie = canvas.create_rectangle((WIDTH - WIDTH_VOIE) / 2, 0, (WIDTH + WIDTH_VOIE) / 2, HEIGHT + 4,
                                          fill="black")

      self.vf1 = canvas.create_rectangle((WIDTH + WIDTH_VOIE) / 2,HEIGHT,
                                         WIDTH / 2, HEIGHT-8, fill="black", outline="black")
      self.vf2 = canvas.create_rectangle((WIDTH - WIDTH_VOIE) / 2, 0,
                                         WIDTH / 2, 8, fill="black", outline="black")

      entree1 = (WIDTH + WIDTH_VOIE / 2) / 2, HEIGHT
      sortie1 = (WIDTH + WIDTH_VOIE / 2) / 2, 0

      self.pe1 = (WIDTH + WIDTH_VOIE / 2) / 2, HEIGHT / 2 + WIDTH_VOIE
      self.pa1 = (WIDTH + WIDTH_VOIE / 2) / 2, HEIGHT / 2 + WIDTH_VOIE / 2
      self.vp1 = canvas.create_rectangle((WIDTH + WIDTH_VOIE) / 2 + 8, (HEIGHT + WIDTH_VOIE) / 2+1,
                                         (WIDTH + WIDTH_VOIE) / 2 , (HEIGHT + WIDTH_VOIE) / 2 + 16, fill="black",
                                         outline="red")
      self.ps1 = (WIDTH + WIDTH_VOIE / 2) / 2, HEIGHT / 2 - WIDTH_VOIE / 2

      entree2 = (WIDTH - WIDTH_VOIE / 2) / 2, 0
      sortie2 = (WIDTH - WIDTH_VOIE / 2) / 2, HEIGHT



      self.pe2 = (WIDTH - WIDTH_VOIE / 2) / 2, HEIGHT / 2 - WIDTH_VOIE
      self.pa2 = (WIDTH - WIDTH_VOIE / 2) / 2, HEIGHT / 2 - WIDTH_VOIE / 2
      self.vp2 = canvas.create_rectangle((HEIGHT - WIDTH_VOIE) / 2 - 8, (WIDTH - WIDTH_VOIE) / 2 -1,
                                         (HEIGHT - WIDTH_VOIE) / 2, (WIDTH - WIDTH_VOIE) / 2 - 16, fill="black",
                                         outline="red")
      self.ps2 = (WIDTH - WIDTH_VOIE / 2) / 2, HEIGHT / 2 + WIDTH_VOIE / 2

      self.entree = (entree1, entree2)
      self.sortie = (sortie1, sortie2)

class Tiret:
  def __init__(self, orientation):
    self.orientation = orientation
    tiret = UNITE // 5
    w = WIDTH_VOIE // 12
    if orientation == "w":
      for i in range(0, 6):
        canvas.create_rectangle(WIDTH / 2 - WIDTH_VOIE / 1.5, (HEIGHT + WIDTH_VOIE + 4) / 2 - w * (1 + 2 * i),
                                WIDTH / 2 - WIDTH_VOIE, (HEIGHT + WIDTH_VOIE + 4) / 2 - w * (2 + 2 * i),
                                fill="#707070")
      for i in range(0, 52):
        canvas.create_rectangle((i - 1) * UNITE, (HEIGHT + tiret) / 2, i * UNITE, (HEIGHT - tiret) / 2,
                                fill="white")
      for i in range(0, 6):
        canvas.create_rectangle(WIDTH / 2 + WIDTH_VOIE / 1.5, (HEIGHT + WIDTH_VOIE + 4) / 2 - w * (1 + 2 * i),
                                WIDTH / 2 + WIDTH_VOIE, (HEIGHT + WIDTH_VOIE + 4) / 2 - w * (2 + 2 * i),
                                fill="#707070")
    else:
      for i in range(0, 6):
        canvas.create_rectangle((WIDTH + WIDTH_VOIE + 4) / 2 - w * (1 + 2 * i), HEIGHT / 2 - WIDTH_VOIE / 1.5,
                                (WIDTH + WIDTH_VOIE + 4) / 2 - w * (2 + 2 * i), HEIGHT / 2 - WIDTH_VOIE,
                                fill="#707070")
      for i in range(0, 52):
        self.vt = canvas.create_rectangle((WIDTH + tiret) / 2, (i - 1) * UNITE, (WIDTH - tiret) / 2, i * UNITE,
                                          fill="white")
      for i in range(0, 6):
        canvas.create_rectangle((WIDTH + WIDTH_VOIE + 4) / 2 - w * (1 + 2 * i), HEIGHT / 2 + WIDTH_VOIE / 1.5,
                                (WIDTH + WIDTH_VOIE + 4) / 2 - w * (2 + 2 * i), HEIGHT / 2 + WIDTH_VOIE,
                                fill="#707070")

class Car:
  def __init__(self, ne, ns, color="red"):
    self.color = color
    self.xn, self.yn = 20000, 20000
    self.ne = ne
    self.ns = ns
    self.ve = list_entree[ne]
    self.vs = list_sortie[ns]
    self.x = self.ve[0]
    self.y = self.ve[1]
    self.v = canvas.create_oval(self.x - 7, self.y - 7,
                                self.x + 7, self.y + 7, fill=color)
    self.xx = self.ve[0] - self.vs[0]
    self.yy = self.ve[1] - self.vs[1]
    self.pe = self.pa = self.ps = False

    # self.drive()

  # for x,y in zip(range(0, 50),range(0, 50)):
  # 	self.x = x
  # 	self.y = y
  # 	window.after(200 , self.v)
  def drive(self):
    canvas.delete(self.v)
    arrive = False
    self.xn, self.yn = 20000, 20000
    if (self.ve[0] % WIDTH == 0):
      if (self.x != self.vs[0]):
        self.x -= self.xx // abs(self.xx)
        self.xn, self.yn = self.x - 18 * (self.xx // abs(self.xx)), self.y
      elif (self.y != self.vs[1]):
        self.y -= self.yy // abs(self.yy)
    else:
      if (self.y != self.vs[1]):
        self.y -= self.yy // abs(self.yy)
        self.xn, self.yn = self.x, self.y - 18 * (self.yy // abs(self.yy))
      elif (self.x != self.vs[0]):
        self.x -= self.xx // abs(self.xx)

    # self.xn, self.yn = self.x - 18 * (self.xx // abs(self.xx)), self.y - 18 * (self.xx // abs(self.xx))

    self.pe = self.x == list_pe[self.ne][0] and self.y == list_pe[self.ne][1]
    self.pa = self.x == list_pa[self.ne][0] and self.y == list_pa[self.ne][1]
    self.ps = self.x == list_ps[self.ns][0] and self.y == list_ps[self.ns][1]
    arrive = self.x == self.vs[0] and self.y == self.vs[1]
    self.v = canvas.create_oval(self.x - 7, self.y - 7,
                                self.x + 7, self.y + 7, fill=self.color)
    if self.pe:
      list_cpe.append(self)
      dic_cpe[self.ne].append(self)
    if compareNext(self):
      list_cpa.add(self)
    if self.ps:
      list_cpe.remove(self)
      list_cpr.remove(self)
      dic_car[self.ne].remove(self)
      dic_cpe[self.ne].remove(self)
      dic_cpr[self.ne].remove(self)

    if arrive:
      canvas.delete(self.v)
    return arrive

def genereV():
  if state:
    mul= 1
    ve = [i for i in range(4) if list_stats[i]]
    if len(ve) > 0:
      if mode:
        depart = random.choice(ve)
        color = colors[depart]#random.choice(colors)

        if depart == 0:
          arrivee = random.choice([0, 1, 3])
        elif depart == 1:
          arrivee = random.choice([0, 1, 2])
        elif depart == 2:
          arrivee = random.choice([1, 2, 3])
        else:
          arrivee = random.choice([0, 2, 3])
        if len(dic_car[depart]) < 10:
          car = Car(depart, arrivee, color)
          dic_car[depart].append(car)
          list_car.append(car)
      else:
        for i in ve:
          color = colors[i]#random.choice(colors)
          depart = i
          if depart == 0:
            arrivee = random.choice([0, 1, 3])
          elif depart == 1:
            arrivee = random.choice([0, 1, 2])
          elif depart == 2:
            arrivee = random.choice([1, 2, 3])
          else:
            arrivee = random.choice([0, 2, 3])
          if len(dic_car[depart]) < 10:
            car = Car(depart, arrivee, color)
            dic_car[depart].append(car)
            list_car.append(car)
          mul=len(ve)
    window.after(VG*mul, genereV)

def compareNext(car1):
  for car2 in list_cpa:
    if car1 != car2:
      if car1.xn == car2.x and car1.yn == car2.y:
        return True
  return False

def priority(car):
  if len(list_cpr) > 0:
    if len(dic_cpr[car.ne]) > 0 and len(dic_cpe[dic_prio[car.ne]]) == 0:
      return True
    else:
      return False
  elif len(dic_cpe[dic_prio[car.ne]]) > 0:
    pp = False   # Arrivees simultanees
    if (car.ne == 0):
      for i in dic_cpe.values():
        pp = pp or len(i) == 0
      return pp != True
    return False
  return True

def traffik():
  # print(len(listCar))
  if state:
    for car in list_car:
      arrive = False
      if compareNext(car) != True:
        if car.pa:
          list_cpa.add(car)
          if priority(car):
            list_cpr.append(car)
            list_cpa.remove(car)
            dic_cpr[car.ne].append(car)
            canvas.itemconfig(list_vp[car.ne], fill="#50ff20")
            arrive = car.drive()
          else:
            canvas.itemconfig(list_vp[car.ne], fill="red")
        else:
          if len(dic_cpe[car.ne]) <= 0:
              canvas.itemconfig(list_vp[car.ne], fill="orange" if list_stats[car.ne] else "black",
                                outline="black" if list_stats[car.ne] else "red")
          else:
            pass
            # canvas.itemconfig(list_vp[car.ne], fill="red")
          arrive = car.drive()
        if arrive:
          list_car.remove(car)
    window.after(VT, traffik)


if __name__ == "__main__":
  window = Tk()
  window.title("Traffic Simulation")
  window.resizable(False, False)

  canvas = Canvas(window, bg="green",
                  height=HEIGHT, width=WIDTH)
  voieh = Voie("h")
  voiew = Voie("w")
  tireth = Tiret("h")
  tiretw = Tiret("w")

  list_entree = [voiew.entree[0],
                 voieh.entree[0],
                 voiew.entree[1],
                 voieh.entree[1]]

  list_sortie = [voiew.sortie[0],
                 voieh.sortie[0],
                 voiew.sortie[1],
                 voieh.sortie[1]]

  list_pe = [voiew.pe1, voieh.pe1, voiew.pe2, voieh.pe2]
  list_pa = [voiew.pa1, voieh.pa1, voiew.pa2, voieh.pa2]
  list_ps = [voiew.ps1, voieh.ps1, voiew.ps2, voieh.ps2]

  list_vf = [voiew.vf1, voieh.vf1, voiew.vf2, voieh.vf2]
  list_vp = [voiew.vp1, voieh.vp1, voiew.vp2, voieh.vp2]

  genereV()
  traffik()

  canvas.pack()

  def changeStats(ne):
    list_stats[ne] = not list_stats[ne]
    canvas.itemconfig(list_vf[ne], fill="black" if list_stats[ne] else "red",
                      outline="black" if list_stats[ne] else "red")

  def changeStat():
    global state
    state = not state
    bStart.config(text= "Arreter" if state else "Demarrer", background="red" if state else "yellow")
    if state:
      window.after(VG, genereV)
      traffik()

  def changeMode():
    global mode
    mode = not mode
    bMode.config(text= "Tous" if mode else "Par 1")

  frame = Frame(canvas, width=150, height=100, background="green", border=0)
  bStart = Button(frame, text="Demarrer"
                  , background="yellow", border=1, width=8, command=lambda: changeStat())

  window.bind("<space>", lambda e: changeStat())
  bStart.grid(row=0, column=0, padx=10, pady=10)
  bMode = Button(frame, text="Tous", background="orange", border=1,width=8, command=lambda: changeMode())
  bMode.grid(row=0, column=1, padx=10, pady=10)
  cv1 = Checkbutton(frame, text="Voie 1", background="green", command=lambda: changeStats(0))
  cv1.select()
  cv1.grid(row=1, column=0, padx=5, pady=10)
  cv2 = Checkbutton(frame, text="Voie 2", background="green", command=lambda: changeStats(1))
  cv2.select()
  cv2.grid(row=2, column=0, padx=5, pady=10)
  cv3 = Checkbutton(frame, text="Voie 3", background="green", command=lambda: changeStats(2))
  cv3.select()
  cv3.grid(row=1, column=1, padx=5, pady=10)
  cv4 = Checkbutton(frame, text="Voie 4", background="green", command=lambda: changeStats(3))
  cv4.select()
  cv4.grid(row=2, column=1, padx=5, pady=10)

  canvas.create_window(20, 10, window=frame, anchor='nw')
  window.update()

  window_width = window.winfo_width()
  window_height = window.winfo_height()
  screen_width = window.winfo_screenwidth()
  screen_height = window.winfo_screenheight()

  x = int((screen_width / 2) - (window_width / 2))
  y = int((screen_height / 2) - (window_height / 2))

  window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  window.mainloop()
