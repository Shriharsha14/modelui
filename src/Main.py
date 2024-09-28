import wx
import serial

class SerialConnectionApp(wx.Frame):
    def __init__(self, parent, title):
        super(SerialConnectionApp, self).__init__(parent, title=title, size=(400, 200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Label and input for COM port
        self.port_label = wx.StaticText(panel, label="COM Port:")
        vbox.Add(self.port_label, flag=wx.LEFT | wx.TOP, border=10)

        self.port_input = wx.TextCtrl(panel, value="COM21")
        vbox.Add(self.port_input, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Button to connect to COM port
        self.connect_button = wx.Button(panel, label="Connect")
        vbox.Add(self.connect_button, flag=wx.LEFT | wx.TOP, border=10)
        self.connect_button.Bind(wx.EVT_BUTTON, self.on_connect)

        # Status label
        self.status_label = wx.StaticText(panel, label="Status: Not connected")
        vbox.Add(self.status_label, flag=wx.LEFT | wx.TOP, border=10)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def on_connect(self, event):
        port_name = self.port_input.GetValue()
        self.connect_com_port(port_name)

    def connect_com_port(self, port_name="COM21", baud_rate=9600, timeout=1):
        try:
            ser = serial.Serial(port_name, baud_rate, timeout=timeout)
            if ser.is_open:
                self.status_label.SetLabel(f"Status: Connected successfully to {port_name}")
                ser.close()
            else:
                self.status_label.SetLabel(f"Status: Failed to connect to {port_name}")
        except serial.SerialException as e:
            self.status_label.SetLabel(f"Error: {e}")

if __name__ == "__main__":
    app = wx.App()
    SerialConnectionApp(None, title="Serial Connection")
    app.MainLoop()
