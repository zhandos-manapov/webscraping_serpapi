from serpapi import GoogleSearch

params = {
  "q": "",
  "hl": "en",
  "gl": "us",
  "api_key": "api_key"
}

query = input('Enter your question: ')

while query:
    params["q"] = query
    search = GoogleSearch(params)
    results = search.get_dict()

    answer_box = None
    try: 
        if results["answer_box"]["type"] == "calculator_result" or results["answer_box"]["type"] == "currency_converter":
            answer_box = results["answer_box"]["result"]
        elif results["answer_box"]["type"] == "weather_result":
            answer_box = results["answer_box"]["temperature"] + " " + results["answer_box"]["unit"]
        elif results["answer_box"]["type"] == "finance_results":
            answer_box = results["answer_box"]["price"] + " " + results["answer_box"]["currency"]
        elif results["answer_box"]["type"] == "population_result":
            answer_box = results["answer_box"]["population"]
        elif results["answer_box"]["type"] == "dictionary_results":
            answer_box = results["answer_box"]["definitions"]
        elif results["answer_box"]["type"] == "organic_result":
            try:
                answer_box = results["answer_box"]["list"] 
            except:
                try:
                    answer_box = results["answer_box"]["contents"]["table"]
                except:
                    try:
                        answer_box = results["answer_box"]["snippet"]
                    except:
                        answer_box = results["answer_box"]["answer"]

        elif results["answer_box"]["type"] == "translation_result":
            answer_box = results["answer_box"]["target"]["text"]
        elif results["answer_box"]["type"] == "directions":
            answer_box = results["answer_box"]["routes"]["summary"]
        else:
            answer_box = results["answer_box"]["answer"]
    except:
        answer_box = "Couldn't fint any results. Try again. "

    print(answer_box)

    query = input('Enter your question: ')

