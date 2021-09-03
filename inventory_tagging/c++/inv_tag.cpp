//
// Created by Sean on 5/23/2021.
//

#include "inv_tag.h"
#include <string>

using namespace std;

using std::cin;
using std::cout;
using std::endl;
using std::string;

Inv_Tag::Inv_Tag(string tn,
                 string lb,
                 int lf,
                 string lr,
                 string ma,
                 string mo,
                 string sn,
                 long pd,
                 long td,
                 string pdoc,
                 int dc,
                 string o,
                 bool fp,
                 string com) {
    this.tag_num = tn;
    this.loc_bldg = lb;
    this.loc_flr = lf;
    this.loc_room = lr;
    this.make = ma;
    this.model = mo;
    this.serial_num = sn;
    this.pur_date = pd;
    this.tag_date = td;
    this.pur_doc = pdoc;
    this.dept_contact = dc;
    this.owner = o;
    this.fed_prop = fp;
    this.comment = com;
}

InvTag::getPurDateStr() {

};

InvTag::setPurDate(string dateString) {

};

InvTag::getTagDateStr() {

};

InvTag::setTagDate(string dateString) {

};