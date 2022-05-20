from funcsInterface import Funcoes
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk



root = Tk()

class Tela(Funcoes):

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_datas()
        self.frame_resposta()
        self.lista_frame()
        self.calendario_init()
        self.calendario_final()
        self.bttn_pesquisar()
        self.bttn_addexcel()
        self.caminhosave_excel()
        self.bttn_caminhofile()
        root.mainloop()

    def tela(self):
        self.root.title('Câmbio')
        self.root.configure(background='#4E6070')
        self.root.geometry('850x930')
        self.root.minsize(width=850, height=930)

    def frame_resposta(self):
        self.frame1 = Label(root, text='', font=('verdana', 10, 'bold'), justify=LEFT, anchor=NW)
        self.frame1.place(relx=0.5, rely=0.17, relwidth=0.45, relheight=0.8)

    def frame_datas(self):
        self.TxtDtInicial = Label(self.root, text = 'Data Inicial', bg ='#4E6070', font=('verdana', 13, 'bold'))
        self.TxtDtInicial.place(relx = 0.099, rely = 0.055, relwidth=0.3, relheight=0.05)
        self.TxtDtFinal = Label(self.root, text = 'Data Final', bg ='#4E6070', font=('verdana', 13, 'bold'))
        self.TxtDtFinal.place(relx = 0.099, rely = 0.46, relwidth=0.3, relheight=0.05)

        self.entryDtInit = Entry(self.root, width = 10)
        self.entryDtInit.place (relx = 0.099, rely = 0.12, relwidth=0.3, relheight=0.05)
        self.entryDtFin = Entry(self.root, width = 10)
        self.entryDtFin.place(relx=0.099, rely=0.52, relwidth=0.3, relheight=0.05)

    def calendario_init(self):
        self.calendario1 = Calendar(self.root, fg = 'gray75', bg = 'blue', font= ('verdana', '7', 'bold'), locale= 'pt_br' )
        self.calendario1.place(relx = 0.121, rely = 0.187, relwidth=0.255, relheight=0.19)

        self.sertData1 = Button(self.root, text = 'Confirmar Data Inicial', bd=3, font=('verdana', 8, 'bold'), command = self.func_calon)
        self.sertData1.place (relx = 0.099, rely = 0.39, relwidth=0.3, relheight=0.05)

    def calendario_final(self):
        self.calendario2 = Calendar(self.root, fg = 'gray75', bg = 'blue', font= ('verdana', '7', 'bold'), locale= 'pt_br' )
        self.calendario2.place(relx = 0.121, rely = 0.58, relwidth=0.255, relheight=0.19)

        self.sertData2 = Button(self.root, text='Confirmar Data Final', bd=3, font=('verdana', 8, 'bold'), command = self.func_calof)
        self.sertData2.place(relx=0.099, rely=0.78, relwidth=0.3, relheight=0.05)

    def lista_frame(self):
        self.listarec = ttk.Treeview(self.frame1, height = 9, column = ('col1', 'col2', 'col3'))
        self.listarec.heading('#0', text = '')
        self.listarec.heading('#1', text='Data')
        self.listarec.heading('#2', text='Dolar')
        self.listarec.heading('#3', text='Euro')

        self.listarec.column('#0', width=1)
        self.listarec.column('#1', width=100)
        self.listarec.column('#2', width=90)
        self.listarec.column('#3', width=90)

        self.listarec.place(relx=0.01, rely=0.01, relwidth=0.949, relheight=0.98)

        self.scroollist = Scrollbar(self.frame1, orient = 'vertical')
        self.listarec.configure(yscroll = self.scroollist.set)
        self.scroollist.place(relx = 0.96, rely = 0.01, relwidth = 0.04, relheight = 0.98)

    def bttn_pesquisar(self):
        self.btt_pesquisar = Button(self.root, text='Pesquisar', bd=3, font=('verdana', 8, 'bold'), command=self.verifyerror)
        self.btt_pesquisar.place(relx=0.099, rely=0.85, relwidth=0.301, relheight=0.0496)

    def bttn_addexcel(self):
        self.btt_pesquisar = Button(self.root, text='Colar dados no EXCEL', bd=3, font=('verdana', 8, 'bold'), command=self.warnadd)
        self.btt_pesquisar.place(relx=0.099, rely=0.92, relwidth=0.301, relheight=0.0493)

    def caminhosave_excel(self, caminho = r'F:\Contabilidade\Sales Controling\2022\Taxas de Cambio.xlsx'):
        self.lbcaminho = Label(self.root, text= 'Caminho arquivo Excel:', bg ='#4E6070', font=('verdana', 15))
        self.lbcaminho.place(relx = 0.49, rely = 0.055, relwidth=0.3, relheight=0.05)

        self.entrycaminho = Entry(self.root, width=100)
        self.entrycaminho.insert(0, caminho)
        self.entrycaminho.place(relx = 0.50, rely = 0.11, relwidth=0.362, relheight=0.03)

    def bttn_caminhofile(self):
        self.bttprocarquivo = Button(self.root, text='Procurar', command = self.trocarcaminho)
        self.bttprocarquivo.place(relx = 0.87, rely = 0.11, relwidth=0.08, relheight=0.03)

if __name__ == '__main__':

    Tela()