import os 

WEATHER_OPTIONS = {'1' : 'Quente', '2' : 'Frio'}
LANDSCAPE_OPTIONS = {'1': 'Com paisagens naturais', '2': 'Com paisagens urbanas'}
NIVEIS_ORCAMENTO = {
    "a até 1000R$": 1,
    "a até 5000R$": 2,
    "acima de 5000R$": 3
}

def load_data():
    return [
    {
        "place": "Rio de Janeiro",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Piauí",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 1000R$"
    },
    {
        "place": "São Paulo",
        "weather": "Frio",
        "type_landscape": "Com paisagens urbanas",
        "budget": "acima de 5000R$"
    },
    {
        "place": "Salvador",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Fortaleza",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 1000R$"
    },
    {
        "place": "Florianópolis",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 5000R$"
    },
    {
        "place": "Manaus",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 1000R$"
    },
    {
        "place": "Curitiba",
        "weather": "Frio",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Recife",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Belo Horizonte",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Porto Alegre",
        "weather": "Frio",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 5000R$"
    },
    {
        "place": "Brasília",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "acima de 5000R$"
    },
    {
        "place": "Gramado",
        "weather": "Frio",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 5000R$"
    },
    {
        "place": "Natal",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 3000R$"
    },
    {
        "place": "Foz do Iguaçu",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 5000R$"
    },
    {
        "place": "Campos do Jordão",
        "weather": "Frio",
        "type_landscape": "Com paisagens naturais",
        "budget": "acima de 5000R$"
    },
    {
        "place": "Lençóis Maranhenses",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 3000R$"
    },
    {
        "place": "Bonito",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "acima de 5000R$"
    },
    {
        "place": "Ouro Preto",
        "weather": "Frio",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 3000R$"
    },
    {
        "place": "Chapada dos Veadeiros",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 3000R$"
    },
    {
        "place": "Jericoacoara",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 5000R$"
    },
    {
        "place": "Paraty",
        "weather": "Quente",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 3000R$"
    },
    {
        "place": "Ilhabela",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 3000R$"
    },
    {
        "place": "Búzios",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "acima de 5000R$"
    },
    {
        "place": "Petrópolis",
        "weather": "Frio",
        "type_landscape": "Com paisagens urbanas",
        "budget": "a até 3000R$"
    },
    {
        "place": "Maceió",
        "weather": "Quente",
        "type_landscape": "Com paisagens naturais",
        "budget": "a até 3000R$"
    }
]


def clear():
        os.system("cls" if os.name == "nt" else "clear")

def show_apresentation() -> None:
    clear()
    print("Bem vindo ao nosso sistema de recomendação de viagems!")
    print("Responda as seguintes perguntas para recomedamamos a melhores opções de viagem para você!\n")

def get_menu_choice(prompt : str, options: dict[str, str]) -> str:
    while True:
        print(f"\n{prompt}")
        for key, value in options.items():
            print(f'{key}. {value}')
        option = input("Escolha a opção: ") 
        if option in options:
            return options[option]
        clear()
        print(f"Opção inválida! Por favor, escolha um dos números disponíveis ({', '.join(options.keys())}).")

def classify_travel_budget() -> str:
    while True:
         try:
            input_value = float(input("\nQual é o seu orçamento disponível para a viagem em reais: "))
            break
         except ValueError:
             print("Valor inválido! Digite apenas números, por favor.")

    if input_value <= 1000:
        return "a até 1000R$"
    elif input_value <= 5000:
        return "a até 5000R$"
    else:
        return "acima de 5000R$"

def get_user_preferences() -> dict:
    type_weather = get_menu_choice("Você prefere qual tipo de clima?", WEATHER_OPTIONS)
    location_type = get_menu_choice("Você prefere qual tipo de lugar?", LANDSCAPE_OPTIONS)
    budget = classify_travel_budget()

    return {
        'weather' : type_weather, 
        'location' : location_type, 
        'budget' : budget, 
    }

def filter_recommendations(data: list, preferences: dict) -> dict:
    recommendations_of_places = {
        'exact_budget' : [],
        'others_budget' : [],
        }
    user_budget_level = NIVEIS_ORCAMENTO[preferences["budget"]]

    for item in data:
        item_budget_level_in_data = NIVEIS_ORCAMENTO.get(item['budget'])
        if item_budget_level_in_data is None:
            continue

        match_weather = item["weather"] == preferences["weather"]
        match_location = item["type_landscape"] == preferences["location"]
        match_budget = item_budget_level_in_data <= user_budget_level

        if match_weather and match_location and match_budget:
            Local_place = item.get('place')
            if item_budget_level_in_data == user_budget_level:
                recommendations_of_places['exact_budget'].append(Local_place)
            else:
                recommendations_of_places["others_budget"].append((Local_place, item['budget']))

    return recommendations_of_places

def display_results(recommendations: dict, preferences: dict) -> None:
    clear()
    
    exact_places = recommendations["exact_budget"]
    other_places = recommendations["others_budget"]

    if not exact_places and not other_places:
        print("Desculpe, não encontramos destinos com essas características.")
        input("Aperte qualquer tecla para continuar...")
        return
    
    if exact_places:
        print("De acordo com as suas escolha(s), o(s) estado(s) recomendado(s) foram os seguintes:")
        for place in exact_places:
            print(f"- {place}")
        
        print(f"\nJustificativa: Clima {preferences["weather"].lower()}, {preferences["location"]} e orçamento de {preferences['budget']}.")

        if other_places:
            print(f"\nA seguir tem outros lugares que estão abaixo do seu orçamento de {preferences['budget']}, caso esteja interessado em visitar:\n")
            for place, budget in other_places:
                print(f"- {place} (orçamento: {budget})")

def main():
    show_apresentation()

    preferences = get_user_preferences()

    data = load_data()

    recommendations = filter_recommendations(data, preferences)

    display_results(recommendations, preferences)    

if __name__ == "__main__":
    main()