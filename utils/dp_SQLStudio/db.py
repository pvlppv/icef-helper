import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subscription_users" ("user_id") VALUES (?)', (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subscription_users" WHERE "user_id" = ?', (user_id,)).fetchall()
            return bool(len(result))

    def set_sub_time(self, user_id, sub_time):
        with self.connection:
            return self.cursor.execute('UPDATE "subscription_users" SET "sub_time" = ? WHERE "user_id" = ?', (sub_time, user_id,))

    def get_sub_time(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT "sub_time" FROM "subscription_users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result:
                sub_time = int(row[0])
            return sub_time

    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT "sub_time" FROM "subscription_users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result:
                sub_time = int(row[0])

            if sub_time > int(time.time()):
                return True
            else:
                return False

    def get_user_id(self):
        with self.connection:
            user_id = self.cursor.execute('SELECT * FROM "queue"', ()).fetchmany(1)



# subscription
    def add_check(self, user_id, bill_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO "check" ("user_id", "bill_id") VALUES (?,?)', (user_id, bill_id,))

    def get_check(self, bill_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "check" WHERE "bill_id" = ?', (bill_id,)).fetchmany(1)
            if not bool(len(result)):
                return False
            return result[0]

    def delete_check(self, user_id):
        with self.connection:
            return self.cursor.execute('DELETE FROM "check" WHERE "user_id" = ?', (user_id,))



# anonim chat
    def add_queue(self, chat_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO "queue" ("chat_id") VALUES (?)', (chat_id,))

    def delete_queue(self, chat_id):
        with self.connection:
            return self.cursor.execute('DELETE FROM "queue" WHERE "chat_id" = ?', (chat_id,))

    def get_chat(self):
        with self.connection:
            chat = self.cursor.execute('SELECT * FROM "queue"', ()).fetchmany(1)
            if (bool(len(chat))):
                for row in chat:
                    return row[1]
            else:
                return False

    def get_queue(self, chat_id):
        with self.connection:
            self.cursor.execute('SELECT * FROM "queue" WHERE "chat_id" = ?', (chat_id,))

    def create_chat(self, chat_one, chat_two):
        with self.connection:
            if chat_two != 0:
                self.cursor.execute('DELETE FROM "queue" WHERE "chat_id" = ?', (chat_two,))
                self. cursor.execute('INSERT INTO "chats" ("chat_one", "chat_two") VALUES (?,?)', (chat_one, chat_two,))
                return True
            else:
                return False

    def get_active_chat(self, chat_id):
        with self.connection:
            chat = self.cursor.execute('SELECT * FROM "chats" WHERE "chat_one" = ?', (chat_id,))
            id_chat = 0
            for row in chat:
                id_chat = row[0]
                chat_info = [row[0], row[2]]

            if id_chat == 0:
                chat = self.cursor.execute('SELECT * FROM "chats" WHERE "chat_two" = ?', (chat_id,))
                for row in chat:
                    id_chat = row[0]
                    chat_info = [row[0], row[1]]
                if id_chat == 0:
                    return False
                else:
                    return chat_info
            else:
                return chat_info

    def delete_chat(self, id_chat):
        with self.connection:
            self.cursor.execute('DELETE FROM "chats" WHERE "id" = ?', (id_chat,))

    # calculus
    def add_calculus(self, calculus):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("calculus") VALUES (?)', (calculus,))

    def calculus_exists(self, calculus):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "calculus" = ?', (calculus,)).fetchall()
            return bool(len(result))

    def calculus_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT created_at, calculus FROM subjects WHERE calculus IS NOT NULL ORDER BY id DESC').fetchone()

    def calculus_last_count(self):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(calculus) from subjects').fetchall()

    # statistics
    def add_statistics(self, statistics):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("statistics") VALUES (?)', (statistics,))

    def statistics_exists(self, statistics):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "statistics" = ?', (statistics,)).fetchall()
            return bool(len(result))

    def statistics_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT created_at, statistics FROM subjects WHERE statistics IS NOT NULL ORDER BY id DESC').fetchone()

    def statistics_last_count(self):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(statistics) from subjects').fetchall()

    # microeconomics
    def add_microeconomics(self, microeconomics):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("microeconomics") VALUES (?)', (microeconomics,))

    def microeconomics_exists(self, microeconomics):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "microeconomics" = ?', (microeconomics,)).fetchall()
            return bool(len(result))

    def microeconomics_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT created_at, microeconomics FROM subjects WHERE microeconomics IS NOT NULL ORDER BY id DESC').fetchone()

    def microeconomics_last_count(self):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(microeconomics) from subjects').fetchall()

    # history
    def add_history(self, history):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("history") VALUES (?)', (history,))

    def history_exists(self, history):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "history" = ?', (history,)).fetchall()
            return bool(len(result))

    def history_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT created_at, history FROM subjects WHERE history IS NOT NULL ORDER BY id DESC').fetchone()

    def history_last_count(self):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(history) from subjects').fetchall()

    # timetable
    def add_timetable(self, timetable):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("timetable") VALUES (?)', (timetable,))

    def delete_timetable(self):
        with self.connection:
            return self.cursor.execute('DELETE FROM "subjects" WHERE "timetable"=(SELECT MAX("timetable") FROM "subjects")')

    def timetable_exists(self, timetable):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "timetable" = ?', (timetable,)).fetchall()
            return bool(len(result))

    def timetable_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT MAX(created_at), timetable FROM subjects WHERE timetable IS NOT NULL').fetchone()

    # office_hours
    def add_office_hours(self, office_hours):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("office_hours") VALUES (?)', (office_hours,))

    def delete_office_hours(self):
        with self.connection:
            return self.cursor.execute('DELETE FROM "subjects" WHERE "office_hours"=(SELECT MAX("office_hours") FROM "subjects")')

    def office_hours_exists(self, office_hours):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "office_hours" = ?', (office_hours,)).fetchall()
            return bool(len(result))

    def office_hours_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT MAX(created_at), office_hours FROM subjects WHERE office_hours IS NOT NULL').fetchone()

    # optional_courses
    def add_optional_courses(self, optional_courses):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("optional_courses") VALUES (?)', (optional_courses,))

    def delete_optional_courses(self):
        with self.connection:
            return self.cursor.execute('DELETE FROM "subjects" WHERE "optional_courses"=(SELECT MAX("optional_courses") FROM "subjects")')

    def optional_courses_exists(self, optional_courses):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "optional_courses" = ?', (optional_courses,)).fetchall()
            return bool(len(result))

    def optional_courses_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT MAX(created_at), optional_courses FROM subjects WHERE optional_courses IS NOT NULL').fetchone()

    # exams_timetable
    def add_exams_timetable(self, exams_timetable):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects" ("exams_timetable") VALUES (?)', (exams_timetable,))

    def delete_exams_timetable(self):
        with self.connection:
            return self.cursor.execute('DELETE FROM "subjects" WHERE "exams_timetable"=(SELECT MAX("exams_timetable") FROM "subjects")')

    def exams_timetable_exists(self, exams_timetable):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "subjects" WHERE "exams_timetable" = ?', (exams_timetable,)).fetchall()
            return bool(len(result))

    def exams_timetable_last_update(self):
        with self.connection:
            return self.cursor.execute('SELECT MAX(created_at), exams_timetable FROM subjects WHERE exams_timetable IS NOT NULL').fetchone()

    # notifications
    def add_notification(self, user_id, start_date, end_date, text):
        with self.connection:
            return self.cursor.execute('INSERT INTO "notifications" ("user_id", "start_date", "end_date", "text") VALUES (?,?,?,?)', (user_id, start_date, end_date, text,))

    # subjects schedule
    def add_subjects_schedule(self, date, time, title, professor, auditorium, group):
        with self.connection:
            return self.cursor.execute('INSERT INTO "subjects_schedule" ("date", "time", "title", "professor", "auditorium", "group") VALUES (?,?,?,?,?,?)', (date, time, title, professor, auditorium, group,))

    def subjects_schedule_monday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Monday%" ORDER BY "time"', (title,)).fetchall()
            return result

    def subjects_schedule_tuesday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Tuesday%" ORDER BY "time"', (title,)).fetchall()
            return result

    def subjects_schedule_wednesday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Wednesday%" ORDER BY "time"', (title,)).fetchall()
            return result

    def subjects_schedule_thursday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Thursday%" ORDER BY "time"', (title,)).fetchall()
            return result

    def subjects_schedule_friday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Friday%" ORDER BY "time"', (title,)).fetchall()
            return result

    def subjects_schedule_saturday(self, title):
        with self.connection:
            result = self.cursor.execute('SELECT "date", "time", "title", "professor", "auditorium", "group" FROM "subjects_schedule" WHERE "title" = ? AND "date" LIKE "%Saturday%" ORDER BY "time"', (title,)).fetchall()
            return result






