from tkinter import *
import random

UNITE = 10
WIDTH = 80 * UNITE
HEIGHT = 50 * UNITE
WIDTH_VOIE = 10 * UNITE
SPACE_SIZE = 20

VT = 5

list_train = []
list_pass = []
dict_train = {0:[],1:[]}
dict_pass = {0:[],1:[]}
dict_entree = {0:[],1:[]}


class Train:
  def __init__(self, nv, taille):
    self.taille = taille
    self.nv = nv
    self.voie = list_voie[nv]
    self.pe, self.is_pe = list_pe[nv], False
    self.ps, self.is_ps = list_ps[nv], False
    self.wagons = []
    self.coord = []
    self.position = 0
    self.drive()

  def drive(self):
    arrive = False
    if len(self.wagons) > 0 :
      for i in self.wagons:
        # print(i)
        canvas.delete(i)
      self.wagons = []
    if  self.position < len(self.voie)-1:
        self.coord = [self.voie[self.position]] + self.coord
        self.is_pe = int(self.voie[self.position][0]) == int(self.pe[0]) and int(self.voie[self.position][1]) == int(self.pe[1])

        self.is_ps = int(self.voie[self.position][0]) == int(self.ps[0]) and int(self.voie[self.position][1]) == int(self.ps[1])
        if self.position >= self.taille*12:
          self.coord.remove(self.coord[-1])
        for i in range(0,len(self.coord), 1): #self.voie[self.position - taille: self.position]:
          if i%12 ==0 :
            w = canvas.create_oval(self.coord[i][0]-7, self.coord[i][1]-7,
                                   self.coord[i][0] + 7, self.coord[i][1] + 7, fill='yellow')
            self.wagons.append(w)

        self.position += 1
    else:
      arrive = True
    return arrive

def genTrain():
  nv = random.randint(0,1)
  if len(dict_entree[nv]) <= 0:
    train = Train(nv, 5)
    list_train.append(train)
    dict_train[nv].append(train)
    dict_entree[nv].append(train)
  window.after(2000, genTrain)

def traffik():
  arrive = False
  for i in list_train:
    if i.is_pe:
      if len(list_pass)> 0 and len(dict_pass[i.nv]) > 0 or len(list_pass)== 0:
        arrive = i.drive()
        list_pass.append(i)
        dict_pass[i.nv].append(i)
        dict_entree[i.nv].remove(i)

    else:
      arrive = i.drive()
      if i.is_ps:
        list_pass.remove(i)
        dict_pass[i.nv].remove(i)
    if arrive:
      list_train.remove(i)
      dict_train[i.nv].remove(i)

  window.after(10, traffik)
