import streamlit as st


def chat():
    # Display a title and description
    st.title("Chatbot")
    st.write("This is a simple chatbot that can help you with your queries.")

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

