#what we want the program tgo do
#what variables we need
#how are we going to do it

#Open up a series of web pages

#We need a list of urls that we will Open
#open up a series of tabs

import webbrowser
import time
socialMediaUrls = ["www.facebook.com", "www.twitter.com"]
techUrls = ["www.pcper.com", "https://www.youtube.com/user/jerzybakes420"]

def open_tabs(url_list):
    for url in url_list:
        webbrowser.open_new_tab(url)
def main():
    webbrowser.open("www.youtube.com", new=0, autoraise=False)
    time.sleep(1)
    open_tabs(socialMediaUrls)
    open_tabs(techUrls)

main()