class Voie:
  def __init__(self):

    self.route = canvas.create_rectangle(0, (HEIGHT + WIDTH_VOIE) / 2, WIDTH + 4, (HEIGHT - WIDTH_VOIE) / 2,
                                         fill="#5f5f7f")

    self.entree1 = 0, (HEIGHT + WIDTH_VOIE / 2) / 2
    self.sortie1 = WIDTH, (HEIGHT + WIDTH_VOIE / 2) / 2

    self.long_tunnel = WIDTH / 3
    self.long_inter = self.long_tunnel / 4
    self.long_entree = (WIDTH - self.long_tunnel) / 2 - self.long_inter

    self.entree2 = WIDTH, (HEIGHT - WIDTH_VOIE / 2) / 2
    self.sortie2 = 0, (HEIGHT - WIDTH_VOIE / 2) / 2

    self.voie1 = []
    self.e1 = self.s1 = 0,0
    self.voie2 = []
    self.e2 = self.s2 = 0, 0
    self.genV()
  def support(self, x, y, l=12, color="#fcfcfc"):
    if x % 4 ==0:
      canvas.create_line(x, y-l/2,x, y+l/2, width=0.4,fill=color)
  def fer(self, x1,y1,x2,y2, w=5, color="black"):
    canvas.create_line(x1, y1-w/2, x2, y2-w/2, width=2, fill=color)
    canvas.create_line(x1, y1+w/2, x2, y2+w/2, width=2, fill=color)
  def genV(self):

    long_tunnel = self.long_tunnel
    long_inter = self.long_inter
    long_entree = self.long_entree
    long_voie = 7
    entree1, entree2 = self.entree1, self.entree2


    for i in range(0, int(long_entree), 1):
      self.voie1.append([i, entree1[1]])
      self.support(i, entree1[1])
    self.fer(0,entree1[1],long_entree,entree1[1])
    self.e1 = int(long_entree),entree1[1]

    y = (HEIGHT / 2 - entree1[1]) / long_inter
    for i, o in zip(range(int(long_entree), int(long_entree + long_inter), 1), range(0, int(long_inter), 1)):
      self.voie1.append([i, entree1[1] + y * o])
      self.support(i, entree1[1] + y * o)
    self.fer(long_entree, entree1[1], long_entree + long_inter, HEIGHT/2)


    y = (HEIGHT / 2)
    for i in range(int(long_entree + long_inter), int(long_entree + long_inter + long_tunnel), 1):
      self.voie1.append([i, y])
      self.support(i, y)
    self.fer(long_entree + long_inter, HEIGHT/2, long_entree + long_inter + long_tunnel, HEIGHT/2)

    y = -(HEIGHT / 2 - entree1[1]) / long_inter
    for i, o in zip(
        range(int(long_entree + long_inter + long_tunnel), int(long_entree + long_tunnel + 2 * long_inter), 1),
        range(0, int(long_inter), 1)):
      self.voie1.append([i, HEIGHT / 2 + y * o])
      self.support(i, HEIGHT / 2 + y * o)
    self.fer(long_entree + long_inter + long_tunnel, HEIGHT/2, long_entree + 2*long_inter + long_tunnel, entree1[1])
    self.s1 = long_entree + 2*long_inter + long_tunnel, entree1[1]

    for i in range(int(long_entree + long_tunnel + 2 * long_inter), int(WIDTH+50), 1):
      self.voie1.append([i, entree1[1]])
      self.support(i, entree1[1])
    self.fer(long_entree + 2*long_inter + long_tunnel, entree1[1], WIDTH, entree1[1])


    # ########################################################################################


    for i in range(int(WIDTH), int(long_entree + long_tunnel + 2 * long_inter), -1):
      self.voie2.append([i, entree2[1]])
      self.support(i, entree2[1])
    self.fer(long_entree + 2*long_inter + long_tunnel, entree2[1], WIDTH, entree2[1])
    self.e2 = long_entree + 2 * long_inter + long_tunnel, entree2[1]

    y = (HEIGHT / 2 - entree2[1]) / long_inter
    for i, o in zip(
        range(int(long_entree + long_tunnel + 2 * long_inter), int(long_entree + long_inter + long_tunnel), -1),
        range(0, int(long_inter), 1)):
      self.voie2.append([i, entree2[1] + y * o])
      self.support(i, entree2[1] + y * o)
    self.fer(long_entree + long_inter + long_tunnel, HEIGHT/2, long_entree + 2*long_inter + long_tunnel, entree2[1])

    y = (HEIGHT / 2)
    for i in range(int(long_entree + long_inter + long_tunnel), int(long_entree + long_inter), -1):
      self.voie2.append([i, y])

    y = -(HEIGHT / 2 - entree2[1]) / long_inter
    for i, o in zip(range(int(long_entree + long_inter), int(long_entree-1), -1), range(0, int(long_inter+1), 1)):
      self.voie2.append([i, HEIGHT / 2 + y * o])
      self.support(i, HEIGHT / 2 + y * o)
    self.fer(long_entree, entree2[1], long_entree + long_inter, HEIGHT/2)
    self.s2 = long_entree, entree2[1]

    for i in range(int(long_entree), -50, -1):
      self.voie2.append([i, entree2[1]])
      self.support(i, entree2[1])
    self.fer(0,entree2[1],long_entree,entree2[1])


if __name__ == "__main__":
  window = Tk()
  window.title("Traffic Simulation")
  window.resizable(False, False)
  x = int((WIDTH / 2) - (WIDTH / 2))
  y = int((HEIGHT / 2) - (HEIGHT / 2))

  window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

  canvas = Canvas(window, bg="green",
                  height=HEIGHT, width=WIDTH)

  canvas.pack()

  voie = Voie()
  list_voie = [voie.voie1, voie.voie2]
  list_pe = [voie.e1, voie.e2]
  list_ps = [voie.s1, voie.s2]

  genTrain()
  traffik()
  # train = Train(1, 5)
  # train = Train(voie.voie1, 3)



  frame = Frame(canvas, width=150, height=100, background="green", border=0)
  bStart = Button(frame, text="Demarrer"
                  , background="yellow", border=1, width=8)
  bStart.grid(row=0, column=0, padx=10, pady=10)

  canvas.create_window(20, 10, window=frame, anchor='nw')
  window.update()

  # window_width = window.winfo_width()
  # window_height = window.winfo_height()
  # screen_width = window.winfo_screenwidth()
  # screen_height = window.winfo_screenheight()



  window.mainloop()
