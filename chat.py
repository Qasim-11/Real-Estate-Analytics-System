import streamlit as st

# Set the page title
st.set_page_config(page_title="Voiceflow Chatbot")

# Display a title and description
st.title("Welcome to My Website")
st.write("This is a simple webpage with a Voiceflow chatbot.")

# Add the Voiceflow chatbot script using Streamlit's HTML component
chatbot_script = """
<script type="text/javascript">
    (function(d, t) {
        var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
        v.onload = function() {
            window.voiceflow.chat.load({
                verify: { projectID: '66bce9ba54f05efaa188bc69' },
                url: 'https://general-runtime.voiceflow.com',
                versionID: 'production'
            });
        }
        v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; 
        v.type = "text/javascript"; 
        s.parentNode.insertBefore(v, s);
    })(document, 'script');
</script>
"""

# Embed the chatbot into the Streamlit app
st.components.v1.html(chatbot_script, height=600)

