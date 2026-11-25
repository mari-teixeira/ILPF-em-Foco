

import streamlit as st

# CONFIGURACAO
st.set_page_config(
    page_title="ILPF em Foco",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# IDENTIDADE VISUAL
st.markdown("""
<style>
.stApp {
    background-color: #F5F4EF;
}

[data-testid="stSidebar"] {
    background-color: #24543B;
}

[data-testid="stSidebar"] * {
    color: white;
}

.hero {
    background-image:
        linear-gradient(rgba(0,0,0,0.48), rgba(0,0,0,0.48)),
        url("https://www.revistarural.com.br/sitenovo/wp-content/uploads/2019/04/ILPF300420129.jpg");
    background-size: cover;
    background-position: center;
    min-height: 430px;
    padding: 65px 45px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.hero h1 {
    color: white;
    font-size: 48px;
}

.hero p {
    color: white;
    font-size: 21px;
    max-width: 700px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 12px;
    border-left: 5px solid #66845A;
    min-height: 180px;
    margin-bottom: 15px;
}

.card h3 {
    color: #24543B;
}

.card p {
    color: #555;
}

.section-title {
    color: #24543B;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# MENU
st.sidebar.title("🌱 ILPF EM FOCO")
st.sidebar.caption("Conhecimento, pesquisa e sustentabilidade")

pagina = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "Início",
        "Conheça a ILPF",
        "Modalidades de integração",
        "Implantação e manejo",
        "Benefícios e sustentabilidade",
        "Experimento IF Goiano",
        "Pesquisas e resultados",
        "Publicações e materiais"
    ]
)

# =====================================
# PAGINA INICIAL
# =====================================

if pagina == "Início":

    st.markdown("""
    <div class="hero">
        <h1>ILPF EM FOCO</h1>
        <p>
        Integração, inovação e sustentabilidade:
        conhecimento científico aplicado aos sistemas
        integrados de produção agropecuária.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        "<h2 class='section-title'>Bem-vindo ao ILPF em Foco!</h2>",
        unsafe_allow_html=True
    )

    st.write("""
    A Integração Lavoura-Pecuária-Floresta (ILPF) representa
    uma estratégia de produção que combina diferentes
    atividades agropecuárias em uma mesma área.

    Este portal foi desenvolvido para reunir conhecimentos
    técnicos, informações científicas e experiências sobre
    sistemas integrados de produção, contribuindo para a
    divulgação de tecnologias e práticas sustentáveis no campo.
    """)

    st.divider()

    st.markdown(
        "<h2 class='section-title'>Conheça os sistemas de integração</h2>",
        unsafe_allow_html=True
    )

    st.write(
        "Os sistemas podem combinar dois ou três componentes "
        "produtivos, de acordo com as características e os "
        "objetivos de cada propriedade."
    )

    col1, col2, col3, col4 = st.columns(4)

    modalidades = [
        ("🌱", "ILP", "Integração Lavoura-Pecuária",
         "Combinação entre cultivos agrícolas e produção animal."),
        ("🌳", "ILF", "Integração Lavoura-Floresta",
         "Combinação entre cultivos agrícolas e espécies florestais."),
        ("🐄", "IPF", "Integração Pecuária-Floresta",
         "Associação entre pastagens, animais e árvores."),
        ("🌱", "ILPF", "Integração Lavoura-Pecuária-Floresta",
         "Integração dos componentes agrícola, pecuário e florestal.")
    ]

    for col, item in zip(
        [col1, col2, col3, col4], modalidades
    ):
        with col:
            st.markdown(f"""
            <div class="card">
                <h2>{item[0]} {item[1]}</h2>
                <h4>{item[2]}</h4>
                <p>{item[3]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        "<h2 class='section-title'>Por que integrar?</h2>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Produção e eficiência**

        - Diversificação das atividades produtivas;
        - Melhor aproveitamento da área;
        - Otimização do uso de recursos;
        - Possibilidade de produção ao longo do ano.
        """)

    with col2:
        st.markdown("""
        **Sustentabilidade ambiental**

        - Conservação do solo e da água;
        - Ciclagem de nutrientes;
        - Melhoria do conforto térmico animal;
        - Manutenção da biodiversidade.
        """)

    st.divider()

    st.markdown(
        "<h2 class='section-title'>Pesquisa e inovação</h2>",
        unsafe_allow_html=True
    )

    st.write("""
    A pesquisa científica é fundamental para compreender
    o funcionamento dos sistemas integrados, avaliar seus
    resultados e desenvolver estratégias de manejo.

    Conheça também o espaço dedicado ao experimento de ILPF
    desenvolvido no IF Goiano, com destaque para as avaliações
    ambientais e o monitoramento de gases do solo.
    """)

    st.info(
        "Explore as seções do portal para conhecer os conceitos, "
        "as práticas de manejo e os resultados das pesquisas."
    )

    st.divider()

    st.markdown("### Fontes e conteúdos para consulta")

    st.markdown("""
    - [Embrapa – Conheça a ILPF](https://www.embrapa.br/pt/tema-integracao-lavoura-pecuaria-floresta-ilpf)
    - [Embrapa – Perguntas e respostas](https://www.embrapa.br/pt/tema-integracao-lavoura-pecuaria-floresta-ilpf/perguntas-e-respostas)
    """)

# =====================================
# CONHECA A ILPF
# =====================================

elif pagina == "Conheça a ILPF":

    st.title("🌱 O que é ILPF?")

    st.write("""
    A Integração Lavoura-Pecuária-Floresta é uma estratégia
    de produção agropecuária que integra atividades agrícolas,
    pecuárias e florestais em uma mesma área.

    Essa integração pode ocorrer por meio de consórcio,
    sucessão ou rotação, buscando estabelecer interações
    positivas entre os componentes do sistema.
    """)

    st.subheader("Como funciona?")

    st.write("""
    Na prática, diferentes atividades produtivas compartilham
    o mesmo espaço ao longo do tempo ou simultaneamente.

    A lavoura pode contribuir para a formação de pastagens,
    a pecuária pode aproveitar os resíduos vegetais e as
    árvores podem proporcionar sombra, proteção do solo
    e produtos florestais.
    """)

    st.subheader("Uma estratégia adaptável")

    st.write("""
    A escolha do sistema depende das condições climáticas,
    características do solo, relevo, infraestrutura,
    disponibilidade de máquinas, mercado e objetivos
    do produtor rural.
    """)

# =====================================
# MODALIDADES
# =====================================

elif pagina == "Modalidades de integração":

    st.title("🌳 Modalidades de integração")

    st.write("""
    Os sistemas integrados podem ser organizados em quatro
    modalidades principais:
    """)

    st.subheader("1. Integração Lavoura-Pecuária (ILP)")

    st.write("""
    Integra cultivos agrícolas e produção animal,
    podendo ocorrer em consórcio, rotação ou sucessão.
    """)

    st.subheader("2. Integração Lavoura-Floresta (ILF)")

    st.write("""
    Combina espécies agrícolas e florestais na mesma área,
    permitindo a produção de grãos e produtos florestais.
    """)

    st.subheader("3. Integração Pecuária-Floresta (IPF)")

    st.write("""
    Associa pastagens, animais e árvores, proporcionando
    diferentes possibilidades de produção e sombreamento.
    """)

    st.subheader("4. Integração Lavoura-Pecuária-Floresta (ILPF)")

    st.write("""
    Integra os três componentes produtivos, combinando
    agricultura, pecuária e floresta em um mesmo sistema.
    """)

# =====================================
# IMPLANTACAO E MANEJO
# =====================================

elif pagina == "Implantação e manejo":

    st.title("🚜 Implantação e manejo dos sistemas")

    st.write("""
    O planejamento é uma etapa fundamental para a implantação
    de sistemas integrados. É necessário conhecer as condições
    da propriedade e definir os objetivos da produção.
    """)

    etapas = [
        ("1. Diagnóstico da propriedade",
         "Avaliação do solo, clima, relevo, infraestrutura e histórico de uso da área."),
        ("2. Planejamento do sistema",
         "Definição dos componentes produtivos e do arranjo espacial."),
        ("3. Correção e preparo do solo",
         "Planejamento das práticas de correção, fertilidade e conservação do solo."),
        ("4. Implantação",
         "Estabelecimento dos componentes agrícolas, pecuários e florestais."),
        ("5. Manejo e monitoramento",
         "Acompanhamento do desenvolvimento das culturas, pastagens, animais e árvores.")
    ]

    for titulo, descricao in etapas:
        with st.expander(titulo):
            st.write(descricao)

# =====================================
# BENEFICIOS
# =====================================

elif pagina == "Benefícios e sustentabilidade":

    st.title("🌎 Benefícios e sustentabilidade")

    st.write("""
    Os sistemas integrados podem proporcionar benefícios
    produtivos, econômicos e ambientais, dependendo do
    planejamento e do manejo adotado.
    """)

    st.subheader("Benefícios agronômicos")

    st.write("""
    - Diversificação da produção;
    - Ciclagem de nutrientes;
    - Melhor aproveitamento da área;
    - Possibilidade de recuperação de áreas de pastagens;
    - Integração entre culturas agrícolas e forrageiras.
    """)

    st.subheader("Benefícios ambientais")

    st.write("""
    - Proteção do solo;
    - Melhoria da cobertura vegetal;
    - Conservação da água;
    - Potencial de aumento dos estoques de carbono no solo;
    - Melhoria do conforto térmico dos animais.
    """)

    st.subheader("Benefícios econômicos")

    st.write("""
    - Diversificação das fontes de renda;
    - Aproveitamento de diferentes produtos;
    - Redução da dependência de uma única atividade;
    - Possibilidade de melhor distribuição das receitas ao longo do ano.
    """)

    st.warning(
        "Os resultados dependem das condições locais, "
        "do arranjo produtivo e do manejo empregado."
    )

# =====================================
# EXPERIMENTO IF GOIANO
# =====================================

elif pagina == "Experimento IF Goiano":

    st.title("🔬 Experimento de ILPF – IF Goiano")

    st.write("""
    Esta seção é dedicada à apresentação do experimento
    de integração desenvolvido no IF Goiano, incluindo
    sua estrutura, tratamentos, manejo e avaliações.
    """)

    st.subheader("Organização dos tratamentos")

    st.markdown("""
    - **T:** bovinos em capim BRS Tamani.
    - **TG:** bovinos em capim BRS Tamani consorciado com guandu.
    - **TGO:** bovinos e ovinos em capim BRS Tamani consorciado com guandu.
    """)

    st.subheader("Monitoramento de gases do solo")

    st.write("""
    O monitoramento dos fluxos de gases do solo permite
    avaliar as trocas de gases de efeito estufa entre o
    solo e a atmosfera nos diferentes sistemas de manejo.
    """)

    st.markdown("""
    **Gases avaliados:**

    - Dióxido de carbono (CO₂);
    - Metano (CH₄);
    - Óxido nitroso (N₂O).
    """)

    st.info(
        "Os dados, gráficos, fotografias da área experimental "
        "e resultados das avaliações serão incorporados "
        "após a organização e validação das informações."
    )

# =====================================
# PESQUISAS
# =====================================

elif pagina == "Pesquisas e resultados":

    st.title("📊 Pesquisas e resultados")

    st.write("""
    Esta seção reunirá resultados de pesquisas científicas
    sobre sistemas integrados de produção agropecuária.
    """)

    st.subheader("Temas de pesquisa")

    st.markdown("""
    - Qualidade física, química e biológica do solo;
    - Fluxos de gases de efeito estufa;
    - Estoques de carbono;
    - Produtividade agrícola e pecuária;
    - Bem-estar animal;
    - Biodiversidade e sustentabilidade;
    - Indicadores ambientais e econômicos.
    """)

    st.info(
        "Artigos, gráficos e resultados científicos serão "
        "adicionados progressivamente."
    )

# =====================================
# PUBLICACOES
# =====================================

elif pagina == "Publicações e materiais":

    st.title("📚 Publicações e materiais técnicos")

    st.write("""
    Reúna nesta seção materiais de apoio para estudantes,
    pesquisadores, técnicos e produtores rurais.
    """)

    st.subheader("Fontes de informação")

    st.markdown("""
    - [Portal ILPF – Embrapa](https://www.embrapa.br/pt/tema-integracao-lavoura-pecuaria-floresta-ilpf)

    - [Embrapa Agrossilvipastoril](https://www.embrapa.br/web/agrossilvipastoril/solucoes-tecnologicas/integracao-lavoura-pecuaria-floresta-ilpf)

    - [Perguntas e respostas sobre ILPF](https://www.embrapa.br/pt/tema-integracao-lavoura-pecuaria-floresta-ilpf/perguntas-e-respostas)
    """)

    st.caption(
        "ILPF em Foco | Divulgação técnica e científica"
    )

# RODAPE
st.divider()

st.caption(
    "ILPF em Foco | Portal de divulgação técnica e científica"
)
    
    