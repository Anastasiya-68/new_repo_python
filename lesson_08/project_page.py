from faker import Faker
import requests
from config import YOUGILE_TOKEN

fake = Faker("ru_RU")


class ProjectApi:
    def __init__(self, url, token=YOUGILE_TOKEN):
        self.url = url
        self.token = token

    # 1. Метод получения списка проектов
    def get_project_list(self):
        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(self.url + "/api-v2/projects", headers=my_headers)
        return resp.json()

    # 2. Метод создания проекта
    def create_project(self):
        title = fake.catch_phrase()
        new_project = {"title": title}

        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.post(
            self.url + "/api-v2/projects", json=new_project, headers=my_headers
            )
        return resp.json()

    # 2. Метод создания проекта с пустым названием (негативная проверка)
    def create_project_empty_title(self):

        title = ""
        new_project = {"title": title}

        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.post(
            self.url + "/api-v2/projects", json=new_project, headers=my_headers
            )
        return resp

    # 3. Метод получения проекта по id
    def get_project_by_id(self, project_id):

        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(
            self.url + "/api-v2/projects/" + str(
                project_id), headers=my_headers
            )
        return resp.json()

    # 4. Метод получения проекта по несуществующему id (негативная проверка)
    def get_project_by_fake_id(self, project_id):
        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(
            self.url + "/api-v2/projects/" + str(
                project_id), headers=my_headers
            )
        return resp

    # 4. Метод изменения проекта
    def edit_project(self, project_id, new_title):

        new_project = {"title": new_title}

        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.put(
            self.url + "/api-v2/projects/" + str(
                project_id), json=new_project, headers=my_headers
            )
        return resp.json()

    # 4. Метод изменения удаленного проекта
    def edit_remote_project(self, project_id, body):

        my_headers = {}
        my_headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.put(self.url + "/api-v2/projects/" + str(
            project_id), json=body, headers=my_headers)
        return resp
