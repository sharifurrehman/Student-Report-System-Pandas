import pandas as pd

# -----------------------------
# Step 1: Create Student Dataset
# -----------------------------

data = {
    "Name": ["Sharif ur Rehman", "Ahmed", "Sara", "Fatima", "Usman", "Ayesha", "Hamza"],
    "Course": ["Python", "Python", "AI", "AI", "Django", "Django", "Python"],
    "Marks": [85, 72, None, 91, 44, None, 88]
}

df = pd.DataFrame(data)

print("========== Original Dataset ==========")
print(df)

# -----------------------------
# Step 2: Clean Missing Marks
# -----------------------------

average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)

print("\n========== Missing Marks Cleaned ==========")
print(df)

# -----------------------------
# Step 3: Add Pass / Fail Column
# -----------------------------

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\n========== Pass / Fail ==========")
print(df)

# -----------------------------
# Step 4: Students with 80+ Marks
# -----------------------------

top_students = df[df["Marks"] >= 80]

print("\n========== Students with 80+ Marks ==========")
print(top_students)

# -----------------------------
# Step 5: Course Wise Average
# -----------------------------

course_average = df.groupby("Course")["Marks"].mean()

print("\n========== Course Wise Average ==========")
print(course_average)

# -----------------------------
# Step 6: Sort Highest to Lowest
# -----------------------------

sorted_students = df.sort_values(by="Marks", ascending=False)

print("\n========== Sorted Students ==========")
print(sorted_students)

# -----------------------------
# Step 7: Export Files
# -----------------------------

sorted_students.to_csv("student_report.csv", index=False)

sorted_students.to_json("student_report.json", orient="records", indent=4)

print("\nCSV File Saved Successfully!")

print("JSON File Saved Successfully!")
