import PySimpleGUI as sg
import random
import datetime
import time
import socket
from playsound import playsound

HOST = '192.168.0.21'
PORT = 9090
colors = ['DarkBlack', 'DarkPurple1', 'DarkBlue13', 'DarkGrey12', 'DarkGrey9', 'LightBlue7']
sg.ChangeLookAndFeel(random.choice(colors))
CurrentTime = time.strftime("%H:%M")

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = datetime.datetime.today().weekday()

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('MEDICINE REMINDER', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Enter your alarm time in 24 hour format: ')],
    [sg.InputText('', size=(10, 1), tooltip='Use these to enter your alarm time')],
    [sg.Frame(layout=[
    [sg.Checkbox('Sun', default=True),  sg.Checkbox('Mon', default=True)],
    [sg.Checkbox('Tue', default=True), sg.Checkbox('Wed', default=True)],
    [sg.Checkbox('Thu', default=True), sg.Checkbox('Fri', default=True)],
    [sg.Checkbox('Sat', size=(10, 1))]
    ], title='Days', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set days')],
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
]


window = sg.Window('Medicine Reminder', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.read()
window.close()

# event 1: saat, 2: Sun, 3: Mon, 4: Tue, 5: Wed, 6: Thu, 7: Fri, 8: Sat
if values[1] == '':
    sg.popup('Enter an alarm')
    exit("Enter an alarm")

else:
    sg.popup('Your alarm will be rang at: ', str(values[1]), 'You can close this page.')

AlarmTime = values[1]

num_of_pills = 0
for i in range(9):
    if values[i] is True:
        num_of_pills += 1


def pill_time(client_socket):
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    data = 'Pill time'
    # Send data to server
    client_socket.send(data.encode())
    client_socket.close()


while values[2] or values[3] or values[4] or values[5] or values[6] or values[7] or values[8]:
    if values[2] is True and weekDays[today] == 'Sunday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[2] = False

    if values[3] is True and weekDays[today] == 'Monday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[3] = False

    if values[4] is True and weekDays[today] == 'Tuesday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[4] = False

    if values[5] is True and weekDays[today] == 'Wednesday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[5] = False

    if values[6] is True and weekDays[today] == 'Thursday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[6] = False

    if values[7] is True and weekDays[today] == 'Friday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[7] = False

    if values[8] is True and weekDays[today] == 'Saturday':
        # Check alarm
        while AlarmTime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")
            time.sleep(1)
        if AlarmTime == CurrentTime:
            num_of_pills -= 1
            playsound('C:/Users/Fellandes/Desktop/Alert.wav')
            sg.popup("Pill Time!")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pill_time(client_socket)
            sg.popup("Remaining Pills: ", str(num_of_pills))
            values[8] = False
