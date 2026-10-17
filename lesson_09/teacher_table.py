from sqlalchemy import create_engine, text


class TeacherTable:
    __scripts = {
        "select_all": text("SELECT * FROM teacher"),
        "insert_new": text(
            "INSERT INTO teacher(\"teacher_id\", \"email\", \"group_id\") "
            "VALUES (:teacher_id, :email, :group_id)"),
        "select_by_id": text(
            "SELECT * FROM teacher "
            "WHERE teacher_id = :select_id"),
        "update_email": text(
            "UPDATE teacher SET email = :new_email "
            "WHERE teacher_id = :teacher_id"
        ),
        "delete_by_id": text(
            "DELETE FROM teacher WHERE teacher_id = :id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    # метод для получения списка учителей
    def get_teacher(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_all"])
        rows = result.mappings().all()
        conn.close()
        return rows

    # метод для получения данных учителя по id
    def get_teacher_by_id(self, teacher_id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select_by_id"], {"select_id": teacher_id}
            )
        row = result.mappings().one_or_none()
        conn.close()
        return row

    # метод для добавления нового учителя
    def add_new_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["insert_new"],
            {
                "teacher_id": teacher_id,
                "email": email,
                "group_id": group_id
            }
        )
        conn.commit()
        conn.close()

    # метод для удаления учителя
    def delete_teacher(self, teacher_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete_by_id"], {"id_to_delete": teacher_id}
            )
        conn.commit()
        conn.close()
        return True

    # метод для изменения данных учителя
    def edit_teacher(self, new_email, teacher_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["update_email"],
            {
                "new_email": new_email,
                "teacher_id": teacher_id
            }
        )
        conn.commit()
        conn.close()
