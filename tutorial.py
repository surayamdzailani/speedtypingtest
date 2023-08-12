import tkinter as tk
import random
import time
from essential_generators import DocumentGenerator
from PIL import Image, ImageTk
import threading
#we create gui inside oop 

class Typing_Speed_GUI:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('TSA:Typing Speed Application')
		self.window.geometry("1500x900")
		self.img = Image.open('pic.jpg')
		self.bg =  ImageTk.PhotoImage(self.img)
		self.resize = self.window.resizable(False,False)

		self.word = open('texts.txt', 'r').read().split('\n')


		#label for bg tkinter
		self.bgs =  tk.Label(self.window, image=self.bg)
		self.bgs.place(x=0, y=0)

		#label for interface title
		self.title_font = ("Ink Free", 20, "bold")
		self.title_lable = tk.Label(self.window, text='Yunsz Keyboard Warriors Testing', foreground='white',bg='#FFBF00', font= self.title_font)
		self.title_lable.grid(row=0, column=0, columnspan=2, padx=225, pady=45)

		#label for random words 
		self.sentence_lable = tk.Label(self.window, text= random.choice(self.word), foreground='white', bg='#E49B0F', font=("Times", 15, 'bold'), borderwidth=1, relief='solid',height=5, width=100)
		self.sentence_lable.grid(row=1, column=0, columnspan=2, padx=225, pady=50)

		#entry for typing sentences
		self.typing_box = tk.Entry(self.window, width=40, font=('Times',16,'bold'), bg='black', fg='white')
		self.typing_box.grid(row=2, column=0, columnspan=2, padx=225, pady=50)
		self.typing_box.insert(0,'Please Typing Above Sentence Here....')
		self.typing_box.bind('<FocusIn>', self.temp_text)
		self.typing_box.bind('<KeyPress>', self.start, self.update_timer)

		#label for speed performance
		self.speed = tk.Label(self.window, text='Speed: \n0.00 WPM', font=('Times', 13, 'bold'),fg='black',bg='#DFFF00', width= 15)
		self.speed.grid(row=3, column=0, columnspan = 2, padx=5, pady=10)

		#Label for Timer 
		self.timer = tk.Label(self.window, text='Timer: \n00:00 (min/sec)',  font=('Times', 13, 'bold'),fg='black',bg='#DFFF00', width=15)
		self.timer.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

		#reset button
		self.reset = tk.Button(self.window, text='Reset', bd=3, fg='black', bg='#FBCEB1', font=('Times', 13, 'bold'), command = self.reset)
		self.reset.grid(row=6, column=0, columnspan=2, padx=5, pady=10)


		self.counter= 0
		self.running = False
		self.second = 0 
		self.minute = 0 




		self.window.mainloop()

	def temp_text(self,e):
		self.typing_box.delete(0,'end')

	def start(self,event):
		if not self.running:
			if not event.keycode in [16, 17, 18]:
				self.running = True
				t = threading.Thread(target=self.time_thread)
				t.start()
				self.start_time = time.time()
				self.update_timer(self.start_time)
	
		if not self.sentence_lable.cget('text').startswith(self.typing_box.get()):
			self.typing_box.config(fg='red')
		else:
			self.typing_box.config(fg='green')

		if self.typing_box.get() == self.sentence_lable.cget('text')[:-1]:
			self.running =  False
			self.typing_box.config(fg='green')
			

	def reset(self):
		self.running = False
		self.second =  0
		self.minute = 0
		self.counter = 0 
		self.sentence_lable.config(text= random.choice(self.word))
		self.typing_box.delete(0, tk.END)
		self.speed.config(text='Speed: \n0.00 WPM')
		self.timer.config(text='Timer: \n00:00 (min/sec)')

	def time_thread(self):
		while self.running:
			time.sleep(0.1)
			self.counter += 0.1
			cps = len(self.typing_box.get()) / self.counter
			wpm = cps * 60
			self.speed.config(text=f'Speed: \n{wpm:.2f} WPM')

	def update_timer(self, s_time):
		if self.running== True:
			current_time = time.time()

			if(int(current_time -  s_time) >= 0):
				self.second += 1 
			if self.second == 60:
				self.second = 0
				self.minute += 1

			min_p = '{:0>2d}'.format(int(self.minute))
			sec_p = '{:0>2d}'.format(int(self.second))

			self.timer.config(text=f'Timer: \n{min_p}:{sec_p}')
			self.timer.after(1000, lambda:self.update_timer(s_time))

		else:
			self.end_time = time.time()


		
Typing_Speed_GUI()
