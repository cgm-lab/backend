from gsheets import mixins

from cgm.settings import GSHEETS_DB


class BaseSheet(mixins.SheetPullableMixin):
    spreadsheet_id = GSHEETS_DB["Main"]
    model_id_field = "guid"
    sheet_id_field = "guid"
