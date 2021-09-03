//
// Created by Sean on 5/23/2021.
//

#ifndef INV_TAG_H
#define INV_TAG_H

#include <string>

using std::string;

class Inv_Tag {
private:
    string tag_num;
    string loc_bldg;
    int loc_flr;
    string loc_room;
    string make;
    string model;
    string serial_num;
    long pur_date;
    long tag_date;
    string pur_doc;
    int dept_contact;
    string owner;
    bool fed_prop;
    string comment;
public:
    Inv_Tag(string tn, string lb, int lf, string lr, string ma,
            string mo, string sn, long pd, long td, string pdoc,
            int dc, string o, bool fp, string com);

    string getTag_Num() { return this->tag_num; }
    void setTag_Num(string s) { this->tag_num = s; }

    string getLoc_Bldg() { return this->loc_bldg; }
    void setLoc_Bldg(string s) { this->loc_bldg = s; }

    int getLoc_Flr() { return this->loc_flr; }
    void setLoc_Flr(int n) { this->loc_flr = n}

    string getLoc_Room() { return this->loc_room; }
    void setLoc_Room(string s) { this->loc_room = s; }

    string getMake() { return this->make; }
    void setMake(string s) { this->make = s; }

    string getModel() { return this->model; }
    void setModel(string s) { this->model = s; }

    string getSerialNum() { return this->serial_num; }
    void setSerialNum(string s) { this->serial_num = s; }

    long getPurDate() { return this->pur_date; }
    string getPurDateStr();
    void setPurDate(string dateString);

    long getTagDate() { return this->pur_date; }
    string getTagDateStr();
    void setTagDate(string dateString);

    string getOwner() { return this->owner; }
    void setOwner(string s) { this->owner = s; }

    string getComment() { return this->comment; }
    void setComment(string s) { this->comment = s; }


};

#endif //INV_TAG_H
