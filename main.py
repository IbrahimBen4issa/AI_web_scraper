import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    extract_body_content,
    clean_body_content
)
from parse import parse_with_ollama



st.title("AI Web Scraper !!")
url = st.text_input("Enter the website URL:")

if st.button("Scrapesite"):
    st.write("scraping the website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("Cleaned DOM Content"):
        st.text_area("Cleaned Content", cleaned_content, height=300)

if 'dom_content' in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)

