from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def parse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    forms = soup.find_all("form")
    forms_info = []
    for form in forms:
        form_info = form.attrs
        form_info["action"] = url if form_info.get("action") is None else urljoin(url, form_info.get("action"))
        input_fields = form.find_all('input')
        form_info["input_fields"] = []
        for input_el in input_fields:
            input_info = {"name": "" if input_el.attrs.get("name") is None else input_el.attrs.get("name"),
                          "value": "" if input_el.attrs.get("value") is None else input_el.attrs.get("value")}
            form_info.get("input_fields").append(input_info)
        forms_info.append(form_info)
    return forms_info
