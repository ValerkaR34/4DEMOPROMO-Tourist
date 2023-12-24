from  ..sql_base.models import Excursions

from server.sql_base.Rescript import base_manager
def new_excurs(Excursiones: Excursions):
    sa = base_manager.execute(f""" INSERT INTO Excursions(ExcursionName,Price) VALUES(?,?) RETURNING ExcursionID;""",
                              (Excursiones.ExcursionName,Excursiones.Price))
    return sa


def update_excur(Excursiones: Excursions, ExcursionID: int):
    upod = base_manager.execute(f"""update Excursions set (ExcursionName, Price) = (?,?) where ExcursionID=(?); """,
                                (Excursiones.ExcursionName,Excursiones.Price,ExcursionID))
    return upod

def delete_excur(ExcursionID: int):
    return base_manager.execute(query="DELETE FROM Excursions WHERE ExcursionID=?",
                                args=(ExcursionID,))


def get_excur(ExcursionID: int):
    return base_manager.execute(query="SELECT ExcursionID,ExcursionName,Price FROM Excursions WHERE ExcursionID=?", args=(ExcursionID,))

def get_all_excur():
    return base_manager.execute(query="SELECT ExcursionID,ExcursionName,Price FROM Excursions", many=True)