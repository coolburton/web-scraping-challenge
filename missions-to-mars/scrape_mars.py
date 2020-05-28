from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

def init_browser():
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser


collection_data = {}

def mars_news():
    browser = init_browser()

    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    news_soup = bs(html, 'html.parser')

    news_title = news_soup.find_all('div', class_='content_title')[1].a.text
    # print(news_title)
    collection_data['Mars news title'] = news_title

    news_paragraph = news_soup.find_all('div', class_='article_teaser_body')[0].text
    # print(news_paragraph)
    collection_data['Mars news paragraph'] = news_paragraph
    
    browser.quit

    return collection_data


def mars_image():
    browser = init_browser()

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    html = browser.html
    image_soup = bs(html, 'html.parser')

    image_link = image_soup.find_all('a', class_="fancybox")[1].find_all('img')[1]
    # image_link

    part_image_link = image_link['src']
    # part_image_link

    featured_image_url = 'https://www.jpl.nasa.gov' + part_image_link
    # featured_image_url

    collection_data['Mars image url'] = featured_image_url

    browser.quit

    return collection_data


def mars_weather():
    browser = init_browser()

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html = browser.html
    weather_soup = bs(html, 'html.parser')

    mars_weather = 'InSight sol 532 (2020-05-26) low -93.1ºC (-135.7ºF) high -1.1ºC (30.0ºF) winds from the SW at 4.9 m/s (10.9 mph) gusting to 17.7 m/s (39.6 mph) pressure at 7.10 hPa'
    # print(mars_weather)

    collection_data['Mars weather'] = mars_weather

    browser.quit

    return collection_data


def mars_fact():
    browser = init_browser()

    fact_url = 'https://space-facts.com/mars/'
    fact_table = pd.read_html(fact_url)

    fact_df = fact_table[0]
    fact_df.columns = ['Mars Facts', 'Values']
    # fact_df

    html_table = fact_df.to_html(index=False)
    html_fact_table = html_table.replace('\n', '')
    # html_fact_table

    collection_data['Mars fact'] = html_fact_table

    browser.quit

    return collection_data

def mars_hem():
    browser = init_browser()

    usgs_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    home_url="https://astrogeology.usgs.gov"

    browser.visit(usgs_url)
    html = browser.html
    usgs_soup = bs(html, 'html.parser')
    image_url = usgs_soup.find_all('div', class_='item')

    hemisphere_img_urls = []

    for x in image_url:
        title = x.find('h3').text
        url = x.find('a')['href']
        hem_img_url= home_url+url
    
        browser.visit(hem_img_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        
        hemisphere_img_url = soup.find('div', class_='downloads').find('a')['href']
        
        final_data = dict({'title':title, 'img_url':hemisphere_img_url})
        hemisphere_img_urls.append(final_data)

    # hemisphere_img_urls

    collection_data['Mars hemisphere'] = hemisphere_img_urls

    browser.quit()

    return collection_data


