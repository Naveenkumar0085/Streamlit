import streamlit as st


st.set_page_config(page_title="My W0ebpage",page_icon=":tada:",layout="wide")

with st. container():
  st.subheader("Hi, I am Naveen :wave:")
  st.title("A Data Analyst From India")
  st.write("I am passionate about finding ways to use python and VBA to be more efficient and effective in business setting.")
  st.write("[Learn More >](https://www.instagram.com/naveen_sandy_2330/)")

with st.container():
  st.write("---")
  left_column,right_column = st.column(2)  
  with left_column:
    st.header("What I do")
    st.write("##")
    st.write(
      """
      There's no need to spend days or weeks building a website anymore. In this video,
      I'm going to show you how to build a website with a blog and a contact page in only 12 minutes using Python, 
      Streamlit and other open-source tools."""
    )
    st.write("[youTube channel>](https://www.youtube.com/watch?v=VqgUkExPvLY)")
