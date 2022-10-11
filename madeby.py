from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout



presentation = Builder.load_file('kv/madeby.kv')

class MadeByBox(MDCard): 
	
	def __init__(self, **kwargs):
		super(MadeByBox, self).__init__(**kwargs)
		# print('MadeByCard 0')


