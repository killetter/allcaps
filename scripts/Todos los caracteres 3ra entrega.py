path = "../fonts/AC-Jade-Regular.otf"
lista = ["A", "J", "j", "k", "M", "Odieresis", "R", "S", "s", "t", "u", "x", "y", "z", "at", "ampersand", "question", "exclam", "semicolon", "parenright", "quotedblright", "zero", "one", "two", "three", "four", "five", "seven", "eight", "nine"]

nombre = 'Jade'
margen_x= 39.99
margen_y = 30

fs = FormattedString()
font(path)

#print(x)
fs.font(path)
#print(x)
fs.fontSize(135)
fs.lineHeight(141.22)
fs.fill(1.00,0.93,0.00)

for i, name in enumerate(lista):
    #print(name)
    fs.appendGlyph(name, "space",)
while fs:
    #newPage('Letter')
    newPage(1500,1500)
    fill(0.16,0.14,0.36)
    rect(0,0,1500,1500)
    fs=textBox(fs, (margen_x,margen_y*.1,width()-margen_x*2,height()-margen_y*1.6), align='center')

#saveImage(f'{nombre}.png')
