# 🧠 Resume Keyword Optimizer (ATS Based)

An ATS-style Resume Keyword Optimizer built using **Python and DSA fundamentals**.  
This tool analyzes how well a resume matches a job description based on keywords and provides improvement suggestions.

---

## 📌 Problem Statement

Many resumes get rejected by **Applicant Tracking Systems (ATS)** because they miss important job-specific keywords.  
Candidates often don’t know **what skills are missing** or **how compatible** their resume is with a job role.

---

## 💡 Solution

This project compares **resume keywords** with **job description keywords** and generates:
- Match percentage
- Missing skills
- ATS-style evaluation (Excellent / Strong / Average / Weak)
- Actionable improvement suggestions

---

## ⚙️ How the Project Works (Flow)

1. Take resume keywords as input  
2. Take job description keywords as input  
3. Convert text to lowercase  
4. Remove punctuation and stop words  
5. Remove duplicate keywords  
6. Compare resume and JD keywords  
7. Calculate match percentage  
8. Generate ATS-style report and suggestions  

---

## 🧠 Data Structures & Concepts Used

- String processing
- Lists (Arrays)
- Linear search
- Keyword comparison
- Conditional decision logic
- Time Complexity: **O(n × m)**

---

## 🎯 ATS Decision Logic

| Match Percentage | Status          |
|-----------------|-----------------|
| 90% - 100%          | Excellent Match |
| 75% - 89%          | Strong Match    |
| 50% – 74%       | Average Match   |
| < 50%           | Weak Match      |

---

## 🚀 Future Improvements

- Keyword weightage for important skills  
- Technical vs Soft skill categorization  
- HashSet optimization for **O(n + m)** complexity  
- GUI or Web-based version  

---

## 🏁 Author

**Nitin Singh**  
B.Tech CSE Student  
Python & DSA Beginner Project  

⭐ If you like this project, feel free to star the repository!
