import requests
from bs4 import BeautifulSoup
import json
import time
import csv
from urllib.parse import urljoin

def get_recipe_links(url, headers):
    time.sleep(1)  # Intervalo entre requisições para evitar sobrecarga no servidor
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair links das receitas do JSON-LD script
    script = soup.find('script', type='application/ld+json')
    data = json.loads(script.string)
    recipe_links = [item['url'] for item in data['itemListElement']]

    # Extrair e corrigir links de paginação
    pagination_links = [urljoin(url, a['href']) for a in soup.select('.pagenav a') if 'p=' in a['href']]
    return recipe_links, pagination_links

def save_links_to_csv(links, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Status'])  # Escreve o cabeçalho do arquivo
        for link in links:
            writer.writerow([link, 'Nao Processado'])  # Escreve cada link com o status inicial

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    category_pages = [
        "https://vitat.com.br/receitas/categoria/2-acompanhamentos",
        "https://vitat.com.br/receitas/categoria/7-bolos",
        "https://vitat.com.br/receitas/categoria/8-carnes",
        "https://vitat.com.br/receitas/categoria/9-doces",
        "https://vitat.com.br/receitas/categoria/13-paes",
        "https://vitat.com.br/receitas/categoria/15-pratos-principais",
        "https://vitat.com.br/receitas/categoria/16-saladas",
        "https://vitat.com.br/receitas/categoria/19-sobremesas"	
    ]
    
    all_recipe_links = []
    for page in category_pages:
        recipe_links, pagination_links = get_recipe_links(page, headers)
        all_recipe_links.extend(recipe_links)
        
        for pagination_link in pagination_links:
            recipe_links, _ = get_recipe_links(pagination_link, headers)
            all_recipe_links.extend(recipe_links)
    
    save_links_to_csv(all_recipe_links, 'recipe_links2.csv')

if __name__ == "__main__":
    main()