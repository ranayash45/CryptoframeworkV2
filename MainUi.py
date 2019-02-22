
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.listview import ListItemButton
from kivy.uix.selectableview import SelectableView

from CryptoUi.CryptoFramework.Authentication import Authentication


class Dashboard(BoxLayout):
    def Show_Add_Vote(self):
        self.clear_widgets()
        self.add_widget(AddVote())

class CryptoApp(App):
    pass



class AddVote(BoxLayout):
    adhar_no = ObjectProperty()
    description_output = ObjectProperty()
    btnaddvote = ObjectProperty()
    candidatelist = ObjectProperty()

    def args_converter(self,index,data_item):
        print(data_item)
        return {'candidate':(data_item[0],data_item[1],data_item[2]),
                'is_selected':False
                }

    def Show_Dashboard(self):
        self.clear_widgets()
        self.add_widget(Dashboard())

    def CheckAuthentication(self):
        A = Authentication()
        Data =  A.CheckUser(self.adhar_no.text,None)

        if Data != None:
            self.description_output.text = Data[2]
            self.btnaddvote.disabled = False
        else:
            self.description_output.text = "User Not Found"
            self.btnaddvote.disabled = True

    def ShowCandidates(self):
        data = [["1","Narendra Modi","Bhajap"],["2","Rahul Gandhi","CONGRESS"],["3","Arvind Kejriwal","AAP"]]
        self.candidatelist.adapter.data.clear()
        self.candidatelist.adapter.data.extend(data)
        self.candidatelist._trigger_reset_populate()
        self.candidatelist.bind(on_selection_change=self.PartyChange)

    def PartyChange(self):
        print("Changed")


class CandidateOption(SelectableView,BoxLayout):
    candidate = ListProperty()
    vote = -1

    def __init__(self,**kwargs):
        super(CandidateOption, self).__init__(**kwargs)

        self.deselected_color=[1,1,0,1]
        self.selected_color=[0,1,1,1]




if __name__ == "__main__":
    P = CryptoApp()
    P.run()

