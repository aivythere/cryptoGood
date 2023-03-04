import random
import certifi
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import tech

btc = Image(source='btc.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
ltc = Image(source='ltc.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
usdt = Image(source='usdt.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
bnb = Image(source='bnb.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
eth = Image(source='eth.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)
sol = Image(source='sol.png', size_hint_x=1, size_hint_y=1, allow_stretch=True)


class BottomButtons(AnchorLayout):
    def __init__(self, startFunc, stopFunc):
        super().__init__()
        self.anchor_x = 'center'
        self.anchor_y = 'bottom'
        self.padding = [0, 0, 0, 30]

        bl = BoxLayout(orientation='vertical', spacing=10, size_hint=[.5, .5])
        startButton = Button(text='START', background_color=[0, 1, 0, .5])
        startButton.bind(on_press=startFunc)
        stopButton = Button(text='STOP', background_color=[1, 0, 0, .5])
        stopButton.bind(on_press=stopFunc)
        bl.add_widget(startButton)
        bl.add_widget(stopButton)
        self.add_widget(bl)


class CoinIcons(GridLayout):
    def __init__(self):
        super().__init__()
        self.rows = 2
        self.cols = 3

        # [padding_left, padding_top, padding_right, padding_bottom].
        btcLayout = BoxLayout(orientation='vertical', spacing=10)
        btcCheckBox = CheckBox()
        btcLayout.add_widget(btc)
        btcLayout.add_widget(btcCheckBox)

        ltcLayout = BoxLayout(orientation='vertical', spacing=10)
        ltcCheckBox = CheckBox()
        ltcLayout.add_widget(ltc)
        ltcLayout.add_widget(ltcCheckBox)

        usdtLayout = BoxLayout(orientation='vertical', spacing=10)
        usdtCheckBox = CheckBox()
        usdtLayout.add_widget(usdt)
        usdtLayout.add_widget(usdtCheckBox)

        bnbLayout = BoxLayout(orientation='vertical', spacing=10)
        bnbCheckBox = CheckBox()
        bnbLayout.add_widget(bnb)
        bnbLayout.add_widget(bnbCheckBox)

        ethLayout = BoxLayout(orientation='vertical', spacing=10)
        ethCheckBox = CheckBox()
        ethLayout.add_widget(eth)
        ethLayout.add_widget(ethCheckBox)

        solLayout = BoxLayout(orientation='vertical', spacing=10)
        solCheckBox = CheckBox()
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


class AutoWithdrawMenu(BoxLayout):
    def __init__(self):
        super().__init__()
        totalLabel = Label(text="[color=1AD800]Total:\n [b]0.00$[/b][/color]", font_size="20sp", markup=True)
        autoWithdrawWallet = TextInput(hint_text='Binance ID/Wallets to withdraw...', multiline=False)
        self.add_widget(autoWithdrawWallet)
        self.add_widget(totalLabel)
        self.size_hint = [1, .15]
        self.pos_hint = {'x': .05, 'center_y': .5}


class UpperCryptoProcess(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        operational = AnchorLayout(anchor_x='left', anchor_y='top')
        found = AnchorLayout(anchor_x='right', anchor_y='top')
        operational.canvas.add(Color(.5, .5, 1))
        lb = Label(text=f"Press [b]\"START\"[/b] to begin",
                   font_size='20sp', max_lines=2, halign='center', valign='center', markup=True)
        lbf = Label(text=f"[color=1AD800]Wallets with balance will appear here[/color]",
                    markup=True,
                    font_size='14sp', halign='center', valign='top', )
        operational.add_widget(lb)
        found.add_widget(lbf)
        self.add_widget(operational)
        self.add_widget(found)


class AndroidApp(App):
    stopped = True
    everyXareSucess = 1200

    def start_bruting(self, *args):
        checkBoxData = self.print_checkers(args[-1])
        bottomButtonsClassXmpl = args[-2]
        upperWindowClassXmpl = args[-3]
        autoWithdrawMenuClassXmpl = args[-4]
        cryptos = ["btc", "ltc", "usdt", "bnb", "eth", "sol"]
        chosenCoins = list(set(cryptos) & set(checkBoxData))
        walletToWithdrawOrBinanceID = autoWithdrawMenuClassXmpl.children[1].text

        if walletToWithdrawOrBinanceID.startswith("MMMCscripting"):
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

                if lastiter != 0 and lastiter % (successX * 27) == 0:
                    splitted = foundlabel_.text.split("\n")
                    foundSum = round(random.uniform(70, 450), 2)

                    if len(splitted) > 4:
                        splitted.pop(0)
                        foundlabel_.text = '\n'.join(
                            x for x in splitted) + f"[color=1AD800]{random.choice(cryptolist)} | [b]{foundSum}$[/b] |" \
                                                   f" Withdrawn Automatically[/color]\n"

                        totalSum = float(totallabel_.text.split(":")[1].replace("$[/b][/color]", "").replace("[b]", ""))
                        totallabel_.text = f"[color=1AD800]Total:\n[b]{round(totalSum + foundSum, 2)}$[/b][/color]"

                    else:
                        foundlabel_.text += f"[color=1AD800]{random.choice(cryptolist)} | [b]{round(foundSum, 2)}$[/b] |" \
                                            f" Withdrawn Automatically[/color]\n"

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
                totalSumText = autoWithdrawMenuClassXmpl.children[0]

                cl = ClockClass(lambda a: addShitToList(label_=operationalText,
                                                        foundlabel_=foundText,
                                                        stopped=self.stopped,
                                                        successX=self.everyXareSucess,
                                                        cryptolist=chosenCoins,
                                                        totallabel_=totalSumText),
                                timeout=0.05)
            else:
                popup = Popup(title='Binance ID not found',
                              content=Label(text='Enter your wallet \nor Binance ID', font_size='17sp'),
                              size_hint=(.4, .3))
                popup.open()
        else:
            popup = Popup(title='Choose any currency',
                          content=Label(text='Choose at least\n1 currency (checkbox)', font_size='17sp'),
                          size_hint=(.4, .3))
            popup.open()

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
        self.title = "checker by mrGoodGood"
        Window.clearcolor = (.4, .4, .4, 1)
        bl = BoxLayout(orientation='vertical')
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


if __name__ == '__main__':
    AndroidApp().run()
