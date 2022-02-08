import os,time, tkinter,logging

class Attendance_alarm:

    def __init__(self):
        self.log_init()
        if 'y' in open('stats','r').readlines():
            self.gui()
            logging.info('Attendance_alarm close')
        else:
            self.alarm()

    def log_init(self):
        logging.basicConfig(filename='Error.log',level=logging.INFO,format='%(asctime)s :: %(levelname)s :: %(message)s')

    def alarm(self):
        def pop_up():

            def close():
                root.destroy()

            root = tkinter.Tk()
            root.title('!!! Pls take attendance on MS Teams !!!')
            label = tkinter.Label(root, text='!!! Pls take attendance on MS Teams !!!')
            label.pack()
            button = tkinter.Button(root, text='OK', command=close)
            button.pack()
            root.mainloop()

        trigger_time = [
            {'time':'1','checked':False},
            {'time':'3','checked':False},
            {'time':'5','checked':False},
            {'time':'7','checked':False},
            {'time':'9','checked':False},
            {'time':'11','checked':False},
            {'time':'13','checked':False},
            {'time':'15','checked':False},
            {'time':'17','checked':False},
            {'time':'19','checked':False},
            {'time':'21','checked':False},
            {'time':'23','checked':False}]

        while True:
            now_time = time.strftime('%H')
            for i in trigger_time:
                if now_time == i['time']:
                    if i['checked']==False:
                        i['checked']=True
                        pop_up()

    def gui(self):
        def kill():
            os.system('taskkill /fi "imagename eq alarm.exe"')
        root = tkinter.Tk()

        label = tkinter.Label(text='Close the bot?')
        button_n = tkinter.Button(text='No', command=root.destroy)
        button_y = tkinter.Button(text='Yes', command=kill)

        label.pack(side=tkinter.TOP)
        button_n.pack(side=tkinter.LEFT)
        button_y.pack(side=tkinter.RIGHT)

        root.mainloop()

Attendance_alarm()