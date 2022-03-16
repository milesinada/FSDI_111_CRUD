from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["license_plate"] = result[1]
        res_dict["v_type"] = result[2]
        res_dict["color"] = result[3]
        res_dict["user_id"] = result[4]
        res_dict["active"] = result[5]
        out.append(res_dict)
    return out


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict["v_type"],
        vehicle_dict["license_plate"],
        vehicle_dict["id"],
        vehicle_dict["color"],
        vehicle_dict["user_id"],
        vehicle_dict["active"],



    )
    stmt = """
        INSERT INTO vehicle (
            v_type,
            license_plate,
            color,
            user_id
        ) VALUES (?, ?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(stmt, value_tuple)
    cursor.commit()
    cursor.close()



def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_user_id(uid):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE user_id=?", (uid, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, vehicle_data):
    value_tuple(
        vehicle_data["v_type"],
        vehicle_data["license_plate"],
        vehicle_data["color"],
        vehicle_data["user_id"],

        pk
    )
    stmt = """
        UPDATE vehicle
        SET v_type=?,
        license_plate=?,
        color=?,
        user_id=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()



def deactivate_vehicle(pk):
    stmt = """
        UPDATE vehicle
        SET active=0
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, (pk, ))
    cursor.commit()