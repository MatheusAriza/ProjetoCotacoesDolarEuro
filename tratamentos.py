
class Tratamentos_Moedas():

    def tratamento_geral(self, lista_dol, lista_eur):
        itensprontos = []
        dataevalortratados = []
        index = 0

        for item in lista_dol:
            dataevalortratados.append(self.tratamento_data(lista_dol, index))
            dataevalortratados.append(self.tratamento_valor(lista_dol, index))
            dataevalortratados.append(self.tratamento_euro(lista_eur, index))
            itensprontos.append(dataevalortratados[:])
            dataevalortratados.clear()
            index += 1
        return itensprontos

    def tratamento_euro(self, lista_recebida, index):
        tend = []
        for i in lista_recebida:
            if i['tipoBoletim'] == 'Fechamento':
                tend.append(i)
        for x in tend:
            facto = tend[index]['cotacaoCompra']
        return facto

    def tratamento_data(self, lista_recebida, index):
        tratamentodata = f'{lista_recebida[index]["dataHoraCotacao"][8:10]}/{lista_recebida[index]["dataHoraCotacao"][5:7]}/{lista_recebida[index]["dataHoraCotacao"][:4]}'
        return tratamentodata

    def tratamento_valor(self, lista_recebida, index):
        valor_tratado = lista_recebida[index]['cotacaoCompra']
        return valor_tratado

if __name__ == '__main__':
    valores = [{'cotacaoCompra': 5.026, 'dataHoraCotacao': '2022-05-02 15:57:38.053'},
               {'cotacaoCompra': 5.0161, 'dataHoraCotacao': '2022-05-03 16:10:11.909'},
               {'cotacaoCompra': 5.0087, 'dataHoraCotacao': '2022-05-04 15:35:11.769'},
               {'cotacaoCompra': 5.0045, 'dataHoraCotacao': '2022-05-05 17:33:19.051'},
               {'cotacaoCompra': 5.0744, 'dataHoraCotacao': '2022-05-06 17:46:43.972'},
               {'cotacaoCompra': 5.1334, 'dataHoraCotacao': '2022-05-09 15:14:40.558'}]

    valores_eur = [{'cotacaoCompra': 5.268, 'dataHoraCotacao': '2022-05-02 10:08:18.219', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.2953, 'dataHoraCotacao': '2022-05-02 11:11:15.626',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2954, 'dataHoraCotacao': '2022-05-02 12:10:15.448',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2903, 'dataHoraCotacao': '2022-05-02 15:57:38.046',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2879, 'dataHoraCotacao': '2022-05-02 15:57:38.053', 'tipoBoletim': 'Fechamento'},
                   {'cotacaoCompra': 5.312, 'dataHoraCotacao': '2022-05-03 10:03:17.017', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.2997, 'dataHoraCotacao': '2022-05-03 11:10:17.341',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2825, 'dataHoraCotacao': '2022-05-03 12:07:15.94',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2684, 'dataHoraCotacao': '2022-05-03 16:10:11.904',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.282, 'dataHoraCotacao': '2022-05-03 16:10:11.909', 'tipoBoletim': 'Fechamento'},
                   {'cotacaoCompra': 5.285, 'dataHoraCotacao': '2022-05-04 10:04:17.227', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.287, 'dataHoraCotacao': '2022-05-04 11:09:15.351',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.288, 'dataHoraCotacao': '2022-05-04 12:06:16.327',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2603, 'dataHoraCotacao': '2022-05-04 15:35:11.762',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2782, 'dataHoraCotacao': '2022-05-04 15:35:11.769', 'tipoBoletim': 'Fechamento'},
                   {'cotacaoCompra': 5.2458, 'dataHoraCotacao': '2022-05-05 10:07:15.869', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.2632, 'dataHoraCotacao': '2022-05-05 11:04:15.947',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2831, 'dataHoraCotacao': '2022-05-05 12:02:16.466',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2995, 'dataHoraCotacao': '2022-05-05 17:33:19.046',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.2572, 'dataHoraCotacao': '2022-05-05 17:33:19.051', 'tipoBoletim': 'Fechamento'},
                   {'cotacaoCompra': 5.3702, 'dataHoraCotacao': '2022-05-06 10:10:15.452', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.3819, 'dataHoraCotacao': '2022-05-06 11:05:16.319',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.3526, 'dataHoraCotacao': '2022-05-06 12:04:15.602',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.3472, 'dataHoraCotacao': '2022-05-06 17:46:43.968',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.3631, 'dataHoraCotacao': '2022-05-06 17:46:43.972', 'tipoBoletim': 'Fechamento'},
                   {'cotacaoCompra': 5.4121, 'dataHoraCotacao': '2022-05-09 10:04:16.616', 'tipoBoletim': 'Abertura'},
                   {'cotacaoCompra': 5.4201, 'dataHoraCotacao': '2022-05-09 11:07:46.961',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.4146, 'dataHoraCotacao': '2022-05-09 12:07:17.189',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.4029, 'dataHoraCotacao': '2022-05-09 15:14:40.552',
                    'tipoBoletim': 'Intermediário'},
                   {'cotacaoCompra': 5.4183, 'dataHoraCotacao': '2022-05-09 15:14:40.558', 'tipoBoletim': 'Fechamento'}]

    aaa = Tratamentos_Moedas()
    print(aaa.tratamento_geral(valores, valores_eur))
