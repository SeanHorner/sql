
class Location:
    def __init__(self,
                 bldg: str,
                 floor: int,
                 room: str,
                 map_x: float = 0.0,
                 map_y: float = 0.0):
        self.bldg = bldg
        self.floor = floor
        self.room = room
        self.map_x = map_x
        self.map_y = map_y

    def __str__(self):
        return f"{self.bldg} {self.floor}.{self.room}"

    def str_convert(self, form_str: str):
        bldg, other = form_str.split(' ')
        floor, room = other.split('.')
        self.bldg = bldg
        self.floor = floor
        self.room = room


class PurchaseDoc:
    def __init__(self,
                 doc_id: str,
                 procard: str,
                 dept: str,
                 contact: str,
                 doc_scan=None,
                 associated_tags=None):
        self.associated_tags = list[str]()
        for tag in associated_tags:
            if len(tag) == 6:
                self.add_tag(tag)

        self.doc_Scan = None
        if doc_scan is not None:
            with open(doc_scan, 'rb') as img_file:
                self.doc_scan = img_file.read()

        self.doc_id = doc_id
        self.procard = procard
        self.dept = dept
        self.contact = contact

    def add_tag(self, tag_num: str):
        self.associated_tags += tag_num

    def doc_upload(self, doc_scan):
        with open(doc_scan, 'rb') as file:
            self.doc_scan = file.read()


class DeptContact:
    def __init__(self,
                 contact_id: int,
                 first_name: str,
                 last_name: str,
                 office: str,
                 notes: str,
                 photo=None):
        self.contact_id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.office = office
        self.notes = notes

        self.photo = None
        if photo is not None:
            with open(photo, "rb") as img_file:
                self.photo = img_file.read()


class Tag:
    def __init__(self,
                 tag_num: int,
                 loc: str,
                 make: str,
                 model: str,
                 serial_num: str,
                 pur_date: int,
                 tag_date: int,
                 pur_doc: str,
                 dept_cont: int,
                 owner: str,
                 fed_prop: bool,
                 comment: str):
        self.tag_num = tag_num
        self.loc = loc
        self.make = make
        self.model = model
        self.serial_num = serial_num
        self.pur_date = pur_date
        self.tag_date = tag_date
        self.pur_doc = pur_doc
        self.dept_cont = dept_cont
        self.owner = owner
        self.fed_prop = fed_prop
        self.comment = comment

    def to_csv(self) -> str:
        output = ""
        output += f"{self.tag_num},"
        output += f"\"{self.loc}\","
        output += f"{self.make},"
        output += f"{self.model},"
        output += f"{self.serial_num},"
        output += f"{self.pur_date},"
        output += f"{self.tag_date},"
        output += f"{self.pur_doc},"
        output += f"{self.dept_cont},"
        output += f"{self.owner},"
        output += f"{self.fed_prop},"
        output += f"\"{self.comment}\""
        return output
