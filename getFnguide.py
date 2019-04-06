# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:05:08 2019

@author: SUHO
"""

def ext_fin_fnguide_data(ticker,gb,item,n,freq="a"):
    """
    :param ticker: 종목코드
    :param gb: 데이터 종류 (0 : 재무제표, 1 : 재무비율, 2: 투자지표)
    :param item: html_text file에서 원하는 계정의 데이터를 가져온다.
    :param n: 최근 몇 개의 데이터를 가져 올것인지
    :param freq: Y : 연간재무, Q : 분기재무    
    :return: item의 과거 데이터
    """
    html_text = get_html_fnguide(ticker, gb)
    soup = bs(html_text, 'lxml')
    d = soup.find_all(text=item)
    if(len(d)==0) :
        return None

    #재무제표면 최근 3년을 가져오고 재무비율이면 최근 4년치를 가져온다.
    nlimit =3 if gb==0 else 4

    if n > nlimit :
        return None
    if freq == 'a':
        #연간 데이터
        d_ = d[0].find_all_next(class_="r",limit=nlimit)
        # 분기 데이터
    elif freq =='q':
        d_ = d[1].find_all_next(class_="r",limit=nlimit)
    else:
        d_ = None

    try :
        data = d_[(nlimit-n):nlimit]
        v = [v.text for v in data]

    except AttributeError as e:
        return None

    return(v)