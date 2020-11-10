from splinter import Browser
from bs4 import BeautifulSoup
import requests

import pymongo
from pprint import pprint

import pandas as pd
import os
import time


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    # listing_results = []

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news = soup.select_one("li.slide")
    results = news.find('div', class_="content_title").text
    results2 = news.find('div', class_="article_teaser_body").text
    # print(results)
    # print(results2)
    time.sleep(2)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_id('full_image')
    browser.click_link_by_partial_text('more info')

    # Use Beatiful Soup
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    a = image_soup.find('figure', class_='lede')
    image2 = a.find('a')['href']
    feauture_image_url = f'https://www.jpl.nasa.gov{image2}'

    # print(feauture_image_url)
    time.sleep(2)

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    html = browser.html

    tables = pd.read_html(facts_url)
    len(tables)
# Double check HERE
    mars_facts = tables[0]

    mars_facts.columns = ['Description', 'Value']
    mars_facts.set_index('Description', inplace=True)

    mars_facts
    time.sleep(2)
###############################

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    html = browser.html
    hemis_soup = BeautifulSoup(html, 'html.parser')

    browser.click_link_by_partial_text("Cerberus")
    html = browser.html
    soup1 = BeautifulSoup(html, 'html.parser')

    hemis1_title = soup1.select_one("div.content h2").text
    # print(hemis1_title)

    hemis1_image = browser.find_by_text("Sample")["href"]
    hemis1 = {"Name": hemis1_title, "img_url": hemis1_image}

    browser.click_link_by_partial_text("Schiaparelli")
    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')

    hemis2_title = soup2.select_one("div.content h2").text
    # print(hemis2_title)

    hemis2_image = browser.find_by_text("Sample")["href"]
    hemis2 = {"Name": hemis2_title, "img_url": hemis2_image}

    browser.click_link_by_partial_text("Syrtis")
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')

    hemis3_title = soup3.select_one("div.content h2").text
    # print(hemis3_title)

    hemis3_image = browser.find_by_text("Sample")["href"]
    hemis3 = {"Name": hemis3_title, "img_url": hemis3_image}

    browser.click_link_by_partial_text("Valles")
    html = browser.html
    soup4 = BeautifulSoup(html, 'html.parser')

    hemis4_title = soup4.select_one("div.content h2").text
    # print(hemis4_title)

    hemis4_image = browser.find_by_text("Sample")["href"]
    hemis4 = {"Name": hemis4_title, "img_url": hemis4_image}

    mars_collections = {"news_title": results,
                        "news_p": results2,
                        "featured_image_url": feauture_image_url,
                        "table": mars_facts,
                        "hemisphere_url": [hemis1, hemis2, hemis3, hemis4]
                        }

    browser.quit()
    return mars_collections
