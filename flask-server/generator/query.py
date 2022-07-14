import mysql.connector


# @description: get the timetable blueprint
def db_query():
    #     import mysql.connector

    # config = {
    #   'user': 'root',
    #   'password': 'root',
    #   'host': 'localhost',
    #   'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    #   'database': 'test',
    #   'raise_on_warnings': True
    # }

    # cnx = mysql.connector.connect(**config)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_timetable",
        unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock'

    )
    sql = (
        "SELECT "
        "department.name as 'department', "
        "major.name as 'major', "
        "level.name as 'level', "
        "group_.name as 'group', "
        "module.code as 'Code', "
        "module.name as 'module', "
        "major_level_module.no_of_students as '#students', "
        "lecturer.name as 'lecturer' "
        "FROM "
        "major_level_module "
        "INNER JOIN "
        "module "
        "ON major_level_module.module_code = module.code "
        "INNER JOIN "
        "lecturer on module.lecturer_id = lecturer.id "
        "INNER JOIN "
        "major_level "
        "ON major_level_module.major_level_id = major_level.id "
        "INNER JOIN "
        "major "
        "ON major_level.major_id = major.id "
        "INNER JOIN "
        "department "
        "ON major.department_id = department.id "
        "INNER JOIN "
        "level "
        "ON major_level.level_id = level.id "
        "INNER JOIN group_ "
        "ON major_level_module.group_id = group_.id"
    )

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()

    tt = []
    for e in myresult:
        tt.append({
            'department': e[0],
            'major': e[1],
            'level': e[2],
            'group': e[3],
            'code': e[4],
            'module': e[5],
            'students': e[6],
            'lecturer': e[7]
        })
    # print(tt[0].keys())
    # toCSV.createCSV(tt)
    return tt


def get_lecturers():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",

        database="smart_timetable",
        unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock'
    )
    sql = (
        "SELECT "
        "* "
        "FROM "
        "lecturer"
    )

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    # print(myresult)
    # lecturers = []
    # for e in myresult:
    #     lecturers.append(e[0])
    return myresult


def get_major_students():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",

        database="smart_timetable",
        unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock'
    )

    sql = (
        "SELECT "
        "major.name AS 'major', level.name AS 'level' "
        "from major_level "
        "INNER JOIN major "
        "ON major_level.major_id = major.id "
        "INNER JOIN level on major_level.level_id = level.id"
    )

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    # print(myresult)
    # lecturers = []
    # for e in myresult:
    #     lecturers.append(e[0])
    return myresult


# get_lecturers()
# get_major_students()

def get_major_level_group():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",

        database="smart_timetable",
        unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock'
    )

    sql = ("SELECT `major`.`name` as major, department.name as department, group_.name as `group`, level.name as `level`"
           "FROM major_level_module "
           "INNER JOIN major_level "
           "ON major_level_module.major_level_id = major_level.id "
           "INNER JOIN `level` "
           "ON major_level.level_id = `level`.`id` "
           "INNER JOIN group_ "
           "on major_level_module.group_id = group_.id "
           "INNER JOIN major "
           "on major_level.id = major.id "
           "INNER JOIN department "
           "ON major.department_id = department.id"
           )

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    # put the result in an array and ignore duplicate entries
    # add row number to each row

    anArray = []
    ind = 0
    for e in myresult:
        if e not in anArray:
            anArray.append(e)
    myList = []
    for e in anArray:
        x = list(e)
        x.insert(0, ind)
        x[-2] = x[-2].split('/')
        e = tuple(x)
        myList.append(e)
        ind += 1
        # anArray[ind].append(ind)
        # ind += 1
        # x = list(e)
        # x.insert(0, ind)
        # ind += 1
        # if x not in anArray:
        #     anArray.append(x)
    print(myList)
    # print(myresult)
    # lecturers = []
    # for e in myresult:
    #     lecturers.append(e[0])
    return myresult
