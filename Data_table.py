from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp



class My_Task(MDApp):
	def build(self):
		layout_1 = Screen()
		
		lable = MDLabel(
			#size_hint = (None, None)
			text = "My Task",
			color = (0,0,0)
			
			)

		table = MDDataTable(
			#pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			#size_hint =(0.9, 0.6),
			#check = True,
			column_data = [
				("ID", dp(60)),
				("Title of Task", dp(100)),
				("Effort", dp(60)),
				("Deadline", dp(60))
			],
			row_data = [
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
			]

			)

		layout_1.add_widget(lable)
		layout_1.add_widget(table)
		return layout_1
		
class My_Assigned_Task(MDApp):
	def build(self):
		layout_2 = Screen()
				
		lable = MDLabel(
				text = "My Assigned Task",
				color = (0,0,0)
			
			)

		table = MDDataTable(
			#pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			#size_hint =(0.9, 0.6),
			#check = True,
			column_data = [
				("ID", dp(60)),
				("Title of Task", dp(100)),
				("Effort", dp(60)),
				("Deadline", dp(60))
			],
			row_data = [
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
				("", "", "", ""),
			]

			)

		layout_2.add_widget(lable)
		layout_2.add_widget(table)
		return layout_2

		# Bind the table
		#table.bind(on_check_press=self.checked)
		#table.bind(on_row_press=self.row_checked)





sm = ScreenManager()
sm.screen_widget(My_Task)
sm.screen_widget(My_Assigned_Task)
			
						#return ScreenManager


#self.theme_cls.theme_style = "Light"
#self.theme_cls.primary_palette = "BlueGray"
		#return Builder.load_file('table.kv')
		

	
	# Function for check presses
	#def checked(self, instance_table, current_row):
		#print(instance_table, current_row)
	# Function for row presses
	#def row_checked(self, instance_table, instance_row):
		#print(instance_table, instance_row)


if __name__ == "__main__":
    sm().run()