from sqlite3 import *

def enter_standard(standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:

		cur.execute("SELECT DISTINCT(standard) FROM subject_table;")
		standards = cur.fetchall()[0]
		if standard in standards:
			print "Standard Already Present"
		else:
			cur.execute("INSERT INTO subject_table(standard,subjects) VALUES(?,NULL);",(standard))
		conn.commit()	
	except:
		print "Unable to add standard"

def enter_subject(subject,standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT subjects FROM subject_table;")
		subjects=cur.fetchone()[0]
		subjects+=(","+subject)
		cur.execute("UPDATE subject_table SET subjects = ? WHERE standard = ?;",(subjects,standard))
		cur.execute("INSERT INTO main_table(standard,subject,qmarks) VALUES(?,?,NULL);",(standard,subject))
		conn.commit()
	except:
		print "Unable to add Subject";
	

def enter_marks(subject,standard,mark):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT qmarks FROM main_table WHERE standard=? AND subject=?;",(standard,subject))
		marks = cur.fetchone()[0]
		marks+=(","+mark)
		cur.execute("UPDATE main_table SET qmarks=? WHERE subject=? AND standard=?;",(qmarks,subject,standard))
		conn.commit()
	except:
		print "Unable to add marks"
	
def edit_standard(std_old,std_new):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("UPDATE subject_table SET standard = ? WHERE standard = ?;",(std_new,std_old))
		cur.execute("UPDATE main_table SET standard = ? WHERE standard = ?;",(std_new,std_old))
		conn.commit()
	except:
		print "Unable to edit standard"
	

def edit_subject(sub_old,sub_new,standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT subjects FROM subject_table WHERE standard=?;",(standard))
		subjects = cur.fetchone()[0]
		temp = subjets.split(",")
		for i in temp:
			if i==sub_old:
				i=sub_new
		cur.execute("UPDATE subject_table SET subject = ? WHERE standard = ?;", (",".join(temp),standard))
		cur.execute("UPDATE main_table SET subject=? WHERE subject=?;",(sub_new,sub_old))
		conn.commit()
	except:
		print "Unable to edit standard"
	

def delete_standard(standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("DELETE from subject_table WHERE standard = ?;",(standard))
		cur.execute("DELETE from main_table WHERE standard = ?;",(standard))
		conn.commit()
	except:
		print "Unable to delete standard"

def  delete_subject(sub,standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT subjects FROM subject_table WHERE standard=?;",(standard))
		subjects = cur.fetchone()[0]
		temp = subjects.split(",")
		temp2 = []
		for i in temp:
			if i!=sub:
				temp2.append(i)
		cur.execute("UPDATE subject_table SET subjects = ? WHERE standard= ?;",(",".join(temp2),standard))
		cur.execute("DELETE FROM main_table WHERE subject = ? AND standard = ?;",(subject,standard))
		conn.commit()
	except:
		print "Unable to delete subject"

def retrieve_standard():
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT DISTINCT(standard) FROM subject_table;")
		temp = [i[0] for i in cur.fetchall()]
		return temp
	except:
		print "Failed to retrieve standards"

def retrieve_subjects(standard):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		print standard
		print type(standard)
		cur.execute("SELECT subjects FROM subject_table WHERE standard=?;",(standard))
		temp = cur.fetchone()[0].split(",")
		return temp
	except:
		print "Failed to retrieve subjects"

def retrieve_marks(standard,subject):
	try:
		conn = connect("questions.sqlite")
		cur = conn.cursor()
	except:
		print "Failed to establish connection with database"
	try:
		cur.execute("SELECT qmarks FROM main_table WHERE standard=? AND subject=?;",(standard,subject))
		temp = cur.fetchone()[0].split(",")
		return temp
	except:
		print "Failed to reterieve marks"