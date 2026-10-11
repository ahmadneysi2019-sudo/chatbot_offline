import utils
import streamlit as st

st.title('chatbot porject')

if 'messages'not in st.session_state:
    st.session_state['messages']=[{'role':'ai',
                                    'content':'how can i help you'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input()
model = 'gemma3:1b'
if prompt:

    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user',
                                         'content':prompt})
    with st.spinner('Generating Response....'):
        new_prompt = 'give me answer with example and emoji and shapes and description'+prompt
        response = utils.call_ollama_model(model ,new_prompt)

    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai',
                                         'content':response})