from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup



def makechartdef():
    # content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1)
    # content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a
    # content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(4)
    data_list = []

    resp = requests.get('https://movie.naver.com/movie/running/current.nhn')
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')

    for tr in soup.select('#content div.article div.lst_wrap ul li'):
        try:
            title = tr.select('dl dt a')[0].text
            rating = tr.select('.num')[0].text

        except IndexError:
            continue

        ep = {
            'title':title,
            'rating':rating,
        }

        data_list.append(ep)

    return {
        'data_list':data_list,
        'soup': soup

    }




