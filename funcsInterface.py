from cambioDOLEUR import Scrapping_Moedas
from openpyxl.utils import exceptions
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import openpyxl



class Funcoes():

    def func_bttn(self):

        self.instanc = Scrapping_Moedas()
        self.listacotacoes = self.instanc.buscar(self.dt_init(), self.dt_final())

        for i in self.listarec.get_children():
            self.listarec.delete(i)

        for (data, cotdol, coteur) in self.listacotacoes:
            self.listarec.insert('', 'end', values =(data, cotdol, coteur))

    def add_excel(self):

        try:
            wb = openpyxl.load_workbook(self.entrycaminho.get())
            ws = wb['2022']
            ws = wb.active

            for i in self.listacotacoes:
                ws.append(i)

            wb.save(self.entrycaminho.get())
            tkinter.messagebox.showinfo('ATENÇÃO', 'Cotações adicionadas com sucesso!!!')

        except exceptions.InvalidFileException:
            tkinter.messagebox.showerror('ERROR', 'Local do arquivo não selecionado ou inexistente')

        except FileNotFoundError:
            tkinter.messagebox.showerror('ERROR', 'Local do arquivo não selecionado ou inexistente')

        except PermissionError:
            tkinter.messagebox.showerror('ERROR', 'Por favor feche o arquivo para salvar as cotações')

    def warnadd(self):
        self.perg = tkinter.messagebox.askyesno('Confirmação', 'Deseja adicionar os itens da tela na planilha?', icon ='question')

        try:
            if self.perg == False:
                tkinter.messagebox.showinfo('ATENÇÃO', 'Operação cancelada!!')
            else:
                self.add_excel()
        except AttributeError:
            tkinter.messagebox.showerror('ERROR', 'Por favor pesquise e confira as cotações antes de adicionar no Excel')

    def verificacaodata(self):
        if self.entryDtFin.get() == '':
            tkinter.messagebox.showerror('ERROR', 'Por favor selecione a data inicial/final')
        elif self.entryDtInit.get() == '':
            tkinter.messagebox.showerror('ERROR', 'Por favor selecione a data inicial/final')
        else:
            self.func_bttn()

    def verifyerror(self):
        try:
            self.verificacaodata()
        except IndexError:
            tkinter.messagebox.showerror('ERROR', 'Datas selecionadas muito distante')

    def trocarcaminho(self):
        self.file = tkinter.filedialog.askopenfilename()

        if not self.file:
            self.entrycaminho.delete(0, END)
            self.entrycaminho.insert(0, r'F:\Contabilidade\Sales Controling\2022\Taxas de Cambio.xlsx')
        else:
            self.entrycaminho.delete(0, END)
            self.entrycaminho.insert(0, self.file)

    def func_calon(self):
        self.entryDtInit.delete(0, END)
        self.entryDtInit.insert(END, self.dt_init())

    def func_calof(self):
        self.entryDtFin.delete(0, END)
        self.entryDtFin.insert(END, self.dt_final())

    def dt_init(self):
        return self.calendario1.get_date()

    def dt_final(self):
        return self.calendario2.get_date()


if __name__ == '__main__':
    a = Funcoes()
    a.verify_excel()