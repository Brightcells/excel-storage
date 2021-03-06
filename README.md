# excel-storage
Excel Storage

## Installation

    pip install excel-storage


## Usage

    from excel_storage import ExcelStorage

    def excelfunc():
        data = [
            {
                'Column 1': 1,
                'Column 2': 2,
            },
            {
                'Column 1': 3,
                'Column 2': 4,
            }
        ]
        fpath = ExcelStorage(data, 'my_data', font='name SimSum').save()


or

    from excel_storage import ExcelStorage

    def excelfunc():
        data = [
            ['Column 1', 'Column 2'],
            [1, 2],
            [3, 4]
        ]
        fpath = ExcelStorage(data, 'my_data', font='name SimSum').save()


or

    from excel_storage import ExcelStorage

    def excelfunc():
        data = [
            ['Column 1', 'Column 2'],
            [1, [2, 3]],
            [3, 4]
        ]
        fpath = ExcelStorage(data, 'my_data', font='name SimSum', row_merge=True).save()


## Params

  * font='name SimSum'
    * Set Font as SimSum(宋体)
  * force_csv=True
    * CSV Format? True for Yes, False for No, Default is False


## CSV

  ```python
  datas = [
      [u'中文', ]
  ]
  ```

|                 | Win Excel 2013 | Mac Excel 2011 | Mac Excel 2016 | Mac Numbers |
| --------------- | :------------: | :------------: | :------------: | :---------: |
| UTF8            | Messy          | Messy          | Messy          | Normal      |
| GB18030         | Normal         | Normal         | Normal         | Messy       |
| UTF8 + BOM_UTF8 | Normal         | Messy          | Normal         | Normal      |
| UTF16LE + BOM   |                |                |                |             |
