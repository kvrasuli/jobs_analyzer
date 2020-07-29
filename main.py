import requests
import pprint
pp = pprint.PrettyPrinter()

url = 'https://api.hh.ru/vacancies/'
headers = {'User-Agent': 'Job analyzer/1.0 (rasulikv@gmail.com)'}
params = {'text': 'программист Москва', 'period': '30'}
# 'only_with_salary': True

popular_languages = ['Python', 'JavaScript', 'Java', 'Swift', 'Go', 'C#', 'C++', 'Scala', 'Kotlin', 'Ruby']
number_of_jobs_by_lang = {}

for language in popular_languages:
    params['text'] = f'программист {language} Москва'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    number_of_jobs = response.json()['found']
    if number_of_jobs > 100:
        number_of_jobs_by_lang[language] = number_of_jobs
pp.pprint(number_of_jobs_by_lang)