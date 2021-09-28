import datetime
today = datetime.datetime.now().strftime("%d-%H-%M-%OS")
print (today)
w, h = 1500,1500
bg_r, bg_g, bg_b = 51, 61, 235
fg_r, fg_g, fg_b = 14, 251, 172
fontName="AC-Jade-Variable-VF.ttf"
x1,y1= 100,97.79
x2, y2= 1400, 160.0
for axis, data in listFontVariations().items():
    print((axis, data))
def manejador():
    stroke(fg_r/255, fg_g/255, fg_b/255)
    strokeWidth(4)
    line((x1,y1),(x2,y1))
    fill(0,0.0)
    oval(x1+(x2-x1)*delta-30,y1-30,60,60)

axis_name=list(listFontVariations(fontName).items())[1][0]
minValue_wght = listFontVariations(fontName)[axis_name]["minValue"]
maxValue_wght = listFontVariations(fontName)[axis_name]["maxValue"]
print(axis_name)
fSize=562
#Cuadros por segundo
frames= 60
fps=20
text_Content="Jade"

for frame in range(frames):
    newPage(w,h)
    frameDuration(1/fps)
    fill(bg_r/255, bg_g/255, bg_b/255)
    rect(0,0,w,h)
    fill(fg_r/255, fg_g/255, fg_b/255)
    dx = pi * frame / frames
    delta = pow(sin(dx), 3)
    #print(delta)
    axisValue = delta * (maxValue_wght - minValue_wght) + minValue_wght
    font(fontName, fSize)
    kwargs = {axis_name: axisValue}
    fontVariations(**kwargs)
    text(text_Content, (w/2, h/2-fSize/4+6), align="center")

    manejador()

#saveImage('~/Desktop/ q'+today+'.gif')