from sqlalchemy import select
from app.models import Recipe

def test_create_recipe(session):
    new_recipe = Recipe(
        nome='Arroz colorido',
        ingredientes=["3 colheres (sopa) raladas de Cenoura crua", "2 colheres (sopa) de Cheiro verde"],
        instrucoes=['Pique o cheiro verde, o tomate em cubos e a vagem em pedaços pequenos e reserve. Em uma panela antiaderente, aqueça o azeite e doure o alho picado e a cebola em cubos. Acrescente todos os legumes e refogue bem. Adicione o arroz cozido e misture bem por cerca de 5 minutos. Sirva em seguida.'],
        informacao_nutricional={
            'gramas_por_porcao': '162 g',
            'calorias': '152,52 kcal',
            'carboidratos': '27,40 g',
            'proteinas': '4,04 g',
            'gorduras_totais': '3,24 g',
            'gord_saturadas': '0,52 g',
            'gord_trans': '0,00 g',
            'fibras': '4,52 g',
            'sodio': '82,76 mg'
        },
        categoria='Vegetariano'
    )
    session.add(new_recipe)
    session.commit()

    recipe = session.scalar(select(Recipe).where(Recipe.name == 'Arroz colorido'))

    assert recipe.name == 'Arroz colorido'
    assert recipe.ingredients == new_recipe.ingredients
    assert recipe.instructions == new_recipe.instructions
    assert recipe.nutritional_info == new_recipe.nutritional_info
    assert recipe.category == new_recipe.category