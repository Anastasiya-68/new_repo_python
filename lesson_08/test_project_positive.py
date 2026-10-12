from project_page import ProjectApi
from faker import Faker

fake = Faker("ru_RU")

api = ProjectApi("https://ru.yougile.com")


#  1. Создать новый проект
def test_create_new_project(project_cleanup):

    # получить количество проектов до создания нового проекта
    resp_before = api.get_project_list()
    assert resp_before.status_code == 200
    projects_list_before = resp_before.json().get("content", [])
    len_before = len(projects_list_before)

    # создать новый проект
    resp_create = api.create_project()
    assert resp_create.status_code == 201
    new_project = resp_create.json()

    # передать id созданного проекта в фикстуру для удаления после теста
    project_cleanup["id"] = new_project.get("id")

    # проверить количество проектов после создания нового проекта
    resp_after = api.get_project_list()
    assert resp_after.status_code == 200
    projects_list_after = resp_after.json().get("content", [])
    len_after = len(projects_list_after)

    # проверить, что количество проектов увеличилось на 1
    assert len_after - len_before == 1

    # получить id нового проекта
    id_new_project = new_project.get("id")

    # получить id последнего проекта из обновленного списка
    id_last_project = projects_list_after[-1].get("id")

    # проверить, что id последнего проекта и нового проекта совпадают
    assert id_new_project == id_last_project


#  2. Получить проект по id
def test_get_project(project_cleanup):

    # создать проект
    resp_create = api.create_project()
    assert resp_create.status_code == 201
    id_new_project = resp_create.json().get("id")

    # передать id созданного проекта в фикстуру для удаления после теста
    project_cleanup["id"] = id_new_project

    # получить проект по id
    get_project = api.get_project_by_id(id_new_project)
    assert get_project.status_code == 200
    project_data = get_project.json()

    # проверить,что id созданного проекта и полученного совпадают
    assert project_data.get("id") == id_new_project


#  3. Изменить название проекта
def test_edit_project(project_cleanup):

    # создать проект и получить его id
    resp_create = api.create_project()
    assert resp_create.status_code == 201
    project_id_before = resp_create.json().get("id")

    # передать id созданного проекта в фикстуру для удаления после теста
    project_cleanup["id"] = project_id_before

    # получить title проекта до его изменения
    resp_info_before = api.get_project_by_id(project_id_before)
    assert resp_info_before.status_code == 200
    project_title_before = resp_info_before.json().get("title")

    # присвоить новый title проекту
    new_title = fake.catch_phrase()
    resp_edit = api.edit_project(project_id_before, new_title)
    assert resp_edit.status_code == 200
    project_id_after = resp_edit.json().get("id")

    # получить title проекта после изменения
    resp_info_after = api.get_project_by_id(project_id_after)
    assert resp_info_after.status_code == 200
    project_title_after = resp_info_after.json().get("title")

    # проверить, что id проекта до изменения и после совпадают
    assert project_id_before == project_id_after

    # проверить, что  title проекта до изменения и после не совпадают
    assert project_title_before != project_title_after

    # проверить, что на сервере сохранился именно измененный проект
    assert project_title_after == new_title


#  3. Изменить удаленный проект
def test_edit_remote_project(project_cleanup):

    # создать проект и получить его id
    resp_create = api.create_project()
    assert resp_create.status_code == 201
    project_id = resp_create.json().get("id")

    # передать id созданного проекта в фикстуру для удаления после теста
    project_cleanup["id"] = project_id

    # получить статус "deleted" проекта до его изменения
    resp_info_before = api.get_project_by_id(project_id)
    assert resp_info_before.status_code == 200
    project_status = resp_info_before.json().get("deleted")

    # получить статус проекта (должен вернуться None)
    assert project_status is None

    # изменить статус проекта на True
    new_project_status = api.edit_remote_project(
        project_id, body={"deleted": True})
    assert new_project_status.status_code == 200

    # изменить название удаленного проекта
    new_title = fake.catch_phrase()
    edit_project = api.edit_remote_project(
        project_id, body={"title": new_title})

    # проверить, что изменение проекта прошло успешно
    assert edit_project.status_code == 200

    # проверить, что в ответе вернулось обновленное название проекта
    resp_get_updated = api.get_project_by_id(project_id)
    assert resp_get_updated.status_code == 200
    assert resp_get_updated.json().get("title") == new_title
