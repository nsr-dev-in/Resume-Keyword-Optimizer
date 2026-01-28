# MENU 
print("""
=================================================
        Resume Keyword Optimizer (ATS Based)
=================================================
This program follows the below processing flow:

1. Input Resume Keywords
2. Input Job Description Keywords
3. Preprocess Text (Lowercase, Cleanup)
4. Remove Stop Words
5. Compare Keywords
6. Calculate Match Percentage
7. Show Missing Keywords
=================================================
""")

# TAKING INPUT FROM USER 
resume_text=input("Enter Your Resume Keywords : ")
jd_text=input("Enter Job Description Keywords : ")


if resume_text == "" or jd_text == "":
    print("Please enter both Resume and Job Description")

# CONVERT TO LOWERCASE
resume_text=resume_text.lower()
jd_text=jd_text.lower()

# REMOVE UN-WANTED PUNCTUATIONS 
# REPLACE PUNCTUATIONS MARKS WITH BLANK SPACES
punctutations=",.!?"
for p in punctutations:
    resume_text=resume_text.replace(p,"")
    jd_text=jd_text.replace(p,"")

# SPLIT INTO WORDS (LIST)
resume_words=resume_text.split()
jd_words=jd_text.split()

# REMOVE EXTRA / UN-WANTED / STOPPING WORDS 
print("")
unwanted_words = [
    "and", "or", "but", "so", "while", "although", "though",
    "for", "with", "of", "in", "on", "at", "by", "from",
    "a", "an", "the", "this", "that", "these", "those",
    "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did",
    "very", "really", "quite", "just", "somewhat",
    "maybe", "probably", "mostly", "kind", "sort",
    "worked", "helped", "assisted", "involved", "responsible","looking"
]

# FILTERING USER RESUME
resume_filtered=[]
for word in resume_words:
    if word not in unwanted_words:
        resume_filtered.append(word)

# FILTERING JOB DESCRIPTION 
jd_filtered=[]
for word in jd_words:
    if word not in unwanted_words:
        jd_filtered.append(word)

#print(jd_filtered)

# REMOVE DUBPLICATE 
jd_filtered = list(set(jd_filtered))

#print(jd_filtered)

# COMPARING AND FIND MISSING WORDS
matched=0
matched_keywords=[]
missing=[]

for word in jd_filtered:
    if word in resume_filtered:
        matched+=1
        matched_keywords.append(word)
    else:
        missing.append(word)

# MATCHED PERCENTAGE
match_percentage=(matched/len(jd_filtered))*100
match_percentage=round(match_percentage,2)

#BASIC DECISION CASES
status=""
decision=""

if match_percentage >= 90:
    status= "Excellent Match"
    decision="Resume is Highly Compatible with this Job."

elif match_percentage >= 75 and match_percentage <= 89:
    status= "Strong Match"
    decision= "Resume meets Most Job Requirements."

elif match_percentage >= 50 and match_percentage<=74:
    status= "Average Match"
    decision="Resume Needs Improvement"
else:
    status="Weak Match"
    decision="Resume not suitable For This Role."


# FINAL OUTPUT
print(f"""
=================================================
        Resume Keyword Optimizer Report
=================================================
Total JD Keywords    : {len(jd_filtered)}

Matched Keywords     : {matched_keywords}
Missing Keywords     : {missing}

Match Percentage     : {match_percentage}%

--- ATS Evaluation ---
Status               : {status}
Decision             : {decision}

Suggestion           : Add these skills → {missing}
=================================================
""")