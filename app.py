import streamlit as st
import pandas as pd
import numpy as np

# ------------------------------------------------------------
# Buscador de CEP — Frontend (somente estrutura)
# ------------------------------------------------------------
# Este arquivo contém apenas a estrutura visual (UI) do aplicativo.
# A lógica de requisições/integrações deve ser implementada pelos alunos.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Buscador de CEP",
    page_icon="📮",
    layout="centered",
)

# ======= Sidebar =======
with st.sidebar:
    st.header("📚 Guia Rápido")
    st.markdown(
        """
        **Objetivo:** Implementar um buscador de CEP com duas áreas:
        - **Buscar CEP:** dado um CEP, retornar os dados do endereço.
        - **Descobrir CEP:** dado **UF, cidade, bairro e logradouro**, listar CEPs possíveis.

        **Tarefas (para os alunos):**
        1. Conectar o formulário ao serviço escolhido (ex.: ViaCEP, BrasilAPI, etc.).
        2. Validar campos (CEP com 8 dígitos, UF obrigatória, etc.).
        3. Exibir resultados e tratar erros de forma amigável.
        4. (Opcional) Salvar histórico de buscas em `st.session_state`.
        """
    )
    st.divider()
    st.caption("Feito com ❤️ em Streamlit — apenas UI, sem lógica ainda.")

# ======= Header =======
st.title("📮 Buscador de CEP")
st.markdown(
    """
    Utilize as abas abaixo para **Buscar CEP** diretamente ou **Descobrir CEP** informando os dados do endereço.
    *Esta versão é somente o **frontend**; a lógica será implementada em sala.*
    """
)

# ======= Tabs =======
tab_buscar, tab_descobrir = st.tabs(["🔎 Buscar CEP", "🧭 Descobrir CEP"]) 

# ------------------------------------------------------------
# TAB 1 — Buscar CEP
# ------------------------------------------------------------
with tab_buscar:
    st.subheader("🔎 Buscar CEP")
    st.markdown("Informe um **CEP** válido (apenas números).")

    with st.form("form_buscar_cep", clear_on_submit=False):
        col1, col2 = st.columns([3, 1])
        with col1:
            cep = st.text_input(
                "CEP",
                placeholder="Ex.: 01234567",
                max_chars=9,  # permite inserir com ou sem máscara; validação ficará na lógica
                help="Digite somente números (8 dígitos).",
            )
        with col2:
            st.write("")
            st.write("")
            submit_buscar = st.form_submit_button("Buscar")

    # Área de resultado / placeholders
    st.markdown("### Resultado")
    resultado_container = st.container()

    if submit_buscar:
        # ⚠️ Placeholder: substituir pela lógica real
        with resultado_container:
            st.info("Os dados do endereço aparecerão aqui após implementar a lógica de consulta.")
            with st.expander("Detalhes recebidos (JSON)"):
                st.code("""
                {
                  "cep": "",
                  "logradouro": "",
                  "bairro": "",
                  "localidade": "",
                  "uf": "",
                  "ddd": "",
                  "gia": "",
                  "ibge": "",
                  "siafi": ""
                }
                """, language="json")
            data = pd.DataFrame({
            'lat': np.random.uniform( 35.6, 36, 10),
            'lon': np.random.uniform( 139, 140, 10) 
            })
            st.map(data)

# ------------------------------------------------------------
# TAB 2 — Descobrir CEP
# ------------------------------------------------------------
with tab_descobrir:
    st.subheader("🧭 Descobrir CEP")
    st.markdown(
        "Preencha os campos abaixo para **descobrir** o CEP a partir do endereço. "
        "Campos mínimos recomendados: **UF**, **Cidade** e **Logradouro**."
    )

    ufs = [
        "AC","AL","AP","AM","BA","CE","DF","ES","GO","MA",
        "MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN",
        "RS","RO","RR","SC","SP","SE","TO"
    ]

    with st.form("form_descobrir_cep", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            uf = st.selectbox("UF", options=["Selecione..."] + ufs, index=0)
            cidade = st.text_input("Cidade", placeholder="Ex.: São Paulo")
        with c2:
            bairro = st.text_input("Bairro (opcional)", placeholder="Ex.: Consolação")
            logradouro = st.text_input("Logradouro", placeholder="Ex.: Rua Augusta")

        col_a, col_b, col_c = st.columns([1,1,2])
        with col_a:
            numero = st.text_input("Número (opcional)", placeholder="Ex.: 123")
        with col_b:
            complemento = st.text_input("Compl. (opcional)", placeholder="Apto 12")
        with col_c:
            submit_descobrir = st.form_submit_button("Descobrir CEP")

    st.markdown("### Possíveis CEPs")
    lista_container = st.container()

    if submit_descobrir:
        # ⚠️ Placeholder: substituir pela lógica real
        with lista_container:
            st.warning("A lista de CEPs correspondentes aparecerá aqui após implementar a consulta.")
            st.caption("Dica: exibir resultado em tabela, com colunas como CEP, Logradouro, Bairro, Cidade/UF.")

    # (Opcional) Histórico de buscas — após implementação
    with st.expander("🕓 Histórico (opcional)"):
        st.caption("Exiba aqui as últimas consultas feitas pelo usuário usando st.session_state.")
        st.code(
            """
            # Exemplo (para implementar):
            # if 'historico' not in st.session_state:
            #     st.session_state.historico = []
            # st.session_state.historico.append({
            #     'tipo': 'descobrir',
            #     'uf': uf, 'cidade': cidade, 'bairro': bairro, 'logradouro': logradouro
            # })
            """,
            language="python",
        )

# ------------------------------------------------------------
# Rodapé
# ------------------------------------------------------------
st.divider()
st.markdown(
    """
    **Observações para implementação:**

    - Escolham uma API pública (ex.: ViaCEP `https://viacep.com.br/ws/`, BrasilAPI) e implementem as chamadas dentro dos blocos acima.
    - Tratem erros de rede e CEP inexistente com mensagens claras (ex.: `st.error`).
    - Validem os campos antes de enviar a requisição (ex.: CEP com 8 dígitos; UF selecionada).
    - Padronizem a exibição: cartões para resultado único, tabela para múltiplos resultados.
    - (Desafio) Implementem máscara simples de CEP (#####-###) apenas visual, sem alterar a validação numérica.
    """
)
