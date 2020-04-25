from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import re
import pandas as pd

def scrape_all():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    
    news_title, news_paragraph= news(browser)
    #featured_img = mars_img(browser),
    mars_w = mars_weather(browser)
    #table = facts_mars(browser)


    return {
        "news_t" : news_title,
        "new_p" : news_paragraph,
        #"featured_img": mars_img,
        "mars_w": mars_weather
        #hemispheres: mars_hemispheres,
        #"facts": table
    }



    # hemispheres
    # weather
    # facts
def news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=5.0)
    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep (5.0)
    element = soup.select_one("ul.item_list li.slide")
    time.sleep(5.0)
    return element.find("div", class_="content_title").text,element.find("div", class_="article_teaser_body").text

def mars_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5.0)
    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(5.0)
    mars_weather = soup.find("div", attrs={"class":"tweet", "data":"Mars Weather"})                         
    try:
        m_weather = mars_weather.find("p", "tweet.text").get_text()
        m_weather
    except AttributeError:
        pattern = re.compile(r'sol')
        m_weather = soup.find("span",text=pattern).text
    return m_weather


# def mars_img(browser):
    # mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # time.sleep(5.0)
    # browser.visit(mars_image_url)
    # browser.click_link_by_id('full_image')
    # time.sleep(5.0)
    # browser.click_link_by_partial_text('more info')
    # image_html = browser.html
    # mars_image_soup = bs(image_html, 'html.parser')
    # image = mars_image_soup.body.find("figure", class_="lede")
    # time.sleep(5.0)
    # link = image.find('a')
    # href = link['href']
    # base_url='https://www.jpl.nasa.gov'
    # time.sleep (5.0)
    #retunr featured_image_url = base_url + href

# Mars facts to be scraped, converted into html table
# def facts_mars(browser):
#     facts_url = 'https://space-facts.com/mars/'
#     time.sleep(5.0)
#     tables = pd.read_html(facts_url)
#     mars_facts_df = tables[2]
#     mars_facts_df.columns = ["Description", "Value"]
#     mars_html_table = mars_facts_df.to_html()
#     mars_html_table.replace('\n', '')
#     return mars_html_table
    # Close the browser after scraping
    browser.quit()

    # Return results
    #return mars_dict