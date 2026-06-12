import time
import streamlit as st

from src.services.agent_service import AgentService

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

# --------------------------------------------------
# Service Initialization
# --------------------------------------------------

service = AgentService()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "questions_count" not in st.session_state:
    st.session_state.questions_count = 0

if "response_times" not in st.session_state:
    st.session_state.response_times = []

if "quick_question" not in st.session_state:
    st.session_state.quick_question = None

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🏢 Enterprise Knowledge Agent")

    st.markdown("---")

    st.subheader("About")

    st.markdown("""
Enterprise document assistant powered by:

- Azure AI Foundry
- GPT-4.1 Mini
- File Search
- Vector Store
- RAG Architecture
""")

    st.markdown("---")

    st.subheader("System Status")

    st.success("🟢 Agent Online")

    st.caption("Version 1.0")

    st.markdown("---")

    st.subheader("Quick Questions")

    if st.button("📅 Annual Leave Policy"):
        st.session_state.quick_question = (
            "How many annual leave days are employees entitled to?"
        )

    if st.button("🏨 Hotel Reimbursement"):
        st.session_state.quick_question = (
            "What is the hotel reimbursement limit for metro cities?"
        )

    if st.button("👨‍💼 Leave Approval"):
        st.session_state.quick_question = (
            "Can a Team Lead approve 5 days of leave?"
        )

    if st.button("❌ Unknown Policy"):
        st.session_state.quick_question = (
            "What is the maternity leave policy?"
        )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.questions_count = 0
        st.session_state.response_times = []
        st.session_state.quick_question = None

        st.rerun()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📚 Enterprise Knowledge Assistant")

st.caption(
    "Ask questions about company policies, procedures, employee benefits, approvals, and internal documents."
)

# --------------------------------------------------
# Metrics Dashboard
# --------------------------------------------------

avg_response_time = 0

if st.session_state.response_times:
    avg_response_time = round(
        sum(st.session_state.response_times)
        / len(st.session_state.response_times),
        2
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "GPT-4.1 Mini")

with col2:
    st.metric("Knowledge Base", "3 PDFs")

with col3:
    st.metric(
        "Questions",
        st.session_state.questions_count
    )

with col4:
    st.metric(
        "Avg Response",
        f"{avg_response_time}s"
    )

st.markdown("---")

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------

if len(st.session_state.messages) == 0:

    st.info(
        "Welcome! Ask questions about employee leave, travel reimbursement, approvals, and company policies."
    )

    st.subheader("Example Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "How many annual leave days are employees entitled to?"
        ):
            st.session_state.quick_question = (
                "How many annual leave days are employees entitled to?"
            )

        if st.button(
            "Can a Team Lead approve 5 days of leave?"
        ):
            st.session_state.quick_question = (
                "Can a Team Lead approve 5 days of leave?"
            )

    with col2:

        if st.button(
            "What is the hotel reimbursement limit for metro cities?"
        ):
            st.session_state.quick_question = (
                "What is the hotel reimbursement limit for metro cities?"
            )

        if st.button(
            "What is the maternity leave policy?"
        ):
            st.session_state.quick_question = (
                "What is the maternity leave policy?"
            )

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a question about company policies..."
)

# --------------------------------------------------
# Quick Question Handling
# --------------------------------------------------

if st.session_state.quick_question:

    question = st.session_state.quick_question
    st.session_state.quick_question = None

# --------------------------------------------------
# Process Question
# --------------------------------------------------

if question:

    st.session_state.questions_count += 1

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching enterprise knowledge base..."
        ):

            start_time = time.time()

            answer = service.ask_agent(question)

            elapsed_time = round(
                time.time() - start_time,
                2
            )

            st.session_state.response_times.append(
                elapsed_time
            )

        st.write(answer)

        st.caption(
            f"⏱️ Response generated in {elapsed_time} seconds"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Force refresh so metrics update immediately
    st.rerun()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Powered by Azure AI Foundry • GPT-4.1 Mini • File Search • Vector Store • RAG"
)