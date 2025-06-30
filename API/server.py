from flask import Flask, render_template, request, jsonify

from selenium import webdriver
from flask_cors import CORS
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os
from time import sleep


# driver = webdriver.Chrome()

# driver.get("https://www.amazon.com.br/s?k=sapato&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=38LJ7ZUFOU604&sprefix=sapa%2Caps%2C220&ref=nb_sb_noss_2")

# html_completo_da_pagina = driver.page_source

# soup = BeautifulSoup(html_completo_da_pagina, 'lxml')

# produtos = soup.find_all('div', class_='product-item')
# for produto in produtos:
#     nome = produto.find('h2').text
#     preco = produto.find('span', class_='price').text
#     print(f"Produto: {nome}, Preço: {preco}")



# # 1- Entrar no site https://www.mercadolivre.com.br/
# driver = webdriver.Chrome()
# driver.get('https://lista.mercadolivre.com.br/calca-jeans')


# sleep(5)

# # 2- Anotar o nome dos produtos
# nomes_produtos = driver.find_elements(By.XPATH, "//a[@class='poly-component__title']")

# # 3- Anotar o preço dos produtos
# precos_produtos = driver.find_elements(By.XPATH, "//span[@class='andes-money-amount andes-money-amount--cents-superscript']")

# # print(nomes_produtos)
# # print(precos_produtos)

# # nome_do_arquivo = "precos.csv"

# produtos = []
# # 4- Criar arquivo CSV
# # with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
# #     arquivo.write('Nome,Preco\n')  

# # 5- Salvar os nomes e preços no arquivo CSV
# for nome, preco in zip(nomes_produtos, precos_produtos):
#     # Limpar o texto do nome e preço, removendo caracteres indesejados
#     nome_limpo = nome.text.strip().replace(',', '') 
#     preco_limpo = preco.text.strip().replace('\n', '') 
#     if nome_limpo and preco_limpo:  
#         produto = {}
#         produto["nome"] = nome_limpo
#         produto["preco"] = preco_limpo
#         produtos.append(produto)
#         # with open(nome_do_arquivo, 'a', encoding='utf-8') as arquivo:
#         #     arquivo.write(f'{nome_limpo}, R$ {preco_limpo}\n')
#         pass

app = Flask(__name__)
CORS(app)

@app.route('/')
def produtos():
    driver = webdriver.Chrome()
    driver.get('https://lista.mercadolivre.com.br/calca-jeans')
    sleep(5)
    # 2- Anotar o nome dos produtos
    nomes_produtos = driver.find_elements(By.XPATH, "//a[@class='poly-component__title']")

    # 3- Anotar o preço dos produtos
    precos_produtos = driver.find_elements(By.XPATH, "//span[@class='andes-money-amount andes-money-amount--cents-superscript']")

    imagens_produtos = driver.find_elements(By.XPATH, "//img[@class='poly-component__picture']")

    # links_produto = driver.find_element(By.CSS_SELECTOR, "a.ui-search-link").get_attribute('href')


    # for imagem in imagens_produtos:
    #     link_imagem = imagem.get_attribute('src')
    #     # print(link_imagem)


    produtos = []
    nome_do_arquivo = "precos.txt"
    # 4- Criar arquivo CSV
    # with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
    #     arquivo.write('Nome,Preco\n')  

    # 5- Salvar os nomes e preços no arquivo CSV
    for nome, preco, imagem in zip(nomes_produtos, precos_produtos, imagens_produtos):
        # Limpar o texto do nome e preço, removendo caracteres indesejados
        nome_limpo = nome.text.strip().replace(',', '') 
        preco_limpo = preco.text.strip().replace('\n', '') 
        if nome_limpo and preco_limpo:  
            produto = {}
            produto["nome"] = nome_limpo
            produto["preco"] = preco_limpo
            produto["imagem_url"] = imagem.get_attribute('src') 
            produto["link_do_produto"] = nome.get_attribute('href')
            produtos.append(produto)
            # with open(nome_do_arquivo, 'a', encoding='utf-8') as arquivo:
            #     arquivo.write(f'{nome_limpo}, R$ {preco_limpo}. link da imagem: {produto["imagem_url"]}. link do produto: {produto["link_do_produto"]}\n')
            # pass



    driver.quit()    





    # produtos = [
    #     {'nome': 'Celular Samsung', 'preco': 'R$ 1.500,00'},
    #     {'nome': 'Notebook Dell', 'preco': 'R$ 3.200,00'},
    #     {'nome': 'Fone Bluetooth', 'preco': 'R$ 200,00'}
    # ]

    # print("--- DADOS ENVIADOS PARA O TEMPLATE ---")
    # print(produtos)
    # print("------------------------------------")

    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)