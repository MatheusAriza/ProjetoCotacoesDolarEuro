from bs4 import BeautifulSoup
from tratamentos import Tratamentos_Moedas
import requests
import json



class Scrapping_Moedas():

    def buscar(self, datainicial, datafinal):
        self.inst = Tratamentos_Moedas()
        self.trata = self.inst.tratamento_geral(self.cotacao_dollar(datainicial, datafinal), self.cotacao_euro(datainicial, datafinal))
        return self.trata

    def tratamento_data(self, diamesano):
        self.data = f'{diamesano[3:5]}-{diamesano[0:2]}-{diamesano[6:]}'
        return self.data

    def cotacao_dollar(self, datainicial, datafinal):
        self.strscp = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{self.tratamento_data(datainicial)}'&@dataFinalCotacao='{self.tratamento_data(datafinal)}'&$top=100&$format=json&$select=cotacaoCompra,dataHoraCotacao"
        self.page = requests.get(self.strscp)
        self.soup = BeautifulSoup(self.page.text, 'lxml').text
        self.cep = json.loads(self.soup)
        return self.cep['value']

    def cotacao_euro(self, datainicial, datafinal):
        self.strscp = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='EUR'&@dataInicial='{self.tratamento_data(datainicial)}'&@dataFinalCotacao='{self.tratamento_data(datafinal)}'&$top=100&$format=json&$select=cotacaoCompra,dataHoraCotacao,tipoBoletim"
        self.page = requests.get(self.strscp)
        self.soup = BeautifulSoup(self.page.text, 'lxml').text
        self.cep = json.loads(self.soup)
        return self.cep['value']


if __name__ == '__main__':

    a = Scrapping_Moedas()
    print(a.buscar('01/04/2022', '09/05/2022'))
