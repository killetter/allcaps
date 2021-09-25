path = '../fonts/AC-Jade-Regular.otf'
nombre = 'verde'
margen_x= 39.99
margen_y = 30
tamanoFuente = 901
radio = 5
colorNodos = 0.8117647058823529, 0.027450980392156862, 0.1843137254901961
colorPunto = 0.8117647058823529, 0.027450980392156862, 0.1843137254901961
anchoLinea = 2   
fuenteSize = 1200 
#print(x)
font(path)
#glifos=listFontGlyphNames()
#print(listFontGlyphNames())
glifos = ["A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
]
listaNo= ["space","C.001", "M.001", "R.001", "a.001","c.001","d.001","g.001","g.002","h.001","l.001","m.001","n.001","u.001","y.001","grave","acute","tilde","Barra_mayus","asterisco","cerosup","mayus_serif",]
#print(len(glifos))
for x, glifo in enumerate(glifos):
    if glifo in listaNo :
        continue
    #newPage('Letter')
    newPage(1200,1200)
    frameDuration(1/3)
    tx = BezierPath()
    fs = FormattedString()
    fs.font(path)
    fs.fontSize(tamanoFuente)
    fs.appendGlyph(glifo)
    #with savedState():
    fill(0.98,0.14,0.36,0)
    rect(0,0,width(),height())
    strokeWidth(anchoLinea)
    stroke(0.9, 0.5, 0.5)
    tx.text(fs, font = path, fontSize=fuenteSize,)
    letter_width = tx.bounds()[-2] - tx.bounds()[0]
    x_offset = (width() - letter_width) /2
    translate(x_offset+115, 416)
    drawPath(tx)
    previous_oncurve = None
    for contour in tx:
        for segment in contour:
            if len(segment) == 3:
                offcurve_1, offcurve_2, oncurve = segment
            ####Manejador 1 
                with savedState():
                    fill(*colorNodos,)
                    strokeWidth(anchoLinea)
                    stroke(*colorPunto)
                    rotate(45,(offcurve_1))
                    rect(offcurve_1[0]-radio,offcurve_1[1]-radio, radio*2,radio*2)
            ####Manejador 2
                with savedState():
                    fill(*colorNodos,)
                    stroke(*colorPunto)
                    strokeWidth(anchoLinea)
                    rotate(45,(offcurve_2))
                    rect(offcurve_2[0]-radio,offcurve_2[1]-radio, radio*2,radio*2)
            #######Nodo
                stroke(*colorPunto,1)
                strokeWidth(anchoLinea)
                line(previous_oncurve, offcurve_1)
                line(offcurve_2, oncurve)   
                oval( oncurve[0]-(radio*(factor/2)),oncurve[1]-(radio*(factor/2)),radio*factor,radio*factor)
            else:
                oncurve = segment[-1]
                fill(*colorPunto,1)
                stroke(*colorPunto,1)
                strokeWidth(anchoLinea)
                factor = 2.5
                oval( oncurve[0]-(radio*(factor/2)),oncurve[1]-(radio*(factor/2)),radio*factor,radio*factor)
            previous_oncurve = oncurve
    with savedState():
        strokeWidth(0)
        translate(x_offset-649, -164)
        fill(0.0, 0.6588235294117647, 0.4196078431372549)
        drawPath(tx)
    #saveImage(f'/Users/imac/Work/Olivetti/Glifos/Verde/{nombre}_{x:0>4}.png')
saveImage(f'~/Desktop/{nombre}.mp4')

