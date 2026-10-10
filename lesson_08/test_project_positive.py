from project_page import ProjectApi
from faker import Faker

fake = Faker("ru_RU")

api = ProjectApi("https://ru.yougile.com")


#  1. Создать новый проект
def test_create_new_project():

    # получить количество проектов до создания нового проекта
    projects_list_before = api.get_project_list().get("content", [])
    len_before = len(projects_list_before)

    # создать новый проект
    new_project = api.create_project()

    # проверить количество проектов после создания нового проекта
    projects_list_after = api.get_project_list().get("content", [])
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
def test_get_project():

    # создать проект
    new_project = api.create_project()
    id_new_project = new_project.get("id")

    # получить проект по id
    get_project = api.get_project_by_id(id_new_project)

    # проверить,что id созданного проекта и полученного совпадают
    assert get_project.get("id") == id_new_project


#  3. Изменить название проекта
def test_edit_project():

    # создать проект и получить его id
    project_before = api.create_project()
    project_id_before = project_before.get("id")

    # получить title проекта до его изменения
    project_info_before = api.get_project_by_id(project_id_before)
    project_title_before = project_info_before.get("title")

    # присвоить новый title проекту
    new_title = fake.catch_phrase()
    project_after = api.edit_project(project_id_before, new_title)

    # получить id проекта после изменения
    project_id_after = project_after.get("id")

    # получить title проекта после изменения
    project_info_after = api.get_project_by_id(project_id_after)
    project_title_after = project_info_after.get("title")

    # проверить, что id проекта до изменения и после совпадают
    assert project_id_before == project_id_after

    # проверить, что  title проекта до изменения и после не совпадают
    assert project_title_before != project_title_after

    # проверить, что на сервере сохранился именно измененный проект
    assert project_title_after == new_title


#  3. Изменить удаленный проект
def test_edit_remote_project():

    # создать проект и получить его id
    project_before = api.create_project()
    project_id = project_before.get("id")

    # получить статус "deleted" проекта до его изменения
    project_info_before = api.get_project_by_id(project_id)
    project_status = project_info_before.get("deleted")

    # проверить, что статус проекта False
    assert project_status is None

    # изменить статус "deleted" проекта на True
    new_project_status = api.edit_remote_project(
        project_id, body={"deleted": True})

    # проверить, что статус проекта  успешно изменен
    assert new_project_status.status_code == 200

    # изменить название удаленного проекта
    new_title = fake.catch_phrase()
    edit_project = api.edit_remote_project(
        project_id, body={"title": new_title})

    # проверить, что сервер вернул ошибку
    assert edit_project.status_code == 200
