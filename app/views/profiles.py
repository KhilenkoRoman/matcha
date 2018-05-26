from app import app
from flask import render_template, session, redirect, request
from app.models.users import get_by_id
from app.models.friendship import *


@app.route('/profile/')
@app.route('/user/id<int:id_user>')
def profile(id_user=None):
	if session.get('id_user_logged'):
		if id_user:
			return render_template('timeline.html', user=get_by_id(id_user), user_cur=session.get('user_data'))
		return render_template('timeline.html', user=session.get('user_data'), user_cur=session.get('user_data'))
	if id_user:
		return render_template('timeline.html', user=get_by_id(id_user), user_cur=None)
	return redirect('/')


@app.route('/profile/edit/')
def edit_profile():
	if session.get('id_user_logged'):
		return render_template('edit-profile-basic.html', user=session.get('user_data'))
	return redirect('/')


def is_friends_with(auth_id, user_id):
	user = check_friends(auth_id, user_id)
	if user:
		return user
	return "0"


@app.route('/ajax_check_friends/')
def ajax_check_friends():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')
	user1 = is_friends_with(auth_id, user_id)
	user2 = is_friends_with(user_id, auth_id)

	if auth_id == user_id:
		return "same user"
	if user1 == "0":
		if user2 == "0":
			return "0"
		else:
			if user2['status'] == 0:
				return "pending"
			else:
				return "1"
	else:
		if user1['status'] == 0:
			return "waiting"
		else:
			return "1"


@app.route('/ajax_delete_user_request/')
def ajax_delete_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	delete_user_request(auth_id, user_id)
	return ajax_check_friends()


@app.route('/ajax_add_user_request/')
def ajax_add_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	add_friend(auth_id, user_id)
	return ajax_check_friends()


@app.route('/ajax_confirm_user_request/')
def ajax_confirm_user_request():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	confirm_user_request(user_id, auth_id)
	return ajax_check_friends()


@app.route('/ajax_delete_user_friend/')
def ajax_delete_user_friend():
	auth_id = request.args.get('auth_id')
	user_id = request.args.get('user_id')

	delete_user_request(auth_id, user_id)
	delete_user_request(user_id, auth_id)
	return ajax_check_friends()

