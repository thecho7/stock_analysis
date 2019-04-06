import pandas as pd
import os
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    # OPEN datafile
    file_name =  './data/stocklist.xlsx'
    df = pd.read_excel(io=file_name, dtype={'a': str, 'b': str}, index_col=0)
    
    company_info = dict()
    for i in range(len(df.iloc[:,0])):
        company_info[df.iloc[i, 1]] = str('{:06d}'.format(df.iloc[i, 0]))
    
    
    
    
    
    
    
def get_html_fnguide(ticker, gb):
    """    
    :param ticker: 종목코드 
    :param gb: 데이터 종류 (0 : 재무제표, 1 : 재무비율, 2: 투자지표, 3:컨센서스 )
    :return: 
    """
    url=[]

    url.append("https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701")
    url.append("https://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A" + ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701")
    url.append("https://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A"+ ticker + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701")
    url.append("https://comp.fnguide.com/SVO2/ASP/SVD_Consensus.asp?pGB=1&gicode=A" + ticker +"&cID=&MenuYn=Y&ReportGB=&NewMenuID=108&stkGb=701")

    if gb>3 :
        return None

    url = url[gb]
    try:

        req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        html_text = urlopen(req).read()

    except AttributeError as e :
        return None

    return html_text


if __name__ == "__main__":
    main()
else:
    print("This program should be executed with %s\n", "stock_analyis.py")
    raise RuntimeError 
    
    