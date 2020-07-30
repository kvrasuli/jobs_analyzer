import requests
from itertools import count
from dotenv import load_dotenv
import os
from aux import print_statistics, predict_rub_salary_sj, predict_rub_salary_hh, get_statistics_by_lang



def get_vacancies_from_hh(popular_languages):
    hh_url = 'https://api.hh.ru/vacancies/'
    hh_headers = {'User-Agent': 'Job analyzer/1.0 (rasulikv@gmail.com)'}
    hh_params = {'period': '30', 'area': '1', 'per_page': '100', 'page': '0'}
    vacancies_by_lang = {language: [] for language in popular_languages}
    for language in popular_languages:
        hh_params['text'] = f'программист {language}'
        for page in count(0):
            hh_params['page'] = f'{page}'
            response = requests.get(hh_url, headers=hh_headers, params=hh_params)
            response.raise_for_status()       
            vacancies_page = response.json()
            vacancies_by_lang[language] += vacancies_page['items']
            # it's not possible to get more than 2000 vacancies
            if page == vacancies_page['pages'] or page == 19:
                break   
    return vacancies_by_lang


def get_vacancies_from_sj(token, popular_languages):
    sj_url = 'https://api.superjob.ru/2.33/vacancies'
    sj_headers = {'X-Api-App-Id': token}
    sj_params = {'period': '7', 'town': 'Москва', 'catalogues': '48', 'keyword': '', 'count': '100'}
    vacancies_by_lang = {language: [] for language in popular_languages}
    for language in popular_languages:
        sj_params['keyword'] = f'{language}'
        for page in count(0): 
            sj_params['page'] = f'{page}'
            response = requests.get(sj_url, headers=sj_headers, params=sj_params)
            response.raise_for_status()  
            vacancies_page = response.json()
            vacancies_by_lang[language] += vacancies_page['objects']
            if page == 5:  # it's not possible to get more than 500 vacancies 
                break
    return vacancies_by_lang


def main():
    popular_languages = ['Python', 'JavaScript', 'Java', 'Swift', 'Go', 'C#', 'C++', 'Scala', 'Kotlin', 'Ruby']
    load_dotenv()
    superjob_token = os.getenv('SUPERJOB_TOKEN')
    hh_vacancies = get_vacancies_from_hh(popular_languages)
    sj_vacancies = get_vacancies_from_sj(superjob_token, popular_languages)
    hh_statistics = get_statistics_by_lang(hh_vacancies, predict_rub_salary_hh, popular_languages)
    sj_statistics = get_statistics_by_lang(sj_vacancies, predict_rub_salary_sj, popular_languages)
    print_statistics(hh_statistics, 'HeadHunter Moscow')
    print_statistics(sj_statistics, 'SuperJob Moscow')


if __name__ == '__main__':
    main()
