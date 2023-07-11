from tkinter import *
import random

x0 = 200
y0 = 150
x1 = 300
y1 = 300

panjang = 0
lebar = 0


class Oval:
    def __init__(self, canvas, x0, y0, x1, y1, warna):
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.warna = warna
        self.oval = canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.warna)

    def jalan(self):
        while True:
            self.angka1 = random.choice([-10, 10])
            self.angka2 = random.choice([-10, 10])
            self.x0 += self.angka1
            self.y0 += self.angka2
            self.x1 += self.angka1
            self.y1 += self.angka2

            # if self.x0 + self.angka1 <= 0:
            #     canvas.move(self.oval, 0, self.angka2 * -1)
            # elif self.y0 + self.angka2 <= 0:
            #     canvas.move(self.oval, self.angka1 * -1, 0)
            # elif self.x1 + self.angka1 >= 450:
            #     canvas.move(self.oval, self.angka1 * -1, 0)
            # elif self.y1 + self.angka2 >= 450:
            #     canvas.move(self.oval, 0, self. angka2 * -1)
            # else:
            self.canvas.move(self.oval, self.angka1, self.angka2)
            self.canvas.after(50)
            self.canvas.update()
            print(self.y1)
            print("===")

            # object 1
            if self.x0 == 100 and self.y0 >= -100 and self.y0 <= 100:
                canvas.delete(gambarKecil1)
            if self.y0 == 100 and self.x0 >= -100 and self.x0 <= 50:
                canvas.delete(gambarKecil1)
            if self.x1 == 50 and self.y1 >= -100 and self.y1 <= 100:
                canvas.delete(gambarKecil1)
            if self.y1 == 50 and self.x1 >= 100 and self.x1 <= 100:
                canvas.delete(gambarKecil1)

            # object 2
            if self.x0 == 100 and self.y0 >= 0 and self.y0 <= 200:
                canvas.delete(gambarKecil2)
            if self.y0 == 200 and self.x0 >= -50 and self.x0 <= 0:
                canvas.delete(gambarKecil2)
            if self.x1 == 50 and self.y1 >= -50 and self.y1 < -150:
                canvas.delete(gambarKecil2)
            if self.y1 == 250 and self.x1 >= 100 and self.x1 <= 200:
                canvas.delete(gambarKecil2)

            # object 3
            if self.x0 == 100 and self.y0 >= 100 and self.y0 <= 300:
                canvas.delete(gambarKecil3)
            if self.y0 == 300 and self.x0 >= 50 and self.x0 <= 0:
                canvas.delete(gambarKecil3)
            if self.x1 == 250 and self.y1 >= 50 and self.y1 <= 50:
                canvas.delete(gambarKecil3)
            if self.y1 == 50 and self.x1 >= 100 and self.x1 <= 300:
                canvas.delete(gambarKecil3)

            # object 4
            if self.x0 == 100 and self.y0 >= 200 and self.y0 <= 400:
                canvas.delete(gambarKecil4)
            if self.y0 == 400 and self.x0 >= -50 and self.x0 <= 0:
                canvas.delete(gambarKecil4)
            if self.x1 == 50 and self.y1 >= 150 and self.y1 <= 50:
                canvas.delete(gambarKecil4)
            if self.y1 == 50 and self.x1 >= 100 and self.x1 <= 400:
                canvas.delete(gambarKecil4)

            # object 5
            if self.x0 == 200 and self.y0 >= -100 and self.y0 <= 100:
                canvas.delete(gambarKecil5)
            if self.y0 == 100 and self.x0 >= 50 and self.x0 <= 200:
                canvas.delete(gambarKecil5)
            if self.x1 == 150 and self.y1 >= -150 and self.y1 <= 50:
                canvas.delete(gambarKecil5)
            if self.y1 == 50 and self.x1 >= 0 and self.x1 <= 150:
                canvas.delete(gambarKecil5)

            # # object 8
            # if self.x0 == 200 and self.y0 >= 200 and self.y0 <= 400:
            #     canvas.delete(gambarKecil8)
            # if self.y0 == 400 and self.x0 >= 50 and self.x0 <= 200:
            #     canvas.delete(gambarKecil8)
            # if self.x1 == 150 and self.y1 >= 400 and self.y1 <= 350:
            #     canvas.delete(gambarKecil8)
            # if self.y1 == 350 and self.x1 >= 200 and self.x1 <= 350:
            #     canvas.delete(gambarKecil8)

            # object 9
            if self.x0 == 300 and self.y0 >= -100 and self.y0 <= 100:
                canvas.delete(gambarKecil9)
            if self.y0 == 100 and self.x0 >= 150 and self.x0 <= 300:
                canvas.delete(gambarKecil9)
            if self.x1 == 250 and self.y1 >= -150 and self.y1 <= 50:
                canvas.delete(gambarKecil9)
            if self.y1 == 50 and self.x1 >= 100 and self.x1 <= 250:
                canvas.delete(gambarKecil9)

            # object 13
            if self.x0 == 400 and self.y0 >= -100 and self.y0 <= 100:
                canvas.delete(gambarKecil13)
            if self.y0 == 100 and self.x0 >= 250 and self.x0 <= 400:
                canvas.delete(gambarKecil13)
            if self.x1 == 350 and self.y1 >= -150 and self.y1 <= 50:
                canvas.delete(gambarKecil13)
            if self.y1 == 50 and self.x1 >= 200 and self.x1 <= 350:
                canvas.delete(gambarKecil13)

            # object baru
            if self.x0 == 200 and self.y0 >= 200 and self.y0 <= 400:
                canvas.delete(objBaru)
            if self.y0 == 400 and self.x0 >= 50 and self.x0 <= 200:
                canvas.delete(objBaru)
            if self.x1 == 150 and self.y1 >= 400 and self.y1 <= 350:
                canvas.delete(objBaru)
            if self.y1 == 350 and self.x1 >= 200 and self.x1 <= 350:
                canvas.delete(objBaru)


root = Tk()
root.title('Games Sederhana Widi')
canvas = Canvas(root, width=450, bg='yellow', height=450)
canvas.pack()

gambarKecil1 = canvas.create_oval(50, 50, 100, 100, fill="white")
gambarKecil2 = canvas.create_rectangle(50, 150, 100, 200, fill="red")
gambarKecil3 = canvas.create_rectangle(50, 250, 100, 300, fill="black")
gambarKecil4 = canvas.create_oval(50, 350, 100, 400, fill="white")
gambarKecil5 = canvas.create_rectangle(150, 50, 200, 100, fill="green")
# gambarkecil6 = canvas.create_rectangle(150, 150, 200, 200, fill="white")
# gambarKecil7 = canvas.create_rectangle(150, 250, 200, 300, fill="purple")
# gambarKecil8 = canvas.create_rectangle(150, 350, 200, 400, fill="red")
gambarKecil9 = canvas.create_rectangle(250, 50, 300, 100, fill="brown")
# gambarKecil10 = canvas.create_rectangle(250, 150, 300, 200, fill="orange")
# gambarKecil11 = canvas.create_rectangle(250, 250, 300, 300, fill="white")
# gambarKecil12 = canvas.create_rectangle(250, 350, 300, 400, fill="blue")
gambarKecil13 = canvas.create_oval(350, 50, 400, 100, fill="white")

# object baru
point = [190, 410, 200, 380, 230, 370, 200, 360, 190, 330, 180, 360, 150, 370, 180, 380]
objBaru = canvas.create_polygon(point, fill='red')

a = Oval(canvas, x0, y0, x1, y1, 'red')
a.jalan()
