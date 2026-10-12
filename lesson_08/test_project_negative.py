from project_page import ProjectApi
from faker import Faker

fake = Faker("ru_RU")

api = ProjectApi("https://ru.yougile.com")


#  1. Создать новый проект с пустым названием
def test_create_project_negative_empty_title():
    # получить количество проектов до создания нового проекта
    resp_before = api.get_project_list()
    assert resp_before.status_code == 200
    projects_list_before = resp_before.json().get("content", [])
    len_before = len(projects_list_before)

    # создать новый проект с пустым названием
    new_project = api.create_project_empty_title()

    # проверить, что сервер выдал ошибку на создание пустого проекта
    assert new_project.status_code == 400
    assert "title should not be empty" in new_project.json().get("message")

    # проверить количество проектов после создания нового проекта
    resp_after = api.get_project_list()
    assert resp_after.status_code == 200
    projects_list_after = resp_after.json().get("content", [])
    len_after = len(projects_list_after)

    # проверить, что количество проектов не увеличилось
    assert len_after == len_before


#  2. Получить проект по несуществующему id
def test_get_project_by_fake_id():
    # сгенерировать случайный id проекта
    fake_id = fake.uuid4()

    # получить проект по id
    get_project = api.get_project_by_fake_id(fake_id)

    # проверить,что сервер выдал ошибку запроса
    assert get_project.status_code == 404
    assert get_project.json().get("message") == "Проект не найден"


#  3. Изменить название проекта на пустое
def test_edit_project_empty_title_negative(project_cleanup):
    # создать проект и получить его id
    project_before = api.create_project()
    assert project_before.status_code == 201
    project_id = project_before.json().get("id")

    # передать id созданного проекта в фикстуру для удаления после теста
    project_cleanup["id"] = project_id

    # изменить название проекта на пустое
    edit_response = api.edit_remote_project(project_id, body={"title": ""})

    # проверить, что сервер выдал ошибку
    assert edit_response.status_code == 400
    assert "title should not be empty" in edit_response.json().get("message")
