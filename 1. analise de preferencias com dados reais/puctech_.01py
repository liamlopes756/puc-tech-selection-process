import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#carregamento dos dados
url="https://raw.githubusercontent.com/puc-tech/challenge/refs/heads/main/student_preferences_extended.csv"
df = pd.read_csv(url) #df data frame
#print(df.columns.tolist())
#pd.set_option('display.max_columns',None)
#print(df) #500 rows x 24 colums

#limpeza
#remover colunas irrelevantes
cols_irrelevantes=["comentario"]
df = df.drop(columns=cols_irrelevantes)
#remover linhas com valores nulos
df= df.dropna(subset=["linguagem_preferida","horario_estudo","formato_conteudo_principal"])

#analise
#faz a contagem dos dados
respostas_por_linguagem=df["linguagem_preferida"].value_counts()                    #linguagem preferida
pct_horario=df["horario_estudo"].value_counts(normalize=True)*100       #horario de estudo percentual
formato_top=df["formato_conteudo_principal"].value_counts()            #formatos preferidos


#visualizações

#gráfico 1: barras do total de respostas por linguagem
plt.figure(figsize=(8, 5))
sns.barplot(
    x=respostas_por_linguagem.index, 
    y=respostas_por_linguagem.values
)
plt.title("Total de Respostas por Linguagem")  # barras destacam comparativamente quais linguagens são mais populares
plt.xlabel("Linguagem Preferida")
plt.ylabel("Número de Respostas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# gráfico 2: pizza do percentual de preferência por horário de estudo
plt.figure(figsize=(6, 6))
plt.pie(
    pct_horario.values, 
    labels=pct_horario.index, 
    autopct="%.1f%%", 
    startangle=90
)
plt.title("Percentual de Preferência por Horário de Estudo")  # gráfico de pizza é adequado para mostrar proporções de um todo
plt.axis("equal")  # garante que a pizza fique redonda
plt.show()


#relatorio final
with open("relatorio_preferencias.txt", "w") as f: #f de file
    f.write("=== Total de Respostas por Linguagem ===\n")
    f.write(respostas_por_linguagem.to_string())

    f.write("\n\n=== Percentual por Horário de Estudo ===\n")
    #f.write(pct_horario.round(1).astype(str) + "%\n")
    pct_texto = (pct_horario
                    .round(1)               # arredonda para 1 casa
                    .map(lambda x: f"{x}%") # adiciona "%" a cada valor
                    .to_string()            # junta tudo em uma única string multi-linha
               )
    f.write(pct_texto + "\n")

    f.write("\n=== Formato de Conteúdo Mais Popular ===\n")
    f.write(formato_top.to_string())
    

