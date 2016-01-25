from django.shortcuts import render
import urllib2
from django.shortcuts import HttpResponse
from stocklist.models import StockList
# Create your views here.
def exchange_list (request):
    file_upload = urllib2.urlopen("http://www.nasdaq.com/screening/companies-by-industry.aspx?&render=download").read()
    file=file_upload.split('\n')
    print file[0]
    print file[1]
    for  note in file:
        try:
            stock=note.split(',')
            symbol=stock[0].strip('"')
            name = stock[1].strip('"')
            last_sale = float(stock[2].strip('"'))
            market_cap = float(stock[3].strip('"'))
            ipo = int(stock[5].strip('"'))
            sector = stock[6].strip('"')
            industry = stock[7].strip('"')
            summary_quote = stock[8].strip('"')
            StockList.objects.create(symbol=symbol,name=name,last_sale=last_sale,market_cap=market_cap,ipo=ipo,sector=sector,industry=industry,summary_quote=summary_quote)
        except:
            pass
    return HttpResponse(file[1])