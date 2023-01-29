from numpy import *
import random
import pixel
from PIL import Image

def check(way,test,time,time_this):#definition der check methode zum überprüfen der ausbreitung eines Kristalls
    if time%time_this == 0:#timer durch ausbreitungsgeschwindigkeit ohne Rest heißt ausbreitung
        if way.get_color() == None: # nur ausbreitung zu einem freien Pixel
            way.set_all(test.get_pos_x(),test.get_pos_y(),test.get_neg_x(),test.get_neg_y(),test.get_color())#ausbreitung
            return True
        else:
            return False
    else:
        return False

status = "definiton"#definition einer Matrix in der Größe des Bilds und anzahl der Kristallkerne 
start_pixel_number = 300
random_start_pixel = 700
max_tempo = 30
new_pixel_prozent = 1000000
#höhe und breite des Bildes
num_rows = 1920
num_cols = 1080

matrix_pixel = [[pixel.Pixel() for i in range(num_cols)]]
matrix_pixel = reshape(matrix_pixel,(1,num_cols))
for i in range((num_rows)-1):
    row = [pixel.Pixel() for i in range(num_cols)]
    matrix_pixel = append(matrix_pixel,[row],0)

status = "start"

while start_pixel_number > 0:#werte zuweisen für jeden startpixel
    x = random.randint(0,num_cols)
    y = random.randint(0,num_rows)
    if matrix_pixel[y-1][x-1].get_active() != True:
        matrix_pixel[y-1][x-1].set_color(random.randint(10,255))
        matrix_pixel[y-1][x-1].set_active_true()
        matrix_pixel[y-1][x-1].set_pos_x(random.randint(1,max_tempo))
        matrix_pixel[y-1][x-1].set_pos_y(random.randint(1,max_tempo))
        matrix_pixel[y-1][x-1].set_neg_x(random.randint(1,max_tempo))
        matrix_pixel[y-1][x-1].set_neg_y(random.randint(1,max_tempo))

        start_pixel_number = start_pixel_number-1

status = "simmulieren"#starten der Simmulation
time = 0
while status == "simmulieren":
    time = time +1
    y = -1
    used_pixel = 0
    liste_forced = []
    for line in matrix_pixel:
        x = -1
        y= y + 1
        for new_pixel in line:#durchlaufen jedes Pixels für jedee Zeit
            x= x + 1
            if new_pixel.get_color() == None and random_start_pixel > 0:# Möglichkeit zum einfügen späterer Pixel  mit einer zufälligen Zeit
                if random.randint(1,new_pixel_prozent) == 1:
                    matrix_pixel[y][x].set_color(random.randint(0,255))
                    matrix_pixel[y][x].set_active_true()
                    matrix_pixel[y][x].set_pos_x(random.randint(1,max_tempo))
                    matrix_pixel[y][x].set_pos_y(random.randint(1,max_tempo))
                    matrix_pixel[y][x].set_neg_x(random.randint(1,max_tempo))
                    matrix_pixel[y][x].set_neg_y(random.randint(1,max_tempo))
                    random_start_pixel = random_start_pixel-1

            if new_pixel.get_active():#für jeden aktiven Pixel
                if y-1 > -1 :# Überprüfung des Randes des Bild
                    top = matrix_pixel[y-1][x]
                    if check(top,new_pixel,time,new_pixel.get_neg_y()):#nutzen der Checkmethode für den Pixel über dem ausgewählten Pixel
                        liste_forced = liste_forced +[(y-1,x)]#speichern des neuen Pixels

                if y+1 <= num_rows-1:#Wiederholung für dem Pixel darunter
                    bottom = matrix_pixel[y+1][x]
                    if check(bottom,new_pixel,time,new_pixel.get_pos_y()):
                        liste_forced = liste_forced +[(y+1,x)]

                if x-1 > -1:#Wiederholung für den Pixel links
                    left = matrix_pixel[y][x-1]
                    if check(left,new_pixel,time,new_pixel.get_neg_x()):
                        liste_forced = liste_forced +[(y,x-1)]

                if x+1 <= num_cols-1:#Wiederholung für den pixel rechts 
                    right = matrix_pixel[y][x+1]
                    if check(right,new_pixel,time,new_pixel.get_pos_x()):
                        liste_forced = liste_forced + [(y,x+1)]

                        
            if new_pixel.get_color() !=None:#jeden Pixel überprüfen ob er gefärbt ist
                used_pixel = used_pixel+1

    if used_pixel == (num_cols)*(num_rows):#wenn alle gefärbt sind enden der simmulation
        status = "finish"
    for i in liste_forced:# alle neuen Pixel auf aktiv setzen
        y = i[0]
        x = i[1]
        matrix_pixel[y,x].set_active_true()
    if time == num_rows:#not stop der simmulation
        status = "stop"
    i = 0

if status == "finish":#auswertung der simmulation
    ausgabebild=Image.open("test.jpg")
    for y in range(0,num_cols):
        for x in range(0,num_rows):
            color = matrix_pixel[x,y].get_color()
            ausgabebild.putpixel((x, y), (color,color,color))#umwandeln der Matrix in eine Jpg
    name = str(random.randint(1000,9999))
    ausgabebild.save(name +".jpg")
else:
    print("simmulation wurde abgebrochen")
