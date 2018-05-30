from app.config.databse import db_connect


def add_notification_to_db(id_user, notification):
	agruments = [id_user, notification]
	sql = "INSERT INTO notifications (id_user, notification, date_creation) VALUES (?,?, datetime('now', 'localtime'))"
	res = db_connect(sql, agruments)
	return res


def check_notification_in_db(id_user, notification):
	agruments = [id_user, notification]
	sql = "SELECT id_notif FROM notifications WHERE id_user = ? AND notification = ? "
	res = db_connect(sql, agruments)
	return res