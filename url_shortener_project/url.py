import pyshorteners
import streamlit as st

#function to shorten url
def shorten_url(url):
    short_url=pyshorteners.Shortener()
    return short_url.tinyurl.short(url)

#page configuration for web app
st.set_page_config(page_title='URLShortener',layout='centered')

#title of the web app
st.title('URL Shortener')
url_input=st.text_input('Enter a URL to shorten:')

#button to shorten url
if st.button('Shorten URL'):
    if url_input:
        shortened_url=shorten_url(url_input)
        st.success(f'Shortened URL:{shortened_url}')