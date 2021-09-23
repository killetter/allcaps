path = "../fonts/AC-Jade-Regular.otf"
lista =   [ "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "k", "L", "l", "M", "m", "N", "n", "Ntilde", "ntilde", "Odieresis", "oacute", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "w", "x", "y", "z", "at", "ampersand", "question", "exclam", "semicolon", "parenright", "quotedblright", "zero", "one", "two", "three", "four", "five", "seven", "eight", "nine", "space", "dieresis", "acute", "tilde",]


nombre = 'Jade'
margen_x= 44.99
margen_y =19

fs = FormattedString()
font(path)

#print(x)
fs.font(path)
#print(x)
fs.fontSize(108)
fs.lineHeight(111.22)
fs.fill(1)

for i, name in enumerate(lista):
    #print(name)
    fs.appendGlyph(name, "space",)
while fs:
    #newPage('Letter')
    newPage(1280,720)
    fill(0.0, 0.6588235294117647, 0.4196078431372549)
    rect(0,0,1500,1500)
    fs=textBox(fs, (margen_x,margen_y*.1,width()-margen_x*2,height()-margen_y*1.6), align='center')

    saveImage(f'../Imagenes/{nombre}.png')
