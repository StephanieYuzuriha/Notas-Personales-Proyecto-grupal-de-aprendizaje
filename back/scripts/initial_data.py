import sys

sys.path.insert(0, "")
from src.domain.user import UserRepository, User
from src.domain.note import NotesRepository, Note
from src.domain.info import InfoRepository, Info
from src.domain.tags import Tag, TagsRepository


def main():

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-my-notes-app2"))

    notes_repository = NotesRepository(database_path)

    tag_repository = TagsRepository(database_path)
    # tag_1 = Tag(note_id="1", tag="Music")
    # tag_2 = Tag(note_id="2", tag="Claudio")

    # Guardar categorias en NOTE repository
    notes_repository.save_a_new_category("cat-0", "No category")
    notes_repository.save_a_new_category("cat-1", "Sports")
    notes_repository.save_a_new_category("cat-2", "Music")
    notes_repository.save_a_new_category("cat-3", "Shopping List")

    nota1 = Note(
        id="note-1",
        title="Lista de la compra:",
        text="Pan y Chorizo",
        user_id="user-1",
        id_cat="cat-1",
    )
    nota2 = Note(
        id="note-2",
        title="Bebidas",
        text="Vino y agua",
        user_id="user-1",
        id_cat="cat-2",
    )

    notes_repository.insert_data_note(nota1)
    notes_repository.insert_data_note(nota2)

    print("last category id: ", notes_repository.get_last_category_id())

    # Repositorio de Usuarios

    user_repository = UserRepository(database_path)

    user_repository.save(User("user-1", "Roberto", "password1"))
    user_repository.save(User("user-2", "Laura", "password2"))
    tag_1 = Tag("note-1", ["Musica", "Cine"])
    tag_2 = Tag("note-1", ["Drogarme", "Ainarismo"])
    tag_repository.save(tag_1)
    tag_repository.save(tag_2)
    print("Datos iniciales cargados (se ha ejecutado initial_data.py)")


main()
