from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton, MDRectangleFlatButton, MDIconButton
import ezgmail

try:
    ezgmail.init()
except Exception:
    pass

Window.size = (300, 500)
""
screen_helper = """
ScreenManager:
    MenuScreen:
    
    ProfileScreen:




<MenuScreen>:

    name: 'menu'

    Screen:
        BoxLayout:
            orientation : 'vertical'
            MDToolbar:
                title: 'FutureMails'
                
                elevation: 10

            

            ScrollView:
                MDList:
                    id: container
                    OneLineIconListItem:
                        text: '#Facts from the future'
                        IconLeftWidget:
                            icon: 'rocket'  
                        
                    TwoLineIconListItem:
                        text: '#Fact1'
                        secondary_text: 'Gravity sleeps'
                        on_press: app.showthem2()
                        IconLeftWidget:
                            icon: 'leaf'
                        
                        
                    TwoLineIconListItem:
                        text: '#Fact2'
                        secondary_text: 'where is the mind?'
                        on_press: app.showthem3()
                        IconLeftWidget:
                            icon: 'leaf'
                        
                        
                    TwoLineIconListItem:
                        text: '#Fact3'
                        secondary_text: 'Finally ,a code for nature'
                        on_press: app.showthem4()
                        IconLeftWidget:
                            icon: 'leaf'
                        
                        
                        
                        
                    TwoLineIconListItem:
                        text: '#Fact4'
                        secondary_text: 'Human AI'
                        on_press: app.showthem5()
                        IconLeftWidget:
                            icon: 'leaf'
                        
                        
                    TwoLineIconListItem:
                        text: '#Fact5'
                        secondary_text: 'Rapture happened!'
                        on_press: app.showthem7()
                        IconLeftWidget:
                            icon: 'leaf'
                        
                    TwoLineIconListItem:
                        text: '#Fact?'
                        secondary_text: 'want more ?'
                        on_press: app.showthem6()
                        IconLeftWidget:
                            icon: 'leaf'
                    

            MDBottomAppBar:
                MDToolbar:
                    mode: 'end'
                    type: 'bottom'
                    icon: 'email'
                    on_action_button: root.manager.current = 'Profile'

<ProfileScreen>:


    name: 'Profile'

    MDTextField:
        id: dish 
        hint_text: " Email "
        mode: "rectangle"
        size_hint: 10, None
        height: "300dp"
        icon_right : "email"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        size_hint_x: None
        width : 250

    MDTextFieldRect:
        id: container 
        hint_text: " Message "
        mode: "rectangle"
        multiline: True
        size_hint: 10, None
        height: "300dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width : 275

    MDIconButton:
        icon: "data/logo/kivy-icon-256.png"
        pos_hint: {'center_x': 0.07, 'center_y': 0.97}
        on_release: root.manager.current = 'menu'
        user_font_size: "2sp"

    MDFloatingActionButton:
        icon: "send"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.1}
        on_release: app.navv()

    MDFloatingActionButton:
        icon: "clock"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.2}
        on_release: app.show_date_picker()



"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='Profile'))


class Main(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen

    def get_date(self, date):
        self.samuel = date
        return self.samuel

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)

        date_dialog.open()

    def navv(self):
        message = self.root.get_screen('Profile').ids.container.text
        print(repr(message))
        email = self.root.get_screen('Profile').ids.dish.text
        yes_no = 'Your message has been sent through a time machine and your future self has seen it already' \
                 ' (you would just have to wait till that time becomes a present time ).' \
                 " \n i hope you didn't send a message to the past" \
                 "(you wouldn't want to interfere with the space time " \
                 ' continuum) <br> \n\nStay safe till you get the message , ' \
                 "\n and  don't reply to this message.\n\nThank you !!\n   "

        try:
            time = self.samuel
            s_time = str(time)
            sub = s_time + "',@'" + email
            assert ( email != '')
            ezgmail.send('futuremails3@gmail.com', sub, message) #
            self.send = ezgmail.send(email, 'FutureMails', yes_no,mimeSubtype='html')

            self.show()

            self.root.get_screen('Profile').ids.dish.text = ''
            self.root.get_screen('Profile').ids.container.text = ''
        except:
            self.showthem()


    # a snack bar appears when there is an error
    def show(self):
        Snackbar(text=" message sent",
                 duration=3,
                 ).show()

    def showthem(self):

        close = MDFlatButton(text='close',
                             on_press=self.close)

        self.dialog = MDDialog(title='Time/internet error',
                               size_hint=(0.6, 1),
                               text='Please set time \n or Check your connection!',
                               buttons=[close])
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

    def showthem2(self):

        open = MDFlatButton(text='close',
                            on_press=self.close2)

        self.dialog2 = MDDialog(title='Gravity sleeps',
                                size_hint=(0.6, 1),
                                text='Once in a thousand years ,gravity sleeps . you could literally jump off the planet',
                                buttons=[open])
        self.dialog2.open()

    def close2(self, obj):
        self.dialog2.dismiss()

    def showthem3(self):

        close = MDFlatButton(text='close',
                             on_press=self.close3)

        self.dialog3 = MDDialog(title='Where is the mind?',
                                size_hint=(0.6, 1),
                                text='The next time you see a brain scientist tel him ,it is in the stomach',
                                buttons=[close])
        self.dialog3.open()

    def close3(self, obj):
        self.dialog3.dismiss()

    def showthem4(self):

        close = MDFlatButton(text='close',
                             on_press=self.close4)

        self.dialog4 = MDDialog(title='Finally a code for nature ',
                                size_hint=(0.6, 1),
                                text='Rejoice o ye programmers now you can code plants to grow how ever you want. '
                                     + 'You are probably imagining hackers programming natural disasters,ikr ',
                                buttons=[close])
        self.dialog4.open()

    def close4(self, obj):
        self.dialog4.dismiss()

    def showthem5(self):

        close = MDFlatButton(text='close',
                             on_press=self.close5)

        self.dialog5 = MDDialog(title='Human AI',
                                size_hint=(0.6, 1),
                                text='Believe me ,it is crazy here ,imagine someone hacking into your brain '
                                     + ' and replacing your memory with a fake one. hard to tell what is false right?',
                                buttons=[close])
        self.dialog5.open()

    def close5(self, obj):
        self.dialog5.dismiss()

    def showthem6(self):

        close = MDFlatButton(text='close',
                             on_press=self.close6)

        self.dialog6 = MDDialog(title='want more?',
                                size_hint=(0.6, 1),
                                text='we do not  want to interfere  with the space time continuum. '
                                     + 'its better to keep it secret ',
                                buttons=[close])
        self.dialog6.open()

    def close6(self, obj):
        self.dialog6.dismiss()

    def showthem7(self):

        close = MDFlatButton(text='close',
                             on_press=self.close7)

        self.dialog7 = MDDialog(title='Rapture happened',
                                size_hint=(0.6, 1),
                                text='you are probably wondering why i am still here ',
                                buttons=[close])
        self.dialog7.open()

    def close7(self, obj):
        self.dialog7.dismiss()


Main().run()

"""  
i added 2 extra(showthem and show) functinns ,one to indicate there is no internet .
the other to show that time gas not been set
its itill a bit unclear tho,but as time goes i would get it
"""