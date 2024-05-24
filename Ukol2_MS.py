# Úkol 2 🐱 🐈

import requests
import json

facts_count = 10
timeout_seconds = 0.1

try:
    data = requests.get(f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={facts_count}',timeout=timeout_seconds)

    data = data.json()
    fact_list = []
    for one in data:
        fact_list.append(one["text"])

    # print(fact_list)
    # print(len(fact_list))

    if len(fact_list) != facts_count:
        print('Warning, not enough facts retrieved.')

    number_list = list(range(1,facts_count+1))

    # print(number_list)

    numbered_facts = []
    for value in number_list:
        numbered_facts.append(str(value) + ' ' + fact_list[value-1])

    print(numbered_facts)

    with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
        json.dump(numbered_facts, output_file, indent=4, sort_keys=True, ensure_ascii=False)

except requests.ConnectionError:
    print('ConnectTimeout - you have to increase timeout')


# Obsahu súboru by mal po prebehnutí programu vyzerať takto:

# [
#     "1. Owning a cat can reduce the risk of stroke and heart attack by a third.",
#     "2. Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
#     "3. Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.",
#     "4. The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
#     "5. Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.",
#     "6. Owning a cat can reduce the risk of stroke and heart attack by a third.",
#     "7. Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
#     "8. Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.",
#     "9. The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
#     "10. Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs."
# ]

