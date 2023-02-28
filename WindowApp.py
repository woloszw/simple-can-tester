import wx


class WindowApp(wx.Frame):

    def __init__(self, parent, title):
        super(WindowApp, self).__init__(parent, title=title, size=(800, 800))

        self.st2 = None
        self.st1 = None
        self.col = None
        self.cpnl = None
        self.InitUI()
        self.Centre()

    def InitUI(self):
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
        self.st1 = wx.StaticText(pnl, label="Connected", style=wx.ALIGN_LEFT)
        self.st2 = wx.StaticText(pnl, label="Not connected", style=wx.ALIGN_LEFT)

        self.col = wx.Colour(0, 0, 0)

        connect_button = wx.ToggleButton(pnl, label='Connect', pos=(20, 25))
        self.cpnl = wx.Panel(pnl, pos=(150, 20), size=(110, 110))
        self.cpnl.SetBackgroundColour(self.col)

        self.st1.SetFont(font)
        self.st2.SetFont(font)

        vbox.Add(self.st1, flag=wx.ALL, border=15)

        pnl.SetSizer(vbox)

        connect_button.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_connect)

        self.SetTitle('Toggle buttons')
        self.Centre()

    def toggle_connect(self, e):

        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            self.st2.Hide()
            self.st1.Show()
        else:
            self.st2.Show()
            self.st1.Hide()

        self.cpnl.SetBackgroundColour(self.col)
        self.cpnl.Refresh()


