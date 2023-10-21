
-----------------------------------------------------------------------------------------------------1
from google.colab import files
import io
----------------------------------------------------------------------------------------------------- 2
uploaded = files.upload()
file_name = next(iter(uploaded))
file_name
------------------------------------------------------------------------------------------------------ 3
import pandas as pd
gfile_name = io.StringIO(uploaded[file_name].decode('ISO 8859-1').strip())
df = pd.read_csv(gfile_name)
df
------------------------------------------------------------------------------------------------------ 4
colunas_texto = ['Nome', 'Idade', 'Cor', 'Salario']

df['Texto'] = df.apply(lambda row: f"{row['Nome']} tem {row['Idade']} anos, sua cor favorita é {row['Cor']} e tem um salário de {row['Salario']} reais.", axis=1)

texto_completo = '\n'.join(df['Texto'])

with open('texto_gerado.txt', 'w') as file:
    file.write(texto_completo)

print(texto_completo)
---------------------------------------------------------------------------------------------------- 5

import os

print(os.getcwd())


1 - Importação de bibliotecas do google colab.
2 -Importação de um arquivo CSV.
3 - Importação Biblioteca Python com arquivo formatado para ler CSV.
4 - Transformação dos dados em tabela para o formato de texto, concatenando os registros,
no caso de Ciências de Dados seria a parte em que transformamos dados em informação, dando sentido.
5 - Download do arquivo transformado.

########################## IMPORTANTE ################################
# Foi utilizado o google colab pra desenvolver esse pequeno processo.  #
########################## IMPORTANTE ################################