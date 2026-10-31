import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import smtplib
from email.message import EmailMessage

st.set_page_config(
    page_title="For My 💌 Sorry 🥺",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ----------------- Email Configuration ----------------- #
MY_EMAIL = "pronoypaul.333@gmail.com"
# Paste your 16-letter Google App Password here (spaces don't matter)
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]

def send_email_directly(selected_list):
    msg = EmailMessage()
    msg["Subject"] = "Forgiveness Passes Redeemed! ❤️"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL

    passes_formatted = "\n".join([f"👉 {p}" for p in selected_list])
    body = (
        f"Hey Dudu,\n\n"
        f"She accepted your apology! 🥰❤️\n\n"
        f"She redeemed the following Forgiveness Passes:\n"
        f"{passes_formatted}\n\n"
        f"Time to keep your promise! 💕"
    )
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(MY_EMAIL, GMAIL_APP_PASSWORD.replace(" ", ""))
        smtp.send_message(msg)

# ----------------- Helper: Base64 Background ----------------- #
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_path = "background.jpg"
bg_css = ""
if os.path.exists(image_path):
    bin_str = get_base64_of_bin_file(image_path)
    bg_css = f"""
    /* Default (Mobile & Tablet): Fit screen without cutting off faces at the top */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.65)), 
                    url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center 15%;
        background-repeat: no-repeat;
        background-attachment: scroll;
    }}

    /* Laptop / Desktop screens: Show the full photo cleanly without zooming in & cropping */
    @media (min-width: 768px) {{
        [data-testid="stAppViewContainer"] {{
            background: 
                linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.65)),
                url("data:image/jpeg;base64,{bin_str}") center center / contain no-repeat fixed,
                linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                url("data:image/jpeg;base64,{bin_str}") center center / cover no-repeat fixed;
        }}
    }}
    """

st.markdown(
    f"""
<style>
    {bg_css}
    
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 440px;
        margin: auto;
    }}
    h1 {{
        font-size: 1.8rem !important;
        color: #FFFFFF !important;
        text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.9);
    }}
    h2, h3, p, span, label {{
        color: #FFFFFF !important;
        text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.9);
    }}
    
    /* Style the native Streamlit Primary Button (Accept & Claim) */
    div.stButton > button[kind="primary"] {{
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.45) !important;
        width: 82% !important;
        margin: 10px auto 0px auto !important;
        display: block !important;
    }}
    div.stButton > button[kind="primary"]:hover {{
        background-color: #ff3333 !important;
        transform: scale(1.02);
    }}

    /* Style Secondary Buttons (I love you / Logout) */
    div.stButton > button[kind="secondary"] {{
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 25px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        backdrop-filter: blur(4px);
    }}
    div.stButton > button[kind="secondary"]:hover {{
        background-color: rgba(255, 255, 255, 0.28) !important;
        border-color: white !important;
    }}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------- State Management ----------------- #
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "said_love" not in st.session_state:
    st.session_state.said_love = False


# ============================================================= #
# PAGE 1: Apology & The Runaway Button
# ============================================================= #
if not st.session_state.accepted:
    st.title("I'm so sorry Bubu... 🥺")

    st.write(
        "I know I made a mistake, and I genuinely regret causing you pain. "
        "You mean the world to me, and I want to make things right."
    )

    st.markdown("**Will you forgive me?**")

    # 1. Native Streamlit button for 'Accept'
    if st.button("Apology Accepted ❤️", type="primary", use_container_width=True):
        st.session_state.accepted = True
        st.session_state.said_love = False
        st.rerun()

    # 2. JS Arena strictly for the runaway 'Reject' button
    reject_arena_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
      * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      body {
        background: transparent;
        overflow: hidden;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      .arena {
        position: relative;
        width: 100%;
        height: 190px;
      }
      #rejectBtn {
        display: block;
        padding: 13px 20px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        text-align: center;
        white-space: nowrap;
        width: 82%;
        background-color: #495057;
        color: #f8f9fa;
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        transition: top 0.14s ease-out, left 0.14s ease-out;
      }
    </style>
    </head>
    <body>

    <div class="arena" id="arena">
      <button id="rejectBtn">Apology Rejected 💔</button>
    </div>

    <script>
      const rejectBtn = document.getElementById('rejectBtn');
      const arena = document.getElementById('arena');

      function dodge(e) {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        
        rejectBtn.style.transform = "none";
        
        const arenaW = arena.clientWidth;
        const arenaH = arena.clientHeight;
        const btnW = rejectBtn.offsetWidth;
        const btnH = rejectBtn.offsetHeight;

        const maxLeft = Math.max(5, arenaW - btnW - 5);
        const maxTop = Math.max(5, arenaH - btnH - 5);

        const newX = Math.floor(Math.random() * maxLeft);
        const newY = Math.floor(Math.random() * maxTop);

        rejectBtn.style.left = newX + 'px';
        rejectBtn.style.top = newY + 'px';
      }

      rejectBtn.addEventListener('mouseenter', dodge);
      rejectBtn.addEventListener('touchstart', dodge, { passive: false });
      rejectBtn.addEventListener('click', dodge);
    </script>
    </body>
    </html>
    """

    components.html(reject_arena_html, height=200)


# ============================================================= #
# PAGE 2: Multi-Select Passes, Auto Email & Locked Logout
# ============================================================= #
else:
    st.title("Thank you for forgiving me ❤️")

    st.write(
        "I promise to learn from this and make you smile every day. "
        "Select all the passes you want to redeem right now:"
    )

    st.subheader("Your Forgiveness Passes 🎟️")

    options = [
        "Dinner date at your favorite spot (my treat)",
        "A day of zero arguments and unlimited attention",
        "One unplanned day out from my part",
        "A full day of romantic dates and surprises",
        "Trip to the beach",
    ]

    selected_passes = []
    for option in options:
        if st.checkbox(option, key=option):
            selected_passes.append(option)

    st.write("")

    # Automatic background email trigger via Gmail SMTP
    if selected_passes:
        if st.button(f"Claim {len(selected_passes)} Pass(es) & Send to Me 💌", type="primary", use_container_width=True):
            with st.spinner("Sending your passes straight to him... 💌"):
                try:
                    send_email_directly(selected_passes)
                    st.balloons()
                    st.success("Sent! Your passes have been claimed and emailed to him! 🥰❤️")
                except Exception as e:
                    st.error(f"Could not send email: {e}")
    else:
        st.info("👆 Tick at least one pass above to claim and send!")

    st.write("")
    
    # Bottom buttons: 'I love you!' unlocks 'Logout'
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I love you Dudu! 💖", type="secondary", use_container_width=True):
            st.session_state.said_love = True
            st.snow()

    with col2:
        if st.button("Logout 🔒", type="secondary", use_container_width=True):
            if st.session_state.said_love:
                st.session_state.accepted = False
                st.session_state.said_love = False
                st.rerun()
            else:
                st.warning("Uh-oh! You have to click 'I love you! 💖' first before you can leave! 😤❤️")

    # Show persistent sweet message once she has clicked 'I love you!'
    if st.session_state.said_love:
        st.success("I love you too! Best decision ever. See you soon! 🥰 (Logout is now unlocked 🔓)")