import xlwings as xl
import time
import requests as rq
import json
from pycoingecko import CoinGeckoAPI
from PyQt5.QtWidgets import QMessageBox

def main():

    try:
        filename = 'Producción y Contador.xlsx'
        file = xl.Book(filename)
        sheets = file.sheets

        api = CoinGeckoAPI()


        while True:
            dolar = json.loads(rq.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')._content)
            eth = api.get_price(ids='ethereum', vs_currencies='usd')
            slp = api.get_price(ids='smooth-love-potion', vs_currencies='usd')

            eth_price = eth.get('ethereum').get('usd')
            slp_price = slp.get('smooth-love-potion').get('usd')
            dolarblue_price = ''

            # Extraigo el valor del dólar blue del JSON retornado
            for i in dolar:
                if i.get('casa').get('nombre') == 'Dolar Blue':
                    dolarblue_price = i.get('casa').get('venta')
                    break

            dolarblue_price = dolarblue_price.replace(",",".")
            
            # Loopeo por todas las sheets buscando valores
            for sheet in sheets:
                #SLP
                cell = sheet.api.UsedRange.Find('SLP PRECIO')
                if cell != None:
                    address = address_fixer(cell)
                    sheet.range(address).value = slp_price
                
                #ETH
                cell = sheet.api.UsedRange.Find('ETH PRECIO')
                if cell != None:
                    address = address_fixer(cell)
                    sheet.range(address).value = eth_price

                #BLUE
                cell = sheet.api.UsedRange.Find('BLUE')
                if cell != None:
                    address = address_fixer(cell)
                    sheet.range(address).value = dolarblue_price

            # Espero un minuto antes de volver a cargar los datos
            time.sleep(30)
    except BaseException as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(e))
        msg.setWindowTitle("Error")
        msg.exec_()

def address_fixer(cell):
    address = str(cell.Address)
    address = address.split('$')
    address[1] = chr(ord(address[1]) + 1)    # Sumo 1 a la celda encontrada para insertar el valor a la derecha
    address = ''.join(address)
        
    return address