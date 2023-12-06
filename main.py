import streamlit as st
from streamlit_chat import message

from lookup_google_shopping import lookup

st.set_page_config(
    page_title="Search & Save app.",
    page_icon="🛍️",
)

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


st.sidebar.header("Sobre o Desenvolvedor")
nome = "Renato Moraes"
titulo = "Cientista de Dados"
linkedin_url = "https://linkedin.com/in/renato-moraes-11b546272"
github_url = "https://github.com/RenatoDev4"

st.sidebar.text(f"Nome: {nome}")
st.sidebar.text(f"Cargo: {titulo}")
st.sidebar.markdown(
    f"**[LinkedIn]({linkedin_url})** | **[GitHub]({github_url})**"
)  # noqa

st.sidebar.markdown("***")

st.sidebar.header("Sobre o Projeto")
st.sidebar.info(
    "Este aplicativo foi criado com o objetivo de encontrar os preços mais baixos de produtos, com ênfase em itens relacionados a computadores, como ***processadores***, ***memórias***, ***SSDs*** e ***placas de vídeo***, entre outros. É importante destacar que sua eficácia pode ser limitada ao ser utilizado para buscar preços de outros tipos de produtos. Além disso, é possível que o aplicativo apresente alguns bugs."  # noqa
)

st.sidebar.markdown("***")

lojas = [
    "KabuM",
    "Amazon",
    "Pichau",
    "Terabyte",
    "ITX Gamer",
    "GKInfoStore",
    "Inpower",
    "Waz",
    "GuerraDigital",
]

st.sidebar.header("Lojas em que a IA faz as buscas")
st.sidebar.info("\n".join([f"- {loja}" for loja in lojas]))

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

central_image_path = "img/banner_cortado.png"
st.image(central_image_path, width=700)
st.header("Pesquisa de preço")
st.info(
    "Digite o nome do produto desejado no campo de pesquisa e aguarde a resposta da AI, que mostrará o menor preço encontrado."  # noqa
)


prompt = st.text_input("Nome do produto:", placeholder="Exemplo: RTX 4060")

if st.button("Buscar preço"):
    if prompt:
        with st.spinner("Procurando pelo menor preço.. Por favor aguarde."):
            generated_response = lookup(product_name=prompt)

            formatted_response = f"{generated_response}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["user_prompt_history"]:
    for i in reversed(range(len(st.session_state["user_prompt_history"]))):
        product_query = st.session_state["user_prompt_history"][i]
        price_response = st.session_state["chat_answers_history"][i]

        key = f"chat_message_{i}"

        message(
            f"Resultado de pesquisa de preço para: {product_query}",
            is_user=True,
            key=key,
        )
        message(price_response, key=f"response_message_{i}")
