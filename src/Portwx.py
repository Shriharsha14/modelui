import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        # Create main panel
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Box: Model 3141 (containing Ports, Super Speed, and Orientation)
        model_box = wx.StaticBox(panel, label="Model 3141")
        model_sizer = wx.StaticBoxSizer(model_box, wx.VERTICAL)

        # Sub-box: Ports (Port 1 and Port 2 side by side)
        ports_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Port 1 with On/Off switch
        self.port1_on_off = wx.RadioBox(panel, label="Port 1 On/Off", choices=["On", "Off"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        ports_sizer.Add(self.port1_on_off, flag=wx.ALL, border=5)

        # Port 2 with On/Off switch
        self.port2_on_off = wx.RadioBox(panel, label="Port 2 On/Off", choices=["On", "Off"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        ports_sizer.Add(self.port2_on_off, flag=wx.ALL, border=5)

        # Add Ports sizer to the main Model box sizer
        model_sizer.Add(ports_sizer, flag=wx.ALL | wx.EXPAND, border=10)

        # Super Speed section with Enable/Disable switch
        superspeed_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.superspeed_switch = wx.RadioBox(panel, label="Super Speed", choices=["Enable", "Disable"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        superspeed_sizer.Add(self.superspeed_switch, flag=wx.ALL, border=5)

        model_sizer.Add(superspeed_sizer, flag=wx.ALL | wx.EXPAND, border=10)

        # Orientation section
        # orientation_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # self.orientation_switch = wx.RadioBox(panel, label="Orientation", choices=["Vertical", "Horizontal"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        # orientation_sizer.Add(self.orientation_switch, flag=wx.ALL, border=5)

        # model_sizer.Add(orientation_sizer, flag=wx.ALL | wx.EXPAND, border=10)

        # Set model_sizer as the main sizer
        main_sizer.Add(model_sizer, flag=wx.ALL | wx.EXPAND, border=10)

        # Set the panel's sizer and layout
        panel.SetSizer(main_sizer)
        self.SetSize((400, 400))
        self.SetTitle('Port & Speed Controller - Model 3141')
        self.Centre()

# Create wx App
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None)
        frame.Show(True)
        return True

# Run the application
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
