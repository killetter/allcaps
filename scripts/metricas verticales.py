#Olivetti metricas
#Get the font
thisFont = Glyphs.font
#Get the masters
allMasters = thisFont.masters
#Get The glyphs
allGlyphs = thisFont.glyphs
ascendentes = 780
capHeight = 700
xHeight = 510
descendentes = -220 

#Loop in masters /// enumerate ayuda a iterar sobre el indice de las capas 
for index, master in enumerate(allMasters):
    master.xHeight = xHeight
    master.ascender = ascendentes
    master.capHeight = capHeight
    master.descender = descendentes

    #print(master.alignmentZones)
    
    print(f"xHeight: {master.xHeight} | Ascendentes: {master.ascender} | CapHeight: {master.capHeight} | Descendentes: {master.descender} | ")