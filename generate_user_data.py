#generates json response which is then filled in database.
#python script to generate json response for a student enrolling in makemoocs.
#generates json response like this.
'''

{ 
"Name" : "Name1",
"Username" : "name1",
"Email" : "name1@gmail.com",
"Password" : "Name1@mm123",
"College" : "College2",
"Course" : "Course2",
"Expected_date_of_graduation" : "Year2",
"Interested" : ["Interest2" , "Interest1"],
"Aim_to" : "Aim3",
"Skills" : ["Skill2" , "Skill1"]
}
{ 
"Name" : "Name2",
"Username" : "name2",
"Email" : "name2@gmail.com",
"Password" : "Name2@mm123",
"College" : "College1",
"Course" : "Course1",
"Expected_date_of_graduation" : "Year1",
"Interested" : ["Interest1" , "Interest2"],
"Aim_to" : "Aim3",
"Skills" : ["Skill1" , "Skill2"]
}
'''

import random


college = ("College1" , "College2") # List of Colleges
course = ("Course1", "Course2") # List of courses
expect_graduate = ("Year1" , "Year2") # List of Expected_date_of_graduation
interested = ("Interest1" , "Interest2") # List of Interets availible
AimTo = ("Aim1", "Aim2" , "Aim3") # List of aims with which the candidate has enrolled
skillset = ("Skill1", "Skill2") # List of skills that a person already has

name=["Name1" ,"Name2"] # Names to be passed for whom to generate the json response



for x in name:
	print ("""{ 
\"Name\" : """ + "\""+x+"\"" + ",\n"
	"\"Username\" : \""+x.lower()+"\",\n"
	"\"Email\" : \""+x.lower()+"@gmail.com"+"\",\n"
	"\"Password\" : \""+x+"@mm123"+"\",\n"
	"\"College\" : \""+random.choice(college)+"\",\n"
	"\"Course\" : \""+random.choice(course)+"\",\n"
	"\"Expected_date_of_graduation\" : \""+random.choice(expect_graduate)+"\",\n"
	"\"Interested\" : [\""+'" , "'.join(random.sample(interested,2))+"\"],\n"	# 2 is no of elements in interested[]
	"\"Aim_to\" : \""+random.choice(AimTo)+"\",\n"
	"\"Skills\" : [\""+'" , "'.join(random.sample(skillset,2 ))+"\"]\n}" # 2 is no of elements in skillset[]
	)