import requests
from bs4 import BeautifulSoup

def make_comparison(df):

    df = df[df['Count'] < df['Count2']]
    name_list = df['Name'].tolist()

    return name_list