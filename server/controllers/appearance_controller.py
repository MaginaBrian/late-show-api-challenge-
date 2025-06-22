from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    if not Guest.query.get(data['guest_id']) or not Episode.query.get(data['episode_id']):
        return jsonify({'error': 'Invalid guest or episode ID'}), 404
    
    try:
        appearance = Appearance(**data)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400