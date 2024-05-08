import urllib.parse
import requests


from colorama import Fore , init
init()

#para disenio
lred = Fore.LIGHTRED_EX
lcyan = Fore.LIGHTCYAN_EX


def switch_body(option):
    switcher = {
        "1": "square",
        "2": "mosaic",
        "3": "dot",
        "4": "circle",
        "5": "circle-zebra",
        "6": "circle-zebra-vertical",
        "7": "circular",
        "8": "edge-cut",
        "9": "edge-cut-smooth",
        "10": "japnese",
        "11": "leaf",
        "12": "pointed",
        "13": "pointed-edge-cut",
        "14": "pointed-in",
        "15": "pointed-in-smooth",
        "16": "pointed-smooth",
        "17": "round",
        "18": "rounded-in",
        "19": "rounded-in-smooth",
        "20": "rounded-pointed",
        "21": "star",
        "22": "diamond"
    }
    return switcher.get(option, "Opción no válida")

options_vista_body = [
    "1. Square",
    "2. Mosaic",
    "3. Dot",
    "4. Circle",
    "5. Circle-zebra",
    "6. Circle-zebra-vertical",
    "7. Circular",
    "8. Edge-cut",
    "9. Edge-cut-smooth",
    "10. Japnese",
    "11. Leaf",
    "12. Pointed",
    "13. Pointed-edge-cut",
    "14. Pointed-in",
    "15. Pointed-in-smooth",
    "16. Pointed-smooth",
    "17. Round",
    "18. Rounded-in",
    "19. Rounded-in-smooth",
    "20. Rounded-pointed",
    "21. Star",
    "22. Diamond"
]

options_gradient_colors = {
    "Greeny": (Fore.GREEN, Fore.LIGHTGREEN_EX),
    "Bluey": (Fore.BLUE, Fore.LIGHTBLUE_EX),
    "Orangy": (Fore.YELLOW, Fore.LIGHTYELLOW_EX),
    "Redy": (Fore.RED, Fore.LIGHTRED_EX)
}

options_basic_colors = {
    "Rojo": Fore.RED,
    "Azul": Fore.BLUE,
    "Amarillo": Fore.YELLOW
}

def option_vista_color():
    for i, color in enumerate(options_basic_colors, start=1):
        print("\t" f"{i}. {options_basic_colors[color]}{color}{Fore.RESET}")
    for i, color in enumerate(options_gradient_colors, 4):
        color1, color2 = options_gradient_colors[color]
        print("\t" f"{i}. {color} ({color1}De este color a {Fore.RESET}{color2}este color {Fore.RESET})")

def options_eleccion_color(option_color):
    color2= 'FF0000'
    if option_color == 1:
        color1 = "#FF0000"
    elif option_color == 2:
        color1 = "#0000FF"
    elif option_color == 3:
        color1 = "#FFFF00"
    elif option_color == 4:
        color1 = "#7ED957"
        color2 = "#C1FF72"
    elif option_color == 5:
        color1 = "#004AAD"
        color2 = "#5271FF"
    elif option_color == 6:
        color1 = "#FFBD59"
        color2 = "#FFDE59"
    elif option_color == 7:
        color1 = "#D12C2C"
        color2 = "#FF3131"

    return color1, color2

def options_format(option_format):
    if option_format == 1:
        return "png"
    elif option_format == 2:
        return "svg"
    elif option_format == 3:
        return "pdf"
    else:
        return "eps"

def option_eye_choices(option):
    switcher = {
        0: "frame0",
        1: "frame1",
        2: "frame2",
        3: "frame3",
        4: "frame4",
        5: "frame5",
        6: "frame6",
        7: "frame7",
        8: "frame8",
        9: "frame9",
        10: "frame10",
        11: "frame11",
        12: "frame12",
        13: "frame13",
        14: "frame14",
        15: "frame15",
        16: "frame16"
    }
    return switcher.get(option, "frame0")

def option_ball_choices(option):
    switcher = {
        1: "ball1",
        2: "ball2",
        3: "ball3",
        4: "ball4",
        5: "ball5",
        6: "ball6",
        7: "ball7",
        8: "ball8",
        9: "ball9",
        10: "ball10",
        11: "ball11",
        12: "ball12",
        13: "ball13",
        14: "ball14",
        15: "ball15",
        16: "ball16",
        17: "ball17",
        18: "ball18",
        19: "ball19"
    }
    return switcher.get(option, "ball1")

nombres_archivos = ['logo1.png', 'logo2.png', 'logo3.png', 'logo4.png']

