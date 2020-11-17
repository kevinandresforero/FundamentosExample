from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import tkinter as tk
from PIL import ImageTk,Image
import random

cFondo = '#'+'182b29'
fGround = '#'+'9bf2ff'

vy = 380
vx = 500

dy = 25
dx = 100

def enviarCorreo():
    
    try:
        nombre = campo1.get()
        apellido =  campo2.get()
        correo = campo4.get()
    
        msg = MIMEMultipart()
    
        message = "Bienvenido " + nombre + " " + apellido + " su codigo es el siguiente: " +str(random.randint(1000, 9999))
        # setup the parameters of the message
        password = "Vargas10"
        msg['From'] = "hackerjoker2109@gmail.com"
        msg['To'] = correo
        msg['Subject'] = "Codigo"
    
        msg.attach(MIMEText(message, 'plain'))
    
        server = smtplib.SMTP('smtp.gmail.com: 587')
    
        server.starttls()
    
        server.login(msg['From'], password)
    
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    
        server.quit()
    
        aviso="successfully sent security code to %s:" % (msg['To'])
        print(aviso)
        ventana_mensaje = tk.Toplevel()
        ventana_mensaje.title('Mensaje')
        ventana_mensaje.configure(background = cFondo)
        ventana_mensaje.geometry(str(vx+300)+'x'+str(int(vy*0.1))+'+250+250')
        lmess = tk.Label(ventana_mensaje, text=aviso,background = cFondo, foreground=fGround)
        lmess.pack()
        ventana_mensaje.mainloop()
        
    except:
        aviso = "No se pudo enviar el correo, por favor intenta llenar los campos correctamente o revisar tu conexión"
        ventana_mensaje = tk.Toplevel()
        ventana_mensaje.title('Mensaje')
        ventana_mensaje.configure(background = cFondo)
        ventana_mensaje.geometry(str(vx+300)+'x'+str(int(vy*0.1))+'+250+250')
        lmess = tk.Label(ventana_mensaje, text=aviso,background = cFondo, foreground=fGround)
        lmess.pack()
        ventana_mensaje.mainloop()


def cerrar():
    marco.destroy()

marco = tk.Tk()
marco.title('Registro de Usuario')
marco.geometry(str(vx)+'x'+str(vy)+'+350+150')
marco.resizable(0,0)

cargaF = Image.open('recursos/bgBlue.jpeg')
cargaF = cargaF.resize((int(vx), int(vy)), Image.ANTIALIAS)
photoFondo = ImageTk.PhotoImage(cargaF)
w = photoFondo.width()
h = photoFondo.height()
fondo = tk.Label(marco, image=photoFondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

l1 = tk.Label(marco, text="Nombre", background = cFondo, foreground=fGround)
l1.pack()
l1.place(x=dx, y= dy*2.8)

l2 = tk.Label(marco, text="Apellido", background = cFondo,foreground=fGround)
l2.pack()
l2.place(x=dx, y= dy*4.8)

l3 = tk.Label(marco, text="Identificación", background = cFondo,foreground=fGround)
l3.pack()
l3.place(x=dx, y= dy*6.8)

l4 = tk.Label(marco, text="Correo",background = cFondo,foreground=fGround)
l4.pack()
l4.place(x=dx, y= dy*8.8)

campo1 = tk.Entry(marco, background = fGround, foreground=cFondo)
campo2 = tk.Entry(marco, background = fGround, foreground=cFondo)
campo3 = tk.Entry(marco, background = fGround, foreground=cFondo)
campo4 = tk.Entry(marco, background = fGround, foreground=cFondo)

campo1.pack()
campo1.place(x=dx*2, y= dy*2.8)
campo2.pack()
campo2.place(x=dx*2, y= dy*4.8)
campo3.pack()
campo3.place(x=dx*2, y= dy*6.8)
campo4.pack()
campo4.place(x=dx*2, y= dy*8.8)

butR = tk.Button(marco,text='Registrar', command=enviarCorreo, background = cFondo, foreground=fGround)
butR.pack()
butR.place(x=dx*2, y= dy*11.8)

butC = tk.Button(marco,text='Cerrar', command=cerrar, background = cFondo, foreground=fGround)
butC.pack()
butC.place(x=430, y= 0)

marco.mainloop()