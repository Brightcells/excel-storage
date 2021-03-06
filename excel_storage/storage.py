# -*- coding:utf-8 -*-

import datetime

from excel_base import BytesIO, StringIO, as_csv, as_row_merge_xls, as_xls, is_py2


# Min (Max. Rows) for Widely Used Excel
# http://superuser.com/questions/366468/what-is-the-maximum-allowed-rows-in-a-microsoft-excel-xls-or-xlsx
EXCEL_MAXIMUM_ALLOWED_ROWS = 65536
# Column Width Limit For ``xlwt``
# https://github.com/python-excel/xlwt/blob/master/xlwt/Column.py#L22
EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH = 65535


def __init__(self, data, output_name='excel_data', format='%Y%m%d%H%M%S', headers=None, force_csv=False, encoding='utf-8-sig', font='', sheet_name='Sheet 1', blanks_for_none=True, auto_adjust_width=True, vert=0x01, horz=0x01, row_merge=False, timezone=None):
    self.data = data
    self.output_name = output_name
    self.format = format
    self.headers = headers
    self.force_csv = force_csv
    self.encoding = encoding
    self.font = font
    self.sheet_name = sheet_name
    self.blanks_for_none = blanks_for_none
    self.auto_adjust_width = auto_adjust_width
    self.file_ext = None
    # VERT_TOP     = 0x00    顶端对齐
    # VERT_CENTER  = 0x01    居中对齐（垂直方向上）
    # VERT_BOTTOM  = 0x02    底端对齐
    # HORZ_LEFT    = 0x01    左端对齐
    # HORZ_CENTER  = 0x02    居中对齐（水平方向上）
    # HORZ_RIGHT   = 0x03    右端对齐
    self.vert = vert
    self.horz = horz
    self.timezone = timezone

    # Make sure we've got the right type of data to work with
    # ``list index out of range`` if data is ``[]``
    valid_data = False
    if hasattr(self.data, '__getitem__'):
        if isinstance(self.data[0], dict):
            if headers is None:
                headers = list(self.data[0].keys())
            self.data = [[row[col] for col in headers] for row in self.data]
            self.data.insert(0, headers)
        if hasattr(self.data[0], '__getitem__'):
            valid_data = True
    assert valid_data is True, 'ExcelStorage requires a sequence of sequences'

    self.output = StringIO() if is_py2 else BytesIO()
    if row_merge:
        _, file_ext = (self.as_row_merge_xls, 'xls')
    else:
        # Excel has a limit on number of rows; if we have more than that, make a csv
        use_xls = True if len(self.data) <= self.EXCEL_MAXIMUM_ALLOWED_ROWS and not self.force_csv else False
        _, file_ext = (self.as_xls, 'xls') if use_xls else (self.as_csv, 'csv')
    self.output.seek(0)

    self.file_ext = file_ext


def save(self):
    file_name_ext = '_{0}'.format(datetime.datetime.now().strftime(self.format)) if self.format else ''
    final_file_name = ('%s%s.%s' % (self.output_name, file_name_ext, self.file_ext)).replace('"', '\"')

    with open(final_file_name, 'wb') as writer:
        writer.write(self.output.getvalue())

    return final_file_name


clsdict = {
    'EXCEL_MAXIMUM_ALLOWED_ROWS': EXCEL_MAXIMUM_ALLOWED_ROWS,
    'EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH': EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH,
    '__init__': __init__,
    'as_xls': as_xls,
    'as_row_merge_xls': as_row_merge_xls,
    'as_csv': as_csv,
    'save': save,
}


ExcelStorage = type('ExcelStorage', (object, ), clsdict)
