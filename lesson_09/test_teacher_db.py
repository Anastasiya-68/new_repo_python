from teacher_table import TeacherTable
from faker import Faker

fake = Faker("ru_RU")

db = TeacherTable("")


# 1. добавить нового учителя
def test_add_new_teacher():
    # получить список учителей до добавления нового учителя
    list_before = db.get_teacher()
    len_before = len(list_before)

    # добавить нового учителя
    teacher_id = fake.unique.random_int(min=1, max=1000)
    email = fake.unique.email()
    group_id = fake.unique.random_int(min=1, max=100)
    db.add_new_teacher(teacher_id, email, group_id)

    # взять id нового учителя
    new_id = teacher_id

    # получить список учителей после добавления нового учителя
    list_after = db.get_teacher()
    len_after = len(list_after)

    # удалить из бд нового учителя
    db.delete_teacher(new_id)

    # сравнить список учителей до добавления нового учителя и после
    assert len_after - len_before == 1

    # проверить, что новый учитель появился в бд
    found = False
    for teacher in list_after:
        if teacher.get("teacher_id") == new_id:
            found = True
            assert teacher.get("email") == email
            break

    assert found


# 2. обновить данные учителя
def test_edit_teacher():
    # добавить нового учителя
    teacher_id = fake.unique.random_int(min=1, max=1000)
    email = fake.unique.email()
    group_id = fake.unique.random_int(min=1, max=100)
    db.add_new_teacher(teacher_id, email, group_id)

    # изменить email добавленного учителя
    new_email = fake.unique.email()
    db.edit_teacher(new_email, teacher_id)

    # получить обновленные данные учителя
    teacher_info = db.get_teacher_by_id(teacher_id)

    # удалить из бд учителя
    db.delete_teacher(teacher_id)

    # проверить, что данные учителя обновились
    assert teacher_info.get("teacher_id") == teacher_id
    assert teacher_info.get("email") == new_email


# 3. удалить учителя
def test_delete_teacher():
    # добавить нового учителя
    teacher_id = fake.unique.random_int(min=1, max=1000)
    email = fake.unique.email()
    group_id = fake.unique.random_int(min=1, max=100)
    db.add_new_teacher(teacher_id, email, group_id)

    # удалить добавленного учителя
    db.delete_teacher(teacher_id)

    # убедиться, что в бд нет удаленного учителя
    teacher_info = db.get_teacher_by_id(teacher_id)
    assert teacher_info is None
