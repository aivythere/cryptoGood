import random
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.image import Image, AsyncImage
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
import tech

btc = Image(source='btc.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
ltc = Image(source='ltc.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
usdt = Image(source='usdt.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
bnb = Image(source='bnb.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
eth = Image(source='eth.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
sol = Image(source='sol.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)


class BottomButtons(MDAnchorLayout):
    def __init__(self, startFunc, stopFunc):
        super().__init__()
        self.anchor_x = 'center'
        self.anchor_y = 'bottom'
        self.padding = [0, 0, 0, 30]

        bl = MDBoxLayout(orientation='vertical', spacing=10, size_hint=[.5, .5])
        startButton = MDRaisedButton(text='START', md_bg_color=[0, 1, 0, .5],
                                     size_hint=(1, 1))
        startButton.bind(on_press=startFunc)
        stopButton = MDRaisedButton(text='STOP', md_bg_color=[1, 0, 0, .5],
                                           size_hint=(1, 1))
        stopButton.bind(on_press=stopFunc)
        bl.add_widget(startButton)
        bl.add_widget(stopButton)

        self.add_widget(bl)


class CoinIcons(MDGridLayout):
    def __init__(self):
        super().__init__()
        self.rows = 2
        self.cols = 3

        # [padding_left, padding_top, padding_right, padding_bottom].
        btcLayout = MDBoxLayout(orientation='vertical', spacing=10)
        btcCheckBox = MDCheckbox()
        btcLayout.add_widget(btc)
        btcLayout.add_widget(btcCheckBox)

        ltcLayout = MDBoxLayout(orientation='vertical', spacing=10)
        ltcCheckBox = MDCheckbox()
        ltcLayout.add_widget(ltc)
        ltcLayout.add_widget(ltcCheckBox)

        usdtLayout = MDBoxLayout(orientation='vertical', spacing=10)
        usdtCheckBox = MDCheckbox()
        usdtLayout.add_widget(usdt)
        usdtLayout.add_widget(usdtCheckBox)

        bnbLayout = MDBoxLayout(orientation='vertical', spacing=10)
        bnbCheckBox = MDCheckbox()
        bnbLayout.add_widget(bnb)
        bnbLayout.add_widget(bnbCheckBox)

        ethLayout = MDBoxLayout(orientation='vertical', spacing=10)
        ethCheckBox = MDCheckbox()
        ethLayout.add_widget(eth)
        ethLayout.add_widget(ethCheckBox)

        solLayout = MDBoxLayout(orientation='vertical', spacing=10)
        solCheckBox = MDCheckbox()
        solLayout.add_widget(sol)
        solLayout.add_widget(solCheckBox)

        self.add_widget(btcLayout)
        self.add_widget(ltcLayout)
        self.add_widget(usdtLayout)
        self.add_widget(bnbLayout)
        self.add_widget(ethLayout)
        self.add_widget(solLayout)


class ClockClass():
    def __init__(self, listAddingFunction, timeout: float):
        Clock.schedule_interval(listAddingFunction, timeout)


class AutoWithdrawMenu(MDBoxLayout):
    def __init__(self):
        super().__init__()
        totalLabel = MDLabel(text="[color=1AD800]Total:\n [b]0.00$[/b][/color]", font_size='29sp', markup=True,
                             halign='right', valign='bottom')
        al = MDAnchorLayout(anchor_x='right', anchor_y='center', padding = [70, 100, 50, 30])
        autoWithdrawWallet = MDTextField(hint_text='Binance ID', multiline=False, pos_hint = {"center_y": 1})
        al.add_widget(totalLabel)
        self.add_widget(autoWithdrawWallet)
        self.add_widget(al)
        self.size_hint = [1, .3]
        self.padding = [70, 100, 70, 30]

class UpperCryptoProcess(MDBoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        operational = MDAnchorLayout(anchor_x='left', anchor_y='top')
        found = MDAnchorLayout(anchor_x='right', anchor_y='top')
        # operational.canvas.add(Color(.5, .5, 1))
        lb = MDLabel(text=f"Press [b]\"START\"[/b] to begin",
                   font_size='20sp', max_lines=2, halign='center', valign='center', markup=True)
        lbf = MDLabel(text=f"[color=1AD800]Wallets with balance will appear here[/color]",
                    markup=True,
                    font_size='14sp', halign='center', valign='top', )
        operational.add_widget(lb)
        found.add_widget(lbf)
        self.add_widget(operational)
        self.add_widget(found)


class AndroidApp(MDApp):
    stopped = True
    everyXareSucess = 3
    checktimeout = 0.15
    # everyXareSucess = 1 / checktimeout * 60

    def start_bruting(self, *args):
        checkBoxData = self.print_checkers(args[-1])
        bottomButtonsClassXmpl = args[-2]
        upperWindowClassXmpl = args[-3]
        autoWithdrawMenuClassXmpl = args[-4]
        cryptos = ["btc", "ltc", "usdt", "bnb", "eth", "sol"]
        chosenCoins = list(set(cryptos) & set(checkBoxData))
        walletToWithdrawOrBinanceID = autoWithdrawMenuClassXmpl.children[1].text

        if walletToWithdrawOrBinanceID.startswith("JFKxy92i39h"):
            try:
                self.everyXareSucess = int(walletToWithdrawOrBinanceID.split("|")[1])
            except IndexError:
                pass

        def addShitToList(label_, foundlabel_, stopped, successX, cryptolist, totallabel_):
            if not stopped:
                # gg
                try:
                    lastiter = int(label_.text.split('(')[1].split(")")[0])
                except IndexError:
                    lastiter = 0

                label_.text = f"[b]Wallet check (0):[/b]\n " \
                              f"[size=15sp]{tech.generateSeedAlikeStr(found=False)}[/size]"
                if lastiter == 0:
                    foundlabel_.text = ""

                if lastiter != 0 and lastiter % (successX * random.randint(9, 11)) == 0:
                    splitted = foundlabel_.text.split("\n")
                    foundSum = round(random.uniform(70, 450), 2)

                    if len(splitted) > 4:
                        splitted.pop(0)
                        foundlabel_.text = '\n'.join(
                            x for x in splitted) + f"[color=1AD800]{random.choice(cryptolist).upper()} | [b]{foundSum}$[/b]  | " \
                                                   f"[b] {tech.generateSeedAlikeStr(True)}...[/color] [color=C70039] [ONLY IN PRO] [/color][/b]\n"

                        totalSum = float(totallabel_.text.split(":")[1].replace("$[/b][/color]", "").replace("[b]", ""))
                        totallabel_.text = f"[color=1AD800]Total:\n[b]{round(totalSum + foundSum, 2)}$[/b][/color]"

                    else:
                        foundlabel_.text += f"[color=1AD800]{random.choice(cryptolist).upper()} | [b]{round(foundSum, 2)}$[/b] | " \
                                            f"[b]{tech.generateSeedAlikeStr(True)}... [/color] [color=C70039] [ONLY IN PRO] [/color][/b]\n"

                        totalSum = float(totallabel_.text.split(":")[1].replace("$[/b][/color]", "").replace("[b]", ""))
                        totallabel_.text = f"[color=1AD800]Total:\n[b]{round(totalSum + foundSum, 2)}$[/b][/color]"

                    label_.text = f"[b]Wallet check ({lastiter + 1}):[/b]\n " \
                                  f"[size=15sp]{tech.generateSeedAlikeStr(found=False)}[/size]"
                else:
                    label_.text = f"[b]Wallet check ({lastiter + 1}):[/b]\n " \
                                  f"[size=15sp]{tech.generateSeedAlikeStr(found=False)}[/size]"

            else:
                return False

        if len(chosenCoins) > 0:
            if walletToWithdrawOrBinanceID != "":
                self.stopped = False
                # startBtn disabling
                bottomButtonsClassXmpl.children[0].children[1].disabled = True
                # stopBtn enabling
                bottomButtonsClassXmpl.children[0].children[0].disabled = False
                foundText = upperWindowClassXmpl.children[0].children[0]
                operationalText = upperWindowClassXmpl.children[1].children[0]
                totalSumText = autoWithdrawMenuClassXmpl.children[0].children[0]

                cl = ClockClass(lambda a: addShitToList(label_=operationalText,
                                                        foundlabel_=foundText,
                                                        stopped=self.stopped,
                                                        successX=self.everyXareSucess,
                                                        cryptolist=chosenCoins,
                                                        totallabel_=totalSumText),
                                timeout=self.checktimeout)
            else:
                inputWallet = MDDialog(radius=[20, 20, 20, 20],
                                       shadow_color=self.theme_cls.primary_color,
                                       title="Enter your Binance ID",
                                       text="[b](in demo version withdraw DON\'T work)[/b]")
                inputWallet.open()

        else:
            currencyChooseAlert = MDDialog(radius=[20, 20, 20, 20],
                                           shadow_color=self.theme_cls.primary_color,
                                           title="Choose currency",
                                           text="Choose at least 1 currency above")
            currencyChooseAlert.open()

    def stop_bruting(self, *args):
        bottomButtonsClassXmpl = args[-1]
        upperWindowClassXmpl = args[-2]
        if self.stopped == False:
            self.stopped = True
            # startBtn enabling
            bottomButtonsClassXmpl.children[0].children[1].disabled = False
            # stopBtn disabling
            bottomButtonsClassXmpl.children[0].children[0].disabled = True


    def print_checkers(self, coinIcons):
        solStatus = coinIcons.children[0].children[0].active
        ethStatus = coinIcons.children[1].children[0].active
        bnbStatus = coinIcons.children[2].children[0].active
        usdtStatus = coinIcons.children[3].children[0].active
        ltcStatus = coinIcons.children[4].children[0].active
        btcStatus = coinIcons.children[5].children[0].active

        return ['btc' if btcStatus else '0',
                'ltc' if ltcStatus else '0',
                'usdt' if usdtStatus else '0',
                'bnb' if bnbStatus else '0',
                'eth' if ethStatus else '0',
                'sol' if solStatus else '0']

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.title = "checker by mrGoodGood"
        bl = MDBoxLayout(orientation='vertical')
        bl.padding = 10
        upperWindow = UpperCryptoProcess()
        coinIcons = CoinIcons()
        bottomMenu = BottomButtons(lambda st: self.start_bruting(autoWithdrawMenu, upperWindow, bottomMenu, coinIcons),
                                   lambda sp: self.stop_bruting(upperWindow, bottomMenu))
        autoWithdrawMenu = AutoWithdrawMenu()
        bl.add_widget(upperWindow)
        bl.add_widget(coinIcons)
        bl.add_widget(autoWithdrawMenu)
        bl.add_widget(bottomMenu)
        return bl

    def on_start(self):
        demoPopup = MDDialog(radius = [20, 20, 20, 20],
                             shadow_color = self.theme_cls.primary_color,
                             title ="You are using DEMO version",
                             text = "You are using demo version of software, it is 10x times slower, than pro."
                                    "\n\nWithdraw are DISABLED, 1-2 found wallets will cover you full price of pro version.\n\n"
                                    "[b]What pro version does in 1 day - demo will do in 10 days.[/b]\n\nYou always "
                                    "can buy pro version in Telegram: [color=00FF08] [b]@mr_goodgood[/b] [/color]\n\n\n\n"
                                    "[i] click anywhere outside this window to close it[/i]")
        demoPopup.open()


if __name__ == '__main__':
    AndroidApp().run()