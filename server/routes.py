from flask import Blueprint, request, jsonify
from app import db
from models import Episode, Guest, Appearance

bp = Blueprint("api", __name__)

# GET /episodes
@bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

# GET /episodes/:id
@bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict(include_appearances=True)), 200
    else:
        return jsonify({"error": "Episode not found"}), 404

# GET /guests
@bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

# POST /appearances
@bp.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({"errors": ["Episode or Guest not found"]}), 404

    try:
        appearance = Appearance(rating=rating, episode=episode, guest=guest)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
