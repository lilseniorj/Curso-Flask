import unittest

from app import create_app
from models import Note, db


class NoteTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config.TestConfig")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_create_note(self):
        with self.app.app_context():
            note_db = Note(title="Title", content="Content")
            db.session.add(note_db)
            db.session.commit()

            note = Note.query.first()

            self.assertEqual(note.title, "Title")
            self.assertEqual(note.content, "Content")

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