#api
url = "https://api.qrcode-monkey.com//qr/custom"
url2 = 'https://api.qrcode-monkey.com/qr/uploadImage'

#ingresa por consola los parametros
print("Selecciona el tipo de dato:")
print("1. URL")
print("2. Texto plano")
print("3. Email")
print("4. Teléfono")
print("5. SMS")
option_type = int(input("Opción: "))
Data = input("Ingresa información para tu QR: ")


if option_type == 1:
    Data = urllib.parse.quote(Data)
elif option_type == 3:
    Data = f"mailto:{Data}"
elif option_type == 4:
    Data = f"tel:{Data}"
elif option_type == 5:
    sms_number = input("Ingresa el número de teléfono: ")
    sms_text = Data
    Data = f"sms:{sms_number}?body={urllib.parse.quote(sms_text)}"



print("\nForma:")
for option in options_vista_body:
    print("\t" + option)
option_body = input("Ingresa el número correspondiente a la forma: ")
body = switch_body(option_body)


size = int(input("\nIngresa el tamaño del código QR (de 100 a 1000 pixels): "))



print("\nColor:")

option_vista_color()
option_color= int(input("Elige opcion de color:"))
color1,color2=options_eleccion_color(option_color)


option_eye = int(input("Selecciona el tipo de ojo del código QR (0 al 16): "))
eye = option_eye_choices(option_eye)

option_eyeBall = input("Selecciona el tipo de pupila del ojo del código QR (1 al 19): ")
ball= option_ball_choices(option_eyeBall)

logo_option = input("\n¿Deseas agregar un logo al código QR? (si/no): ")


if logo_option.lower() == "si":
    option_logo = int(input("Elige un logo (1, 2, 3, 4): "))
    adjusted_option = option_logo - 1 
    if 0 <= adjusted_option < len(nombres_archivos):
        files = {'file': open(f'C:/Users/Kasssssssssss/Desktop/Code Generator(API de QR Code Monkey_Python_Requests)/logo/{nombres_archivos[adjusted_option]}', 'rb')}
        response = requests.post(url2, files=files)
        logo = response.json()['file']
    else:
        print("Opción de logo no válida.")
        logo = ""
else:
    logo = ""


if (option_color == 1 or option_color == 2 or option_color == 3  ):
    option_format = int(input("\nFormato de descarga: \t1.png\t2.svg\t3.pdf\t4.eps "))
    download_format = options_format(option_format)
    payload = {"data": Data, "config": {"body": body, "eye": eye, "eyeBall": ball, "bodyColor": "#000000", "bgColor": "#FFFFFF", "eye1Color": color1, "eye2Color": color1, "eye3Color": color1, "eyeBall1Color": color1, "eyeBall2Color": color1, "eyeBall3Color": color1, "gradientColor1": color1, "gradientColor2": color1, "gradientType": "linear", "gradientOnEyes": "true", "logo": logo, "logoMode": "clean"}, "size": size, "download": "imageUrl", "file": download_format}

else:
    option_format=int(input("\nFormato de descarga: \t1.png\t2.svg "))
    download_format = options_format(option_format)
    payload = {"data":Data,"config":{"body":body,"eye":eye,"eyeBall":ball,"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":color1,"eye2Color":color1,"eye3Color":color1,"eyeBall1Color":color2,"eyeBall2Color":color2,"eyeBall3Color":color2,"gradientColor1":color1,"gradientColor2":color2,"gradientType":"linear","gradientOnEyes":"true","logo":logo,"logoMode":"clean"},"size":size,"download":"imageUrl","file":download_format}     

#Enviando una solicitud POST a la API de QR Code Monkey con los datos necesarios para generar un código QR
resp = requests.post(url , json=payload)


if resp.status_code == 200 :
    print(lcyan+"\n[+] Status : Exito!!\n")
    OutPut = resp.json()
    Link = OutPut.get('imageUrl')
    Link = "http:" + Link
    print(Link)    
    print(lcyan + "")

    response = requests.get(Link)
    #la extension si o si debe estar en el mismo formato que lo generaste :)
    name_descarga = input("Nombre descarga (qr.extension) : ")
    if len(name_descarga) == 0 :
        name_descarga = "qr.png"

    file = open(name_descarga, "wb")
    file.write(response.content)
    file.close()

    print(lcyan + "\nEl qr:  ",name_descarga," se descargo correctamente.")

else:
    print(lred +"[-] Status : Error ",resp.status_code)


