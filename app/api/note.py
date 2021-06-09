from flask import request, jsonify
from app import app
from app.models import Note
from app.utils.authenticator import authenticate_appuser, author, editor
from playhouse.shortcuts import model_to_dict

@app.route('/api/v1/notes', methods=['GET','POST'])
@editor
def get_or_create_notes():
    sts, app_user, roles = authenticate_appuser()
    if request.method == 'GET':
        try:
            notes = Note.select()
            result = [model_to_dict(note, exclude=[Note.author]) for note in notes]
            return jsonify(result=result)
        except Exception as e:
            return jsonify(error=str(e))

    if request.method == 'POST':
        data = request.get_json()
        try:
            note = Note(**data)
            note.author = int(app_user)
            note.save()
            return jsonify(result=model_to_dict(note, exclude=[Note.author]))
        except Exception as e:
            return jsonify(error=str(e))
