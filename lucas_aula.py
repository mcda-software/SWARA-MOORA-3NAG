###================================ LUCAS ======================================
###================================ LUCAS ======================================
###================================ LUCAS ======================================
###================================ LUCAS ======================================

#st.dataframe(df.style.highlight_max(axis=0))


import streamlit as st
import pandas as pd                 # CRIAÇÃO DA DATAFRAMES (TABELAS)
import numpy as np                  # OPERAÇÕES ALGÉBRICAS
from st_aggrid import AgGrid
from random import random
#import math as mt                   # FUNÇÕES MATEMÁTICAS
#import statistics as stt             # Importantes sobre médias, medianas, desvio padrao https://www.youtube.com/watch?v=Ztft4ggLPdg
from typing import Type             # Plotar resultados com o grafico deitado
#import altair as alt                #plotar graficos mais simples
import seaborn as sns             # Apresentação de um grafico com mapa de calor
import matplotlib.pyplot as plt   # Plotar o resultado em gráficos 
#import plotly.express as px       # Plotar o resultado em grafico como o matplotlib
from IPython.display import display, HTML #Para deixar os textos visualmente melhores
#import matplotlib
#import duplicates



with open("teste_botao.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)


def set_bg_hack_url():
#    '''
#    A function to unpack an image from url and set as bg.
#    Returns
#    -------
#    The background.
#    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/tstyYps/CRITIC-GRA-3-N-site-1700-800-px-4.png");
             
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#https://media.istockphoto.com/vectors/vector-abstract-technology-innovation-clean-design-background-vector-id477203456?k=6&m=477203456&s=170667a&w=0&h=50PEVTWD6elGqLRjGm1nb74tEjkx2pP-MwgB9b5RRvQ=
set_bg_hack_url()


#if 'numero_alternativa' not in st.session_state: st.session_state['numero_alternativa']= 0       #Colocado pelo LORRAN =-=-=-=-=-=-=-=-=- 
#if 'numero_criterio' not in st.session_state: st.session_state['numero_criterio'] = 0
#if 'coeficiente' not in st.session_state: st.session_state['coeficiente'] = 0
#if 'botao_inclusao_da_matriz' not in st.session_state: st.session_state['botao_inclusao_da_matriz'] = 0
#if 'nome_trabalho' not in st.session_state: st.session_state['nome_trabalho'] = 0



#st.set_page_config(page_title="SWARA-MOORA-3NAG (SM-3NAG)",page_icon="logo_sm-3nag.jpeg",layout="centered")
#st.sidebar.image('1critic-gra-3n.jpeg', use_column_width = 'always')
st.sidebar.image('2logo_sm-3nag.jpeg', use_column_width = 'always')
st.image('reduzido_sm-3nag.jpeg', use_column_width = 'always')
#st.header('SWARA - MOORA - 3NAG')

paginas = ['Home', 'Sobre', 'Autores']
st.sidebar.markdown('# :house: **Menu**')
pagina = st.sidebar.selectbox('Escolha uma página: ', paginas, key='lista_paginas2')

st.sidebar.write('')
st.sidebar.write('')
st.sidebar.markdown("**Para mais métodos e softwares acesse:** ")
st.sidebar.markdown("'Casa da Pesquisa Operacional' - [Youtube](https://www.youtube.com/c/CasadaPesquisaOperacional)")
st.sidebar.image('Casa da Pesquisa.jpeg', caption='Casa da Pesquisa Operacional')



if pagina == 'Home':
    st.markdown('# Bem vindo ao software *Gratuito* para apoio a tomada de decisão.')
    '''
    ### O Site foi desenvolvido para que possa auxiliar o tomador de decisão de uma forma simples, contudo poderosa, além de totalmente gratuita.

    ### Você precisará entrar com os dados desejados de seu problema para que se possa obter um resultado.
    
    #### Buscamos cumprir com os seguintes tópicos: 
    - Ser uma ferramenta online ~~PAGA~~ Totalmente Gratuita
    - Ser um site totalmente intuitivo
    - Simplicidade ao incluir os dados
    - Apresentação detalhada dos resultados
    
    '''
    #st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.markdown('### Para iniciar, inclua o nome do Trabalho:')
    with st.form(key="inicio"):
        trabalho = st.text_input('Nome do Trabalho:')
        botao_iniciar = st.form_submit_button('Iniciar')
    if botao_iniciar == True:
        st.write('O nome escolhido para o trabalho foi: ', trabalho)
    
    '''
    
    ### Insira o número de Alternativas do problema e os seus respectivos nomes:'''
    lista_alternativas = []
    col1, col2 =st.columns([1,3])
    with col1:
        with st.form(key = 'Form1'):
            numero_alternativas = st.number_input('Numero de Alternativas:', 2, 100, step=1, key=0)
            st.form_submit_button('Confirmar nº de Alternativas')
                
    with col2:
        i=1
        for a in range(numero_alternativas):
            #i=1
            alternativa = st.text_input(f'Adicione o nome da Alternativa A{i}: ', key = i)
            i+=1
            lista_alternativas.append(alternativa)
        #def VerficarDuplicados(lista_alternativas):
        #    return list(duplicates(lista_alternativas))
        #if VerficarDuplicados != []:
        #    st.error('Não pode existir nome de Alternativas iguais. Por favor Renomeie as suas Alternativas !!!') 

    numero_alternativas = 4                  # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    lista_alternativas = ['a1','a2','a3','a4']    # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #st.write(numero_alternativas)                # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #st.write(lista_alternativas)             # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    '''
    
    ### Nesse momento será necessário incluir três itens:
    ##### 1 - O número de Critérios do problema;
    ##### 2 - Insira os nomes dos critérios em ordem de preferência; e
    ##### 3 - Informar se o Critério é monotónico de Custo (C) ou monotónico de Lucro (L).
    '''    
    st.write('Obs.:') 
    st.write('Critério monotônico de Custo = Quanto maior for o valor, pior será para Alternativa.') 
    st.write('Critério monotônico de Lucro = Quanto maior for o valor, melhor será para Alternativa.') 
    st.write('Os nomes dos Critérios deverão ser distintos.')
    st.write('')
    #lista_criterios = []
    lista_criterios =[]
    id_criterio = []
    col1, col2 = st.columns([1,3])
    with col1:
            with st.form(key = 'Form2'):
                numero_criterios = st.number_input('Numero de Critérios:', 2, 100, step=1, key=0)
                st.form_submit_button('Confirmar nº de Critérios')
                
    with col2:
        y=1
        for a in range(numero_criterios):
            criterios = st.text_input(f'Adicione o nome do Critério C{y}: ', key = {y+100})
            ID = st.text_input(f'Informar se o Critério C{y} é Monotônico de Lucro (L) ou Custo (C): ', 
                                key = {y+200}, 
                                max_chars = 1, 
                                help = 'Escolha "L" ou "C".', 
                                placeholder ='L ou C' ).upper()
            if ID not in 'LClc':
                st.error('Entre com a Letra "L" para Lucro ou "C" para Custo !!!')
            #while ID not in 'LC':
            #    st.error('Entre com a Letra "L" para Lucro ou "C" para Custo !!! ')
            #    ID = st.text_input(f'Informar se o Critério C{y} é Monotônico de Lucro (L) ou Custo (C): ', key = {y+200}).upper()
            y+=1
            lista_criterios.append(criterios)
            id_criterio.append(ID)
        #def VerficarDuplicados(lista_criterios):
        #    return list(duplicates(lista_criterios))
        #if VerficarDuplicados != None:
        #    st.error('Não pode existir nome de critérios iguais. Por favor Renomeie os seus Critérios !!!') 
        #st.write(VerficarDuplicados(lista_criterios))
        #st.write(lista_criterios)
        #st.write(id_criterio)
            
    lista_criterios = ['c1','c2','c3','c4','c5','c6', 'c7']      # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    numero_criterios = 7                     # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    id_criterio = ['L','L','C','L','L','L', 'C']            # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #st.write(lista_criterios)
    #st.write(id_criterio)
    #st.write(numero_criterios)
    '''

    ### Apresente o quanto os Cristerios são menos importantes entre si. 
    ''' 
    with st.form(key = 'Form3'):
        '''
            #### OBS.:
            - Caso dois Critérios sejam iguais deverá ser marcado o valor 'ZERO'. 
            - Caso marque o valor '1', significa que o Critério é 100% pior que o seu anterior.
            
        '''    
        st.write('_______________________________________________________________')
        z=0
        valor_importancia_sj = []
        nome_comparacao = []
        for a in range(numero_criterios-1):
            w=0
            col1, col2 = st.columns(2)
            with col1:
                st.write(f'Quanto o Critérios "{lista_criterios[z+1]}" é pior em relação ao')
                st.write(f'Critério "{lista_criterios[z]}"')
            with col2:
                comparacao = st.slider('', 
                                    min_value=0.00, 
                                    max_value=1.00,
                                    value = 0.50, 
                                    step=0.01, key=z)
            st.write('_______________________________________________________________')                        
            valor_importancia_sj.append(comparacao)
            w= f'Comparação {z+1}'
            nome_comparacao.append(w)                        
            z+=1
            
        st.form_submit_button('Confirmar os valores de comparação.')
        df_comparacao = pd.DataFrame(valor_importancia_sj , index=nome_comparacao, columns= ['%'] )
        st.dataframe(df_comparacao, width = 300)
    
    if lista_criterios[-1] is not "":
        st.write('A matriz de decisão é:')
        matrix_1 = np.zeros((numero_alternativas,numero_criterios))
        df = pd.DataFrame(matrix_1,index = lista_alternativas,columns=lista_criterios)
        st.dataframe(data=df)

        with st.form(key = 'Form4'):
            '''

            ### Insira o valor de cada Alternativa para cada Critério:
            
            - Após a inserção de cada valor deverá ser pressionado a tecla "Enter" 
            - Os valores "não inteiros" deverão ser inseridos com Ponto. Exemplo: "10.5", "6.3" etc.  
            - Os valores inseridos poderão ser conferidos na Matriz de Decisao que se segue, após clicar no botão. '''

            ag = AgGrid(df, editable=True, height=200, layout="centered")
            df2 = ag['data']
            
            botao_inclusao_matriz = st.form_submit_button('Confirmar os valores inseridos.')
            df2.index = lista_alternativas
            st.dataframe(df2)
            matriz = np.array(df2)                        # Para retirar os valores da matriz
            #st.write(matriz)
            matriz = [[2.6,4.2,210000,3.3,1,190,120],                  # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            [5.18,12,136970,6,1,200,70],                           # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            [5.18,15,185000,4.7,1,200,70],                       # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            [5.09,7,82419,4,2,150,50]]                       # retirar isso aqui  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                 
#===============================================================================================
#===============================================================================================
                                #INICIO DOS CALCULOS
#===============================================================================================
#===============================================================================================
    st.markdown("<h3 style = 'text-align: center;'>Escolha 'Sim' para calcular o resultado:</h3>", unsafe_allow_html=True)
    resultado_radio = st.selectbox('', ['Sim', 'Não'], key='resultado_selebox1', index=1)
    #st.radio('Para calcular o resultado click em "Sim":', ['Sim', 'Não'], key='resultado_radio1', index=1)
    if resultado_radio == 'Sim':

    # =============== /////// ===========  SWARA ========== /////// ============
        valor_importancia_sj.insert(0, 0.0)   #faz referencia para o primeiro criterio

        coluna1 = ['Importância comparativa de valor médio sj']
        coluna2 = ['Coeficiente kj = (sj+1)']
        coluna3 = ['Peso recalculado']
        coluna4 = ['Peso Final SWARA']

        n_criterios_base_cálculos = numero_criterios-1

    #CRIANDO A LISTA QUE TODOS OS ELEMENTOS SÃO 1, OS MESMOS SÃO SOMADOS AOS VALORES DE IMPORTÂNCIA
        kj_novo = []

        for x in range(0, n_criterios_base_cálculos):
            valorkj = float(1)
            kj_novo.append(valorkj)
        #      print('')
        kj_novo.insert(0, 1.0)


    #CRIANDO A LISTA DO COEFICIÊNTE DE KJ
        coef_kj = []
        for elemA, elemB in zip(valor_importancia_sj, kj_novo):
            coef_kj.append(elemA + elemB)


    #CRIANDO  LISTA DO PESO RECALCULADO, CONSIDERANDO QUE O PRIMEIRO ITEM DA LISTA É 1
        peso_recalculado = [1]

        for x in range(0, n_criterios_base_cálculos):
            if coef_kj[x] == 0:
                valor_peso = float(1)
            else:
                valor_peso = float(peso_recalculado[x]) / (coef_kj[x+1])
            peso_recalculado.append(valor_peso)

        soma_peso_recalculado = sum(peso_recalculado)

    #CRIANDO A LISTA DOS PESOS FINAIS
        peso_final = []
        for i in range(0, numero_criterios):
            valor_peso_final = float(peso_recalculado[i])/(soma_peso_recalculado)
            peso_final.append(valor_peso_final)
    
        tabela1 = pd.DataFrame(data = valor_importancia_sj, index = lista_criterios, columns = coluna1 )
        tabela2 = pd.DataFrame(data = coef_kj, index = lista_criterios, columns = coluna2)
        tabela3 = pd.DataFrame(data = peso_recalculado, index = lista_criterios, columns = coluna3)
        tabela4 = pd.DataFrame(data = peso_final, index = lista_criterios, columns = coluna4)
        

    # Calculando o Gráfico
        from typing import Type
        eixo_y = lista_criterios
        dados_grafico = peso_final
    
        altura = [] # valor que está no eixo x
        for i in dados_grafico:
            altura.append(i)
        posicao = []
        for i in range(0,10,1): 
            posicao.append(i)

        L = ['Ordenação']
        x = eixo_y
        y = dados_grafico
        df_swara = pd.DataFrame(data = y, index = x, columns = L)

        fig_swara, ax = plt.subplots(figsize=(8,6))
        
        #criando o gráfico de barras horizontais
        ax = sns.barplot(y=df_swara.index, x=df_swara['Ordenação'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
        #YlOrRd
        #PuBu
        #YlGn
        #GnBu

        #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

        ax.set_facecolor("white") #colocando um fundo branco no gráfico
        ax.set_title("Peso dos critérios", fontdict={'fontsize':15}) #adicionando título
        ax.set_xlabel('Valores', fontdict={'fontsize':14}) #mudando e nome e tamanho do label x
        ax.set_ylabel('Critérios', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
        ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
        ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior

        for axis in ['top', 'right', 'left']: #remoção dos outros três axis
            ax.spines[axis].set_color(None)

        ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks

        #colocando rótulo no gráfico
        rotulo_grafico2 = dados_grafico 
        for index, value in enumerate(rotulo_grafico2): 
            plt.text(value, index, 
                    str(round(value,4)))

        #otimizar espaço da figure
        fig_swara.tight_layout()
     

    #===============================================================================================
    #===============================================================================================
                                # MOORA
    #===============================================================================================
    #===============================================================================================
        ################ Normalização da matriz de decisão ################

        ################ Matriz Potência ################
        matriz_potencia = np.power(matriz,2)
        
        imprime_matriz_potencia = pd.DataFrame(data = matriz_potencia, index = lista_alternativas, columns = lista_criterios)
    
        lista_soma_dos_valores_quadrados_x = np.sum(matriz_potencia, axis=0)    #somando as colunas da matriz potencia (axis=0)
        lista_soma_dos_valores_quadrados = lista_soma_dos_valores_quadrados_x.astype(np.float)  #Transformando o array em float

        raiz = np.sqrt(lista_soma_dos_valores_quadrados)
        SM = ['SOMA DOS QUADRADOS']
        df = pd.DataFrame(lista_soma_dos_valores_quadrados, index = lista_criterios, columns = SM)
    
        lista_matriz_potencia = [matriz_potencia]
        #=========================================
        #Dividindo pela raiz

        teste_matriz=[]
        coisa=0
        for c in range(0, numero_criterios):
            lista=[]
            for l in range(0, numero_alternativas):
                coisa = matriz[l][c]/raiz[c]
                lista.append(coisa)
            teste_matriz.append(lista)  
        
        ############################## SOMA DOS QUADRADOS ###################################
        somaquadrados = pd.DataFrame(data = df, index = lista_criterios, columns = SM)
    
        ############################## MATRIZ NORMALIZADA #####################################
        #'MATRIZ NORMALIZADA - PRIMEIRA NORMALIZAÇÃO - 1N - TRADICIONAL'
        
        transposta_normalizada = np.transpose(teste_matriz)
        m_normalizada = pd.DataFrame(data = transposta_normalizada, index = lista_alternativas, columns = lista_criterios)
        
        matriz_normalizada=pd.DataFrame(data=teste_matriz)
        
        #################################### MATRIZ PONDERADA #############################################

        # 'MATRIZ PONDERADA - PRIMEIRA NORMALIZAÇÃO - 1N - TRADICIONAL'
        ponderada_matriz = []
        transp_ponderada_matriz = []
        linha_coluna = 0
        for c in range(0, numero_criterios):
            lista=[]
            for l in range(0, numero_alternativas):
                linha_coluna = peso_final[c]*transposta_normalizada[l][c]
                lista.append(linha_coluna)
            transp_ponderada_matriz.append(lista)  

        ponderada_matriz = np.transpose(transp_ponderada_matriz)

        ponderada = []
        ponderada = pd.DataFrame(data = ponderada_matriz, index = lista_alternativas, columns = lista_criterios)
        
        #################################### Ordenação tradicional MOORA #########################################

        display(HTML('<h3> ORDENAÇÃO </h3>'))
        LUCRO = []
        CUSTO = []
        for L in range(numero_alternativas):
            lista_lucro=[]
            lista_custo=[]
            lucrinho = float(0)
            custinho = float(0)
            for C in range(numero_criterios):
                if id_criterio[C] in ('l', 'L'):
                    lucrinho = ponderada_matriz[L][C]
                    lista_lucro.append(lucrinho) 
                else:
                    if id_criterio[C] in ('C', 'c'):
                        custinho = ponderada_matriz[L][C]
                        lista_custo.append(custinho)
            LUCRO.append(lista_lucro)
            CUSTO.append(lista_custo)

        lucro_pandas= pd.DataFrame(data=LUCRO, index=lista_alternativas)
        custo_pandas= pd.DataFrame(data=CUSTO, index=lista_alternativas)

        somatorio = lucro_pandas.sum(axis=1) - custo_pandas.sum(axis=1)

        y=['Ordenação MOORA']
        somatorio_df= pd.DataFrame(somatorio, index=lista_alternativas, columns=y)
        sort_somatorio = somatorio_df.sort_values(by=['Ordenação MOORA'], ascending=False)
        
        ###################### Inicio Segunda Ordenação:  Selecionando valores MAX e MIN dos Criterios ##############################

        #pegar o max e min da matriz ponderada final 3 linhas 4 COLUNAS
        #Verificar se a Id é de custo ou lucro
        #se for Custo pega o menor valor do criterio
        #se for Lucro pegar o maior valor do criterio
        #pegar esse valor e considerar como modulo(valor de referencia - absoluto). Ir na matriz ponderada, 

        max_ponderda=[]            
        min_ponderada=[]
        valor_referencia = []
        max_pd_ponderada=ponderada.max()
        min_pd_ponderada=ponderada.min()
        max_ponderada=np.array(max_pd_ponderada)
        min_ponderada=np.array(min_pd_ponderada)
        for i in range(numero_criterios):
            if id_criterio[i] in 'lL':
                valor = max_pd_ponderada[i]
            else:
                valor = min_pd_ponderada[i]
            valor_referencia.append(valor)

        ####################################### MATRIZ COM VERIFICAÇÂO DE VALOR ABSOLUTO #################################

        # pega a matriz poderada verificar se é de criterio ou lucro
        # diminuir na matriz ponderada

        matriz_valor_abs = []

        valor_total_t = []
        valor = 0
        for C in range(numero_criterios):
            valor_cri_abs = []
            for L in range(numero_alternativas):
                if id_criterio[C] in ('l', 'L'):
                    valor = valor_referencia[C] - ponderada_matriz[L][C]
                else:
                    if id_criterio[C] in ('c', 'C'):
                        valor = ponderada_matriz[L][C] - valor_referencia[C]
                valor_cri_abs.append(valor)
            valor_total_t.append(valor_cri_abs)  
        matriz_valor_abs=np.transpose(valor_total_t)
        d= pd.DataFrame(matriz_valor_abs, index=lista_alternativas, columns=lista_criterios)
        #d - LINHA PARA IMPRIMIR A MATRIZ DE VERIFICAÇÃO COM VALOR ABSOLUTO

        #################################### Matriz Ordenação ############################

        #retirar o maior valor de cada linha
        matriz_ord = []
        d=pd.DataFrame(matriz_valor_abs, index=lista_alternativas, columns=lista_criterios)

        matriz_ord = d.max(axis=1)
    
        y=['Ordenação de Tchebycheff Min-Max']

        matriz_ord1 = pd.DataFrame(matriz_ord, columns=y)
        matriz_ord_tch = matriz_ord1.sort_values(by=y, ascending = True)
    
    #===============================================================================================
    #===============================================================================================
    #===============================================================================================
                                # 3NAG
    #===============================================================================================
    #===============================================================================================
    #===============================================================================================

        #display(HTML('<h2>INÍCIO DO PROCESSO QUE CONSIDERA A SEGUNDA EQUAÇÃO DE NORMALIZAÇÃO </h2>'))
        
        ########################### Distância absoluta primeira ordenação - Moora menos Tchebycheff #####################################

        dist_abs_1ord = somatorio - matriz_ord
        dataframe_dis_abs_1ord = pd.DataFrame(dist_abs_1ord, index = lista_alternativas, columns = ['Ordenação Absoluta Normalização 1']) 

        ################################################ MOORA > SEGUNDA NORMALIZAÇÂO

        matriz_print = pd.DataFrame(data=matriz, index=lista_alternativas, columns=lista_criterios)
        somatorio_coluna = matriz_print.sum()
    
        ################################################# MATRIZ NORMALIZADA > SEGUNDA NORMALIZAÇÂO
        somatorio_coluna = matriz_print.sum()
        matriz_2normal = matriz_print/somatorio_coluna          

        ########################################## MATRIZ PONDERADA > SEGUNDA NORMALIZAÇÃO

        p = ['Ordenação das alternativas']
        peso_final_pd = pd.DataFrame(peso_final, index=lista_criterios, columns=p)

        matriz_2ponderada = []
        matriz_2ponderada_t = []
        linha_coluna = 0
        for c in range(numero_criterios):
            lista_2pond=[]
            for l in range(numero_alternativas):
                linha_coluna = peso_final[c]*np.array(matriz_2normal)[l][c]
                lista_2pond.append(linha_coluna)
            matriz_2ponderada_t.append(lista_2pond)  
        matriz_2ponderada = np.transpose(matriz_2ponderada_t)

        ponderada_2normal = pd.DataFrame(data = matriz_2ponderada, index = lista_alternativas, columns = lista_criterios)
    
        ################################## PRIMEIRA ORDENAÇÃO DO MOORA  > SEGUNDA NORMALIZAÇÃO
        LUCRO_2n = []
        CUSTO_2n = []
        for L in range(numero_alternativas):
            lista_lucro_2n=[]
            lista_custo_2n=[]
            lucrinho = float(0)
            custinho = float(0)
            for C in range(numero_criterios):
                if id_criterio[C] in ('l', 'L'):
                    lucrinho = matriz_2ponderada[L][C]
                    lista_lucro_2n.append(lucrinho) 
                else:
                    if id_criterio[C] in ('C', 'c'):
                        custinho = matriz_2ponderada[L][C]
                        lista_custo_2n.append(custinho)
            LUCRO_2n.append(lista_lucro_2n)
            CUSTO_2n.append(lista_custo_2n)
    
        lucro_pandas_2n= pd.DataFrame(data=LUCRO_2n, index=lista_alternativas)
        custo_pandas_2n= pd.DataFrame(data=CUSTO_2n, index=lista_alternativas)

        somatorio_2n = lucro_pandas_2n.sum(axis=1) - custo_pandas_2n.sum(axis=1)


        #########################################  PRIMEIRA ORDENAÇÃO DAS ALTERNATIVAS _ 2N > SEGUNDA NORMALIZAÇÃO

        y=['ORDENAÇÃO MOORA - NORMALIZAÇÃO 2']
        somatorio_df_2n= pd.DataFrame(somatorio_2n, index=lista_alternativas, columns=y)

        sort_somatorio_2n = somatorio_df_2n.sort_values(by=['ORDENAÇÃO MOORA - NORMALIZAÇÃO 2'], ascending=False)

        ############## Inicio Segunda Ordenação: Selecionando valores MAX e MIN dos Criterios (TCHEBYCHEFF)> SEGUNDA NORMALIZAÇÃO
        max_ponderada_2n=[]            
        min_ponderada_2n=[]
        valor_referencia_2n = []
        max_pd_ponderada_2n=ponderada_2normal.max()
        min_pd_ponderada_2n=ponderada_2normal.min()
        max_ponderada_2n=np.array(max_pd_ponderada_2n)
        min_ponderada_2n=np.array(min_pd_ponderada_2n)
        for i in range(numero_criterios):
            if id_criterio[i] in 'lL':
                valor = max_pd_ponderada_2n[i]
            else:
                valor = min_pd_ponderada_2n[i]
            valor_referencia_2n.append(valor)
    

        ################### MATRIZ COM VERIFICAÇÂO DE VALOR ABSOLUTO > SEGUNDA NORMALIZAÇÃO
        # pega a matriz ponderada verificar se é de criterio ou lucro
        # diminuir na matriz ponderada

        matriz_valor_abs_2n = []
        valor_total_t_2n = []
        valor = 0
        for C in range(numero_criterios):
            valor_cri_abs_2n = []
            for L in range(numero_alternativas):
                if id_criterio[C] in ('l', 'L'):
                    valor = valor_referencia_2n[C] - matriz_2ponderada[L][C]
                else:
                    if id_criterio[C] in ('c', 'C'):
                        valor = matriz_2ponderada[L][C] - valor_referencia_2n[C]
                valor_cri_abs_2n.append(valor)
            valor_total_t_2n.append(valor_cri_abs_2n)  
        matriz_valor_abs_2n=np.transpose(valor_total_t_2n)
        d= pd.DataFrame(matriz_valor_abs_2n, index=lista_alternativas, columns=lista_criterios)
 
        ####################  MATRIZ ORDENAÇÃO Tchebycheff Min-Max > SEGUNDA NORMALIZAÇÃO
        #retirar o maior valor de cada linha
        tche_matriz_ord_2n = []
        tche_matriz_ord_2n = d.max(axis=1)
        
        y=['Ordenação Tchebycheff Min-Max']

        matriz_ord_2n = pd.DataFrame(tche_matriz_ord_2n, columns=y)

        matriz_ord_tch_2n = matriz_ord_2n.sort_values(by=y, ascending = True)

     
        ########################## Distância absoluta segunda ordenação - Moora menos Tchebycheff
        # Resultado Distancia Absoluta 2N 

        dist_abs_2ord = somatorio_2n - tche_matriz_ord_2n
        dataframe_dis_abs_2ord = pd.DataFrame(dist_abs_2ord, index = lista_alternativas, columns = ['Ordenação Absoluta Normalização 2']) 

        ############################### INÍCIO  > TERCEIRA NORMALIZAÇÃO #################################
        ############################### MATRIZ DE DECISÃO
        matriz_print = pd.DataFrame(data=matriz, index=lista_alternativas, columns=lista_criterios)
        somatorio_coluna = matriz_print.sum()

        #######################################  Valor máximo - matriz de decisão ###################################
        max_decisao_3n=[]            
        valor_maximo_3n = []
        max_pd_decisao_3n=matriz_print.max()
        
        max_decisao_3n=np.array(max_pd_decisao_3n)
        for i in range(numero_criterios):
            if id_criterio[i] in 'lL' or 'cC':
                valor = max_pd_decisao_3n[i]
            valor_maximo_3n.append(valor)
    
        ################################### Terceira normalização ##################################
        #'<h2>INÍCIO DO PROCESSO QUE CONSIDERA A TERCEIRA EQUAÇÃO DE NORMALIZAÇÃO </h2>'))
        
        matriz_3normal = matriz_print/valor_maximo_3n

        ####################################### Matriz ponderada - terceira normalização #############################

        p = ['Ordenação das alternativas']
        peso_final_pd = pd.DataFrame(peso_final, index=lista_criterios, columns=p)
    
        matriz_3ponderada = []
        matriz_3ponderada_t = []
        linha_coluna = 0
        for c in range(numero_criterios):
            lista_3pond=[]
            for l in range(numero_alternativas):
                linha_coluna = peso_final[c]*np.array(matriz_3normal)[l][c]
                lista_3pond.append(linha_coluna)
            matriz_3ponderada_t.append(lista_3pond)  
        matriz_3ponderada = np.transpose(matriz_3ponderada_t)

        ponderada_3normal = pd.DataFrame(data = matriz_3ponderada, index = lista_alternativas, columns = lista_criterios)
 
        #########################################  Primeira ordenação (moora) - Terceira normalização ####################################
        LUCRO_3n = []
        CUSTO_3n = []
        for L in range(numero_alternativas):
            lista_lucro_3n=[]
            lista_custo_3n=[]
            lucrinho = float(0)
            custinho = float(0)
            for C in range(numero_criterios):
                if id_criterio[C] in ('l', 'L'):
                    lucrinho = matriz_3ponderada[L][C]
                    lista_lucro_3n.append(lucrinho) 
                else:
                    if id_criterio[C] in ('C', 'c'):
                        custinho = matriz_3ponderada[L][C]
                        lista_custo_3n.append(custinho)
            LUCRO_3n.append(lista_lucro_3n)
            CUSTO_3n.append(lista_custo_3n)

        lucro_pandas_3n= pd.DataFrame(data=LUCRO_3n, index=lista_alternativas)
        custo_pandas_3n= pd.DataFrame(data=CUSTO_3n, index=lista_alternativas)

        somatorio_3n = lucro_pandas_3n.sum(axis=1) - custo_pandas_3n.sum(axis=1)

        ##################################### Tabela de resultados - primeira ordenação (moora) - terceira normalização ####################
        y=['ORDENAÇÃO MOORA - NORMALIZAÇÃO 3']
        somatorio_df_3n= pd.DataFrame(somatorio_3n, index=lista_alternativas, columns=y)

        sort_somatorio_3n = somatorio_df_3n.sort_values(by=['ORDENAÇÃO MOORA - NORMALIZAÇÃO 3'], ascending=False)

        #####################################  Início da segunda ordenação - terceira normalização (Thebycheff) ###############################
        ##################################### Verificando os valores máximos e mínimos ###################################
        max_ponderada_3n=[]            
        min_ponderada_3n=[]
        valor_referencia_3n = []
        max_pd_ponderada_3n=ponderada_3normal.max()
        min_pd_ponderada_3n=ponderada_3normal.min()
        max_ponderada_3n=np.array(max_pd_ponderada_3n)
        min_ponderada_3n=np.array(min_pd_ponderada_3n)
        for i in range(numero_criterios):
            if id_criterio[i] in 'lL':
                valor = max_pd_ponderada_3n[i]
            else:
                valor = min_pd_ponderada_3n[i]
            valor_referencia_3n.append(valor)
      
       #################################   Verificação de valor absoluto - terceira normalização #################################
       # pega a matriz ponderada verificar se é de criterio ou lucro
       # diminuir na matriz ponderada

        matriz_valor_abs_3n = []
        valor_total_t_3n = []
        valor = 0
        for C in range(numero_criterios):
            valor_cri_abs_3n = []
            for L in range(numero_alternativas):
                if id_criterio[C] in ('l', 'L'):
                    valor = valor_referencia_3n[C] - matriz_3ponderada[L][C]
                else:
                    if id_criterio[C] in ('c', 'C'):
                        valor = matriz_3ponderada[L][C] - valor_referencia_3n[C]
                valor_cri_abs_3n.append(valor)
            valor_total_t_3n.append(valor_cri_abs_3n)  
        matriz_valor_abs_3n=np.transpose(valor_total_t_3n)
        d= pd.DataFrame(matriz_valor_abs_3n, index=lista_alternativas, columns=lista_criterios)
    
       ########################################## Ordenação Tchebycheff Min-Max - terceira normalização #####################################
        #retirar o maior valor de cada linha
        tche_matriz_ord_3n = []
        tche_matriz_ord_3n = d.max(axis=1)

        y=['Ordenação Tchebycheff Min-Max']

        matriz_ord_3n = pd.DataFrame(tche_matriz_ord_3n, columns=y)
        matriz_ord_tch_3n = matriz_ord_3n.sort_values(by=y, ascending = True)
        
        ################################ Distância absoluta terceira ordenação - Moora menos Tchebycheff ###########################################3
        # Resultado Distancia Absoluta 3N 
        dist_abs_3ord = somatorio_3n - tche_matriz_ord_3n
        
        dataframe_dis_abs_3ord = pd.DataFrame(dist_abs_3ord, index = lista_alternativas, columns = ['Ordenação Absoluta Normalização 3']) 
    
        ###################################### ÚLTIMA ETAPA DO SM-3NAG ###################################
        ############# Distancia Absoluta Global ############################
       
        dist_abs_glo = dist_abs_1ord + dist_abs_2ord + dist_abs_3ord
        Ç = pd.DataFrame(dist_abs_glo, index = lista_alternativas, columns = ['Ordenação Global'])
        dist_abs_glo_pd = Ç.sort_values(by=['Ordenação Global'], ascending = False)
    
        ############################################ GRÁFICO DAS ORDENAÇÕES GLOBAIS ###############################
        dados_grafico2 = dist_abs_glo
        altura = [] # valor que está no eixo x
        for i in dados_grafico2:
            altura.append(i)
        posicao = []
        for i in range(0,10,1): 
            posicao.append(i)

        L = ['Valores']
        x = lista_alternativas
        y = dados_grafico2
        df_global = pd.DataFrame(data = y, index = x, columns = L)
    
        fig_global, ax = plt.subplots(figsize=(8,6))
        
        #criando o gráfico de barras horizontais
        ax = sns.barplot(y=df_global.index, x=df_global['Valores'], ax=ax, palette='GnBu_r') #Para inverter a ordem das cores basta você substituir o sufixo " d " de " GnBu_d " pelo sufixo " r ", ficando então " GnBu_r ".
        #barplot
        #YlOrRd
        #PuBu
        #YlGn
        #GnBu


        #link para ver cores do gráfico: https://chrisalbon.com/code/python/data_visualization/seaborn_color_palettes/

        ax.set_facecolor("white") #colocando um fundo branco no gráfico
        ax.set_title("Gráfico da Ordenação Absoluta Global", fontdict={'fontsize':15}) #adicionando título
        ax.set_ylabel('Alternativas', fontdict={'fontsize':14}) #mudando tamanho do label eixo y
        ax.tick_params(labelsize=14) #mudando tamanho dos labels dos ticks
        ax.spines['bottom'].set_linewidth(2.5) #aumentando espessura linha inferior
        
        for axis in ['top', 'right', 'left']: #remoção dos outros três axis
            ax.spines[axis].set_color(None)

        ax.tick_params(axis='x', labelleft=False, left=None) #remoção dos ticks
        
        #colocando rótulo no gráfico
        rotulo_grafico2 = dados_grafico2 
        for index, value in enumerate(rotulo_grafico2): 
            plt.text(value, index, 
                    str(round(value,4)))

        #otimizar espaço da figure
        fig_global.tight_layout()


#===============================================================================================
#===============================================================================================
#===============================================================================================
                               # Organização 
#===============================================================================================
#===============================================================================================
#===============================================================================================

        '''
        ## Resultados:
        '''
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Peso dos Critérios", 
                                        "🔍 Tabelas", 
                                        "📈 Gráficos dos resultados", 
                                        "💻 Resultado Global"])

#tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
#data = np.random.randn(10, 1)

#st.header("A cat")

#tab1.subheader("A tab with a chart")
#tab1.line_chart(data)

#tab2.subheader("A tab with the data")
#tab2.write(data)

        with tab1:
            '''### Nessa página é apresentado os valores dos pesos e seu respectivo grafico.''' 
            st.write('Obs.:')
            st.write('Caso deseje guardar a imagem do gráfico, apenas click nos tres pontos ao lado e acesse a o item download.')
            st.write('Valores dos Pesos:', tabela4)
            #st.bar_chart(df_swara)
            st.pyplot(fig_swara)

        with tab2:
            '''### Nessa página é apresentado as Tabelas do método para cada Normalização.
            '''
            #''' #### Normalização 1 '''
            tab2.subheader("Normalização 1")
            st.write('Matriz de Decisão', matriz_print)
            st.write('Matriz Normalizada 1', m_normalizada)
            st.write('Matriz Ponderada 1', ponderada)
            st.write('Ordenação Moora 1', sort_somatorio)
            st.write('Ordenação Tchebycheff Min-Max 1', matriz_ord_tch)
            st.write('Ordenação Absoluta Normalização 1', dataframe_dis_abs_1ord)
            st.write('')
            #''' #### 3NAG - Normalização 2'''
            tab2.subheader("3NAG - Normalização 2")
            st.write('Matriz Normalizada - Normalização 2', matriz_2normal)
            st.write('Matriz Ponderada - Normalização 2', ponderada_2normal)
            st.write('Ordenação MOORA - Normalizada 2', sort_somatorio_2n)         
            st.write('Ordenação Tchebycheff Min-Max - Normalização 2', matriz_ord_tch_2n)
            st.write('Ordenação Absoluta Normalização 2', dataframe_dis_abs_2ord)
            st.write('')

            #'''#### 3NAG - Normalização 3 '''
            tab2.subheader("3NAG - Normalização 3")
            st.write('Matriz Normalizada - Normalização 3', matriz_3normal)
            st.write('Matriz Ponderada - Normalização 3', ponderada_3normal)
            st.write('Ordenação MOORA - Normalizada 3', sort_somatorio_3n)         
            st.write('Ordenação Tchebycheff Min-Max - Normalização 3', matriz_ord_tch_3n)
            st.write('Ordenação Absoluta Normalização 3', dataframe_dis_abs_3ord)
            
        with tab3:
            st.write('Gráfico da Ordenação Absoluta Global')
            st.pyplot(fig_global)
            st.write('Valores dos Pesos')
            st.pyplot(fig_swara)
                   
        with tab4:
            tab4.subheader("Ordenação Absoluta Global")
            st.write(dist_abs_glo_pd)
            st.pyplot(fig_global)
            st.write('Obs.:')
            st.write('Para baixar o Gráfico, basta clicar no Botão "Download Gráfico".')
            #with open(st.pyplot(fig_global), "rb") as file:
                #btn = st.download_button(
                #                        label="Download Gráfico",
                #                        data=st.pyplot(fig_global),
                #                        file_name="Ordenação Absoluta Global.png",
                #                        mime="image/png"
                #                        )
            st.balloons()

    
if pagina == 'Sobre':
    ''' #### Para melhor entendimento foi elaborado um framework para aplicação do método SWARA-MOORA-3NAG, sendo demonstrado da seguinte forma:
          
    1. Entendimento e análise do problema;
    2. Levantamento dos dados qualitativos ou quantitativos;
    3. Estruturação e arrumação dos dados coletados;
    4. Utilização do método SWARA para cálculo dos pesos (pode ser aplicado para mais de um decisor);
    5. Utilizar o método MOORA considerando os pesos gerados pelo SWARA;
    6. Calcular a ordenação do MOORA
    7. Calcular a ordenação de Tchebycheff
    8. Calcular a ordenação absoluta na primeira normalização;
    9. Utilizar a mesma matriz de decisão aplicada inicialmente no método MOORA para realizar a segunda normalização (aij / ∑ aij);
    10. Calcular a ordenação do MOORA;
    11. Calcular a ordenação de Tchebycheff
    12. Calcular a ordenação absoluta na segunda normalização;
    13. Utilizar a mesma matriz de decisão aplicada inicialmente no método MOORA para realizar a terceira normalização (aij / max aij);
    14. Calcular a ordenação do MOORA;
    15. Calcular a ordenação de Tchebycheff;
    16. Calcular a ordenação absoluta na terceira normalização;
    17. Realizar o somatório das ordenações absolutas 1, 2 e 3 para se obter a ordenação absoluta global (OAG);
    18. Ordenar de forma decrescente, ou seja, os maiores valores obtidos serão considerados como as melhores opções.
'''

if pagina == 'Autores':
    ''' ## Os desenvolvedores do Site são:'''
    st.write('')
    st.markdown('#### ✔️ Lucas Ramon dos Santos Hermogenes')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/9679408116975910)")
    st.markdown("🖥️ [Researchgate](https://www.researchgate.net/profile/Lucas-Ramon-Dos-Santos-Hermogenes)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/lramon/)")

    st.markdown('#### ✔️ Isaque David Pereira de Almeida')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/4334402971349874)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Isaque-Almeida)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/isaque-d-4954ba1b1/)")

    st.markdown('#### ✔️ Prof. DSc. Marcos dos Santos')
    st.markdown("📜 [Currículo Lattes](httnal)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Marcos-Santos-85)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/profmarcosdossantos/)")
    st.markdown("Casa da Pesquisa Operacional - [YouTube](https://www.youtube.com/c/CasadaPesquisaOperacional)")

    st.markdown('#### ✔️ Prof. DSc. Carlos Francisco Simões Gomes')
    st.markdown("📜 [Currículo Lattes](http://lattes.cnpq.br/7509084995553647)")
    st.markdown("🖥️ [Researshgate](https://www.researchgate.net/profile/Carlos-Francisco-Gomes)")
    st.markdown("💻 [Linkedin](https://www.linkedin.com/in/carlos-francisco-sim%C3%B5es-gomes-7284a3b/)")


st.write('')
st.image('imagem rodape.jpeg', caption='Para Citar: Hermogenes, Lucas Ramon dos Santos; Almeida, Isaque David Pereira; Gomes, Carlos Francisco Simões.; Santos, Marcos dos. \nSWARA-MOORA-3NAG (SM-3NAG) For Decision Making (v1), Universidade Federal Fluminense, Niterói, Rio de Janeiro, 2022.')
