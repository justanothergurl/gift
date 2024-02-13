import streamlit as st

def click_yes():
    st.balloons()
    st.markdown('<div class="msg"><b>AWWWW, MY GULAB JAMUN</b></div>', unsafe_allow_html=True)
    gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmpiOGo4bG9zZTc3bnZ1aHlqa3ozd2Y2bXFzeGgzZnExbjY0ZnlmYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/19CU3F5v6fq4LawRGu/giphy.gif"
    width = 500  # set the desired width
    height = 500  # set the desired height
    st.markdown(f"<p style='text-align: center;'><img src='{gif_url}' alt='Alt Text' width='{width}' height='{height}'></p>", unsafe_allow_html=True)

def click_no():
    st.session_state.audio_playback_counter += 1
    st.audio('why-are-you-gay.mp3',start_time=0)
    st.markdown('<div class="msg"><b>TIME TO GET OUT OF THE CLOSET, HONEY</b></div>', unsafe_allow_html=True)
    gif_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXg4ZnhlNHdtdTNnY3ZobGF5MDg5MW5iaDlxeDY3Ync2emQxaWE0cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/egjCAYphmLmrm/giphy.gif"
    width = 430  # set the desired width
    height = 430  # set the desired height
    st.markdown(f"<p style='text-align: center;'><img src='{gif_url}' alt='Alt Text' width='{width}' height='{height}'></p>", unsafe_allow_html=True)


def main():
    custom_styles = """
        <style>
            .title {
                color: #ffc5e6;
                text-align: center;
                font-size: 60px;
                margin-bottom: 40px;
                margin-left:20px;
            }
            .msg {
                color: #ffffff;
                text-align: center;
                font-size: 60px;
                margin-bottom: 40px;
                margin-left:20px;
            }
            
        </style>
    """
    st.markdown(custom_styles, unsafe_allow_html=True)
    st.markdown('<div class="title"><b>Will you be my valentine?</b></div>', unsafe_allow_html=True)
    st.button("Yes", use_container_width=True, key="Yes", help="it better be your choice :)", on_click=click_yes)
    if "audio_playback_counter" not in st.session_state:
        st.session_state.audio_playback_counter = 0
    st.button("No", use_container_width=True, key="No", help="count your days bitch", on_click=click_no)
    

if __name__ == "__main__":
    main()
