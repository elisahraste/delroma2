from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.logger import Logger
import mysql.connector
import re

class origen(ScreenManager):
    pass

class origen2(ScreenManager):
    pass

class inicio(ScreenManager):
    pass

class login2(ScreenManager):
    pass

class menu(ScreenManager):
  pass

class mesas(ScreenManager):
    pass

class puff(ScreenManager):
    pass

class sillones(ScreenManager):
    pass

class pedido(ScreenManager):
    pass

class compra(ScreenManager):
    pass






Window.size = (320, 600)



class MainApp(MDApp):
    pass

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  
     
    conexion = mysql.connector.Connect(host = "190.228.29.62",
                                                        user = "elisa_dev",
                                                        passwd = "xgvd1z4hxbA3",
                                                        database = "sistemas_colaborativos")
    cursor = conexion.cursor()
    cursor.execute("select * from user")
    for i in cursor.fetchall():
        print(i[0], i[1])
    
    print ("conexion ok")
    
    
    
    def build (self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("origen.kv"))
        screen_manager.add_widget(Builder.load_file("login2.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("inicio.kv"))      
        screen_manager.add_widget(Builder.load_file("menu.kv"))
        screen_manager.add_widget(Builder.load_file("mesas.kv"))
        screen_manager.add_widget(Builder.load_file("puff.kv"))
        screen_manager.add_widget(Builder.load_file("sillones.kv"))
        screen_manager.add_widget(Builder.load_file("compra.kv"))
        screen_manager.add_widget(Builder.load_file("origen2.kv"))
        return screen_manager
    



        
    def send_data(self, email, password):
        if re.fullmatch(self.regex, email.text):
            self.cursor.execute(f"insert into user values ('{email.text}', '{password.text}')")
            self.conexion.commit()
            email.text = ""
            password.text = ""
            print("registro correcto")
            self.root.current = 'login' 
            for i in self.cursor.fetchall():
                print(i[0], i[1])    
        else:
            print("email invalido")  
            self.root.current = 'inicio'      
        
    def receive_data(self, email, password):
        self.cursor.execute("select * from user")
        email_list = []
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if email.text in email_list and email.text != "":
            self.cursor.execute(f"select password from user where email = '{email.text}'")
            for j in self.cursor:
                    if password.text == j[0]:
                        print("Ingreso correcto")
                        self.root.current = 'menu'

                    else:
                        print("Verifique su password")
                        self.dialog = MDDialog(
                            title = "Login",
                            text = f"Verifique los datos ingresados",
                            buttons = [
                                MDFlatButton(
                                text = "Ok", text_color = self.theme_cls.accent_color,
                                on_release = self.close_dialog                                
                                ),
                            ],
                        )
                        self.dialog.open()
        else:
            print("Usuario Inexistente")
            self.dialog = MDDialog(
                title = "Login",
                text = f"Verifique los datos",
                buttons = [
                    MDFlatButton(
                        text = "Ok", text_color = self.theme_cls.accent_color,
                        on_release = self.close_dialog
                        ),
                    ],
                )
            self.dialog.open()
                        
    def close_dialog(self, obj):
        self.dialog.dismiss()
        
      
        
    def clwindow(self):
        MDApp.get_running_app().stop()
        Window.close()
        
        

    def on_stop(self):
        Logger.critical('Adios')
           

            
        
    def check_login(self):
        if self.receive_data():
            return True
        
        
    def do_login(self):
        if self.check_login():
            self.manager.current = 'menu'

    def send_pedido(self, **kwargs):
       
        """n1 = int(mesa.text)
        n2 = int(sillon.text)
        n3 = int(puff.text)
        total = n1 + n2
        #self.n2 = int(self.sillon.text)
        #self.n3 = int(self.puff.text)
        #self.total = n1 + n2 + n3
        print (total)   
        #print (total)

class Pedido(ScreenManager):
    mesa= ObjectProperty()
    sillon= ObjectProperty()
    total = ObjectProperty()"""
            

#my_instance = MainApp()
#my_instance.send_pedido()
MainApp().send_pedido()


#postgres://elisa_sistemas_colaborativos_user:fX1d2rHGdZMDFljjbvW45oOC9w5mpRqZ@dpg-chknbhu7avj217f3npvg-a.oregon-postgres.render.com/elisa_sistemas_colaborativos
   
if __name__=="__main__":
   # LabelBase.register(name="MPoppins", fn_regular= c://user)
   MainApp().run()

