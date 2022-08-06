#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 21:06:31 2022

@author: John Ciubuc
"""

import json

note = []

def noteSection(item):
    return [x for x in note if x['item'] == item]

with open("../MAENI-dumps/student_note_content_202208052105.json", 'r') as f:
    jump = json.load(f)
    
note_db = jump['student_note_content']
note_ids = [329,359,389]

css = """<style type=\"text/css\" style=\"display: none !important;\">
        .alignleft {
        float: left;
        }
        .alignright {
        float: right;
        }
        
        .p1 { 
             line-height: 0px;
        }
        </style>"""
cc = 'chief cadfasdf'


for id in note_ids:
    note =  [x for x in note_db if x['student_note_id'] ==id] 
    html = css +  f"""<br><br><div id=\"headerBox\">
                <p class=\"alignleft\">
                ID: "+{cc}+"<br>
                </p>
                </div>
                <br><br><br><br>
                <h2 align=left>Chief Complaint</h2>
                <h2 align=left>History of Presenting Illness</h2>
                <h2 align=left>Review of Systems</h2>
                <h2 align=left>History</h2>
                <h3 align=left>Past Medical History</h3>
                <h3 align=left>Past Surgical History</h3>
                <h3 align=left>Medications</h3>
                <h3 align=left>Allergies</h3>
                <h3 align=left>Family History</h3>
                <h3 align=left>Social History</h3>
                <h2 align=left>Physical Exam</h2>
                <h3 align=left>Vitals</h3>
                <h3 align=left>Exam</h3>
                <h2 align=left>Data</h2>
                <h2 align=left>Assessment and Plan</h2>
                <h3 align=left>Summary Statement</h3>
                <p1 align=justify>
                ID: "+'Chief Complaint'+"<br>
                </p1>"""
    with open ('test.html', 'w') as f:
        f.write(html)