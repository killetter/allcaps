def hextofloats(h):
    color =  tuple(int(h[i:i + 2], 16) / 255. for i in (1, 3, 5))
    print(f"{color}")
    return color

#Colores #fffff
codigo_bg = "#00a86b"
codigo_fg = "#00a86b"

#Llamado a la funcion hexagesimal a floats
bg_hex = hextofloats(codigo_bg)
fg_hex = hextofloats(codigo_fg)
     
def r_g_b (r,g,b):
    factor = 1/255
    r_color = factor * r
    g_color = factor *g
    b_color = factor * b
    print(f"fill({r_color:.2f},{g_color:.2f},{b_color:.2f})")
    return r_color , g_color , b_color
    
    
sol = r_g_b(7,145,240)
luna = r_g_b(245,65,21)
newPage(500,500)
fill(*sol)
rect(0,0,500,500)
fill(*luna)
rect(100,100,300,300)

#Color hex
newPage(500,500)
fill(*bg_hex)
#rect(0,0,500,500)
fill(*fg_hex)
rect(100,100,300,300)


     