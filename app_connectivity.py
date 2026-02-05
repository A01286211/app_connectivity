import streamlit as st
import time
import random

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'captcha_solved' not in st.session_state:
    st.session_state.captcha_solved = False
if 'server_checked' not in st.session_state:
    st.session_state.server_checked = False

# Page config
st.set_page_config(
    page_title="System Verification Tool v2.4",
    page_icon="🔧",
    layout="centered"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {
        color: #1f77b4;
        font-family: 'Courier New', monospace;
        border-bottom: 2px solid #ddd;
        padding-bottom: 10px;
    }
    .status-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .valentine-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .heart {
        color: #ff6b6b;
        font-size: 50px;
        animation: heartbeat 1.5s infinite;
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
</style>
""", unsafe_allow_html=True)


# ==================== STAGE 0: Initial Professional Interface ====================
def show_stage_0():
    st.markdown("<h1 class='main-header'>🔧 System Verification Tool v2.4</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.info("📋 *Purpose*: Verify system connectivity and user authentication protocols")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("System Status", "Online", "✓")
    with col2:
        st.metric("Protocol Version", "2.4.1", "Latest")
    
    st.markdown("### 📝 Pre-Flight Checklist")
    st.write("- ✅ Database Connection")
    st.write("- ✅ API Gateway Status")
    st.write("- ⏳ User Verification Pending")
    
    st.warning("⚠️ User verification required to proceed with system diagnostics")
    
    if st.button("🚀 Begin Verification Process", use_container_width=True):
        st.session_state.stage = 1
        st.rerun()


# ==================== STAGE 1: Fake CAPTCHA ====================
def show_stage_1():
    st.markdown("<h1 class='main-header'>🔐 Security Verification</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.write("*Security Protocol*: CAPTCHA v3.2")
    st.write("Please complete the verification below to continue")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 🤖 Verify you're human")
    
    # Simple math CAPTCHA
    if 'captcha_answer' not in st.session_state:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        st.session_state.captcha_answer = num1 + num2
        st.session_state.captcha_q = f"{num1} + {num2}"
    
    st.write(f"*Question*: What is {st.session_state.captcha_q}?")
    
    user_answer = st.number_input("Your answer:", min_value=0, max_value=100, step=1, key="captcha_input")
    
    if st.button("✓ Verify", use_container_width=True):
        if user_answer == st.session_state.captcha_answer:
            st.success("✅ Verification successful!")
            time.sleep(1)
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("❌ Incorrect answer. Please try again.")


# ==================== STAGE 2: Server Connectivity Check ====================
def show_stage_2():
    st.markdown("<h1 class='main-header'>🌐 Server Connectivity Check</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    if not st.session_state.server_checked:
        st.info("🔄 Initiating connection to remote servers...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        servers = [
            "auth.server.com",
            "api.gateway.io",
            "database.cluster.net",
            "cdn.content.org",
            "special.message.server"  # The hint!
        ]
        
        for i, server in enumerate(servers):
            status_text.text(f"Pinging {server}...")
            progress_bar.progress((i + 1) / len(servers))
            time.sleep(0.8)
        
        st.success("✅ All servers responding normally!")
        st.session_state.server_checked = True
        time.sleep(1)
        st.rerun()
    
    else:
        st.success("✅ Connection established successfully!")
        
        st.markdown("### 📊 Connection Report")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Latency", "12ms", "-3ms")
        with col2:
            st.metric("Packet Loss", "0%", "0%")
        with col3:
            st.metric("Bandwidth", "1.2Gbps", "+0.3Gbps")
        
        st.info("🔔 Notice: Special message detected from server...")
        
        if st.button("📩 Retrieve Message", use_container_width=True):
            st.session_state.stage = 3
            st.rerun()


# ==================== STAGE 3: Decoding Message ====================
def show_stage_3():
    st.markdown("<h1 class='main-header'>📡 Message Decryption</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.warning("🔐 Encrypted message detected. Decrypting...")
    
    encrypted_messages = [
        "01110100 01100101 00100000 01100001 01101101 01101111 00100000 01110011 01101000 01100101 01111001 01110010 01100001",
        "WW91IGJl",
        "bXkgVmFs",
        "ZW50aW5l",
        "Pw=="
    ]
    
    progress_bar = st.progress(0)
    decoded_text = st.empty()
    
    for i, msg in enumerate(encrypted_messages):
        decoded_text.code(msg, language="text")
        progress_bar.progress((i + 1) / len(encrypted_messages))
        time.sleep(1)
    
    st.success("✅ Decryption complete!")
    
    if st.button("📖 Read Message", use_container_width=True):
        st.session_state.stage = 4
        st.rerun()


# ==================== STAGE 4: Puzzle/Riddle ====================
def show_stage_4():
    st.markdown("<h1 class='main-header'>🧩 Final Verification Step</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<div class='status-box'>", unsafe_allow_html=True)
    st.write("*Security Protocol*: Pattern Recognition")
    st.write("One last verification before accessing the message...")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 💭 Solve this:")
    st.write("""
    *A riddle for you:*
    
    I come once a year, with hearts all around,  
    Chocolates and flowers, love is found,  
    Cupid shoots arrows, couples unite,  
    What celebration is this? Get it right!
    """)
    
    answer = st.text_input("Your answer:", key="riddle_answer").lower().strip()
    
    if st.button("Submit Answer", use_container_width=True):
        if "valentine" in answer:
            st.balloons()
            st.success("🎉 Correct! Unlocking final message...")
            time.sleep(2)
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("❌ Not quite... Think about February 14th!")


# ==================== STAGE 5: The Big Reveal! ====================
def show_stage_5():
    st.markdown("""
    <div class='valentine-box'>
        <div class='heart'>❤️</div>
        <h1>Surprise! 🎉</h1>
        <h2>This wasn't really a work project...</h2>
        <br>
        <h3>I built this entire app just to ask you one question:</h3>
        <br>
        <h1 style='font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            Will you be my Valentine? 💕
        </h1>
        <br>
        <p style='font-size: 18px; font-style: italic;'>
            I really like you, and I wanted to do something special to show it. 
            <br>I hope this made you smile! 😊
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💝 Yes! Absolutely!", use_container_width=True):
            st.balloons()
            st.success("🎉 You've made me the happiest person! 💕")
            st.snow()
    
    with col2:
        if st.button("🤔 Let me think about it", use_container_width=True):
            st.info("That's okay! Take your time 😊")
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #888;'>Made with ❤️ and Python</p>", unsafe_allow_html=True)


# ==================== Main App Logic ====================
def main():
    if st.session_state.stage == 0:
        show_stage_0()
    elif st.session_state.stage == 1:
        show_stage_1()
    elif st.session_state.stage == 2:
        show_stage_2()
    elif st.session_state.stage == 3:
        show_stage_3()
    elif st.session_state.stage == 4:
        show_stage_4()
    elif st.session_state.stage == 5:
        show_stage_5()

if _name_ == "_main_":
    main()