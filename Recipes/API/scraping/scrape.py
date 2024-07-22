import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph, OmniScraperGraph
from scrapegraphai.utils import prettify_exec_info
import pandas as pd
import requests
import json

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

graph_config = {
    "llm": {
        "api_key": OPENAI_KEY,
        "model": "gpt-4o-mini",
    },
    "headless": False,
}

def get_recipes_from_page(page_url):
    smart_scraper_graph = SmartScraperGraph(
        prompt=(
            f"Extraia as informações da receita contidas nos campos 'Ingredientes de: **Nomedareceita**', "
            f"'Como fazer **Nomedareceita**:' e 'Informações Nutricionais de **Nomedareceita**'."
            f"O JSON de saída deve conter os campos 'nome Str', 'ingredientes List(Str)', 'modo_preparo List(Str)', 'informacao_nutricional Dict', e 'categoria Str'."
        ),
        source=page_url,
        config=graph_config
    )
    result = smart_scraper_graph.run()
    return result

def post_recipe_to_api(recipe_data):
    api_url = 'http://localhost:8000/recipes/'
    try:
        response = requests.post(api_url, json=recipe_data)
        response.raise_for_status()  # Vai levantar um erro para respostas 4xx e 5xx
        return response.status_code, response.json()
    except requests.RequestException as e:
        return 400, {"error": str(e)}

def update_link_status(filename, index):
    df = pd.read_csv(filename)
    df.at[index-1, 'Status'] = 'Processado'
    df.to_csv(filename, index=False)

df = pd.read_csv('recipe_links.csv', names=['URL', 'Status'])

processed_count = 0
for index, row in df.iterrows():
    if row['Status'] == 'Nao Processado':
        page_url = row['URL']
        try:
            recipe_data = get_recipes_from_page(page_url)
            if recipe_data:
                status_code, response = post_recipe_to_api(recipe_data)
                if status_code == 200:
                    print(f"Receita de {page_url} adicionada com sucesso.")
                    update_link_status('recipe_links.csv', index)
                    processed_count += 1
                else:
                    print(f"Erro ao adicionar receita de {page_url}: {response}")
        except Exception as e:
            print(f"Erro ao processar a página {page_url}: {str(e)}")

        if processed_count >= 100:
                print("Limite de 20 receitas processadas alcançado.")
                break  # Sai do loop
