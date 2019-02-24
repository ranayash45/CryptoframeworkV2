import hashlib
import hmac
from kivy.app import App
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.selectableview import SelectableView

from ApiCalls.Model import Candidate, Voter
from CryptoFramework.ShortPailler import PaillerCryptoSystem

P = PaillerCryptoSystem()


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
    selectedid = -1
    btngivevote = ObjectProperty()
    def args_converter(self,index,data_item):
        print(data_item)
        return {'candidate':(data_item[0],data_item[1],data_item[2]),
                'is_selected':False
                }

    def __init__(self,**kwargs):
        super(AddVote, self).__init__(**kwargs)
        self.L = LoadingScreen()

    def Show_Dashboard(self):
        self.clear_widgets()
        self.add_widget(Dashboard())

    def SuccessAuthentication(self,response,result: dict):
        if 'error' in result:
            self.L.Image.source = "./Images/error.gif"
            return

        Data = result
        if Data != None:
            self.description_output.text = Data[2]
            self.btnaddvote.disabled = False
        else:
            self.description_output.text = "User Not Found"
            self.candidatelist.adapter.data.clear()
            self.candidatelist.adapter.data.extend([])
            self.candidatelist._trigger_reset_populate()
            self.btnaddvote.disabled = True
        self.L.dismiss()
    def FailAuthentication(self):
        self.L.dismiss()
    def CheckAuthentication(self):
        V = Voter.Voter()
        V.CheckAuthentication(self.adhar_no.text,None,success=self.SuccessAuthentication,fail=self.FailAuthentication)
        self.L.Image.source = "./Images/loading.gif"
        self.L.open()

    def onsuccess(self,request,result):
        data = result['candidates']
        self.data = data
        self.candidatelist.adapter.data.clear()
        self.candidatelist.adapter.data.extend(data)
        self.candidatelist.adapter.bind(on_selection_change=self.PartyChange)
        self.candidatelist._trigger_reset_populate()
        self.L.Image.anim_loop = 1
        self.L.Image.source = "./Images/success.gif"


    def failing(self,request,result):
        self.L.Image.anim_delay = 0.25;
        self.L.Image.source = "./Images/error2.gif"

    def ShowCandidates(self):
        C = Candidate.Candidate()
        C.GetList(self.onsuccess,self.failing)
        self.L.Image.source = "./Images/loading.gif"
        self.L.open()
    def PartyChange(self,sender):
        if len(sender.selection) > 0:
            self.selectedid = sender.selection[0].value
            self.btngivevote.disabled = False
        else:
            self.selectedid = -1
            self.btngivevote.disabled = True

    def VoteSuccess(self,request,result):

        self.L.dismiss()
    def VoteFail(self,request,result):
        self.L.dismiss()

    def GiveVote(self):
        item_id = bytes(str(self.data[self.selectedid][0]),'utf-8')
        item_password = bytes(str(5675),'utf-8')
        print(item_id)
        my_hmac = hmac.new(item_id,item_password,hashlib.md5)
        my_digest = str(my_hmac.digest())
        V = Voter.Voter()
        self.L.Image.source = "./Images/loading2.gif"
        self.L.open()
        my_hmac = str(my_hmac)
        my_digest = str(my_digest)
        tmp_item_id = self.data[self.selectedid]
        V.GiveVote(item_id,my_hmac,my_digest,self.VoteSuccess,self.VoteFail)


class LoadingScreen(ModalView):
    def __init__(self,**kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.Image = Image()
        self.Image.anim_delay = 0.05

        self.add_widget(self.Image)

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

