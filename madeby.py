from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard



presentation = Builder.load_file('kv/madeby.kv')

class MadeByCard(MDCard): 
	# print('MadeByCard 0')
	
	def __init__(self, **kwargs):
		super(MadeByCard, self).__init__(**kwargs)


