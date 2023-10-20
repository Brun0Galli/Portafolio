import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import webbrowser
import datetime
import requests
import os
class Asistente:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0" )
        self.recognizer = sr.Recognizer()
        self.Day_list = ["qué día es hoy", "qué día de la semana es hoy", "en qué mes estamos", "qué año es"]
    def transformar_voz_en_txt(self):
        with sr.Microphone() as source:
            self.recognizer.non_speaking_duration = 0.1
            self.recognizer.pause_threshold = 0.5
            print("Ya puedes hablar")
            audio = self.recognizer.listen(source)
            try:
                pedido = (self.recognizer.recognize_google(audio, language='es-ES')).lower()
                print("Tu pedido es: " + pedido)
                with open("registro_de_voz.txt", "a", encoding='utf-8') as file:
                    file.write(f"{datetime.datetime.now()}: {pedido}\n")
                return pedido
            except sr.UnknownValueError:
                print("No te entendi")
                return "sigo esperando"
            except sr.RequestError:
                print("No hay servicio")
                return "sigo esperando"
            except:
                print("Algo salio mal")
                return "sigo esperando"

    def talk(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def request_day(self, request):
        day = datetime.date.today()
        calendar_days = {0: "lunes", 1: "martes", 2: "miercoles", 3: "jueves", 4: "viernes", 5: "sabado", 6: "domingo"}
        calendar_month = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
        try:
            if "qué día es hoy" in request:
                self.talk(day.day)
            elif "qué día de la semana es hoy" in request:
                self.talk(f"Hoy es {calendar_days[day.weekday()]}")
            elif "en qué mes estamos" in request:
                self.talk(f"Estamos en {calendar_month[day.month]}")
            elif "qué año es" in request:
                result3 = (f"Estamos en el año {day.year}")
                self.talk(result3)
        except:
            print("No te entendí")
    def request_time(self, request):
        time = datetime.datetime.now()
        try:
            if "qué hora es" in request:
                self.talk(f"Son las {time.hour} horas y {time.minute} minutos")
        except:
            print("No te entendí")

    def Current_City(self, request,listCities):
        request= request.lower()
        for city in listCities:
            try:
                if city in request:
                    return city
            except:
                self.talk("No se entendió el nombre de la ciudad")

    def open_app(self, request):
        self.app_name = request.replace("abre", "")
        if "word" in self.app_name:
            os.system("start WINWORD.EXE")
        else:
            os.system(f"start {self.app_name}")
    def request_weather(self, request):

        api_key= "7798b173bc514be4b6b45046231310"
        base_url = "http://api.weatherapi.com/v1/current.json"
        listCities=["ciudad de méxico","guadalajara","monterrey","puebla","tijuana","tuxtla gutierrez",
                    "mérida","oaxaca","san luis potosí","aguascalientes","chihuahua","morelia","cuernavaca",
                    "durango","villahermosa","culiacán","hermosillo","xalapa","zacatecas","saltillo","colima",
                    "mexicali","querétaro","chilpancingo","guanajuato","tampico"]
        city_name = self.Current_City(request,listCities)
        if "qué clima hay" in request:
            completa_url = f"{base_url}?key={api_key}&q={city_name}"
            response = requests.get(completa_url)
            data = response.json()
            if response.status_code != "404":
                clima_info = data["current"]
                current_temperature = clima_info["temp_c"]
                self.talk(f"En {city_name} la temperatura es de {current_temperature} grados")
            else:
                self.talk("No se encontró la ciudad")
    def handle_request(self, request):
        if request in self.Day_list:
            self.request_day(request)
 #hola
        elif "qué hora es" in request:
            self.request_time(request)
        elif "qué clima hay" in request:
            self.request_weather(request)
        elif "abrir youtube" in request:
            webbrowser.open("https://www.youtube.com/")
        elif "abrir google" in request:
            webbrowser.open("https://www.google.com/")
        elif "busca en google" in request:
            request= request.replace("busca en google","")
            self.talk("Buscando en google")
            pywhatkit.search(request)
        elif "chiste" in request:
            self.talk(pyjokes.get_joke('es'))
        elif "abre" in request:
            self.open_app(request)



    def run_assistant(self):
        inicio= self.transformar_voz_en_txt().lower()
        if "enciéndete" in  inicio:
            self.talk("Hola, ¿en qué puedo ayudarte?")
            decision = False
            while not decision:
                request = self.transformar_voz_en_txt()
                self.handle_request(request)
                if "terminar" in request:
                    self.talk("Hasta luego")
                    decision = True


if __name__ == "__main__":
    usuario = Asistente()
    usuario.run_assistant()