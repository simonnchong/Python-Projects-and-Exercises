student_dict = {
    "student" : ["Simon", "James", "Lily"],
    "score" : [56, 76, 98]
}

# # ------------------------------------------------------------- loop through dictionary -----------------------------------------------
for key, value in student_dict.items():
    print(key, value)
    # student ['Simon', 'James', 'Lily']
    # score [56, 76, 98]

import pandas as pd
student_dataframe = pd.DataFrame(student_dict)

print(student_dataframe)
#   student  score
# 0   Simon     56
# 1   James     76
# 2    Lily     98

# # #------------------------------------------------------------- loop through data frame -------------------------------------------------------------
for key, value in student_dataframe.items():
    print(key)
    # student
    # score   
    
    print(value) 
    # 0    Simon
    # 1    James
    # 2     Lily
    # Name: student, dtype: object
    # 0    56
    # 1    76
    # 2    98
    # Name: score, dtype: int64
      
    
# # ------------------------------------------------------------- loop through rows of dataframe -------------------------------------------------------------
for index, row in student_dataframe.iterrows():
    print(row)
    # student    Simon
    # score         56
    # Name: 0, dtype: object
    # student    James
    # score         76
    # Name: 1, dtype: object
    # student    Lily
    # score        98
    # Name: 2, dtype: object
    
    print(row.student)
    # Simon
    # James
    # Lily
    
    print(row.score)
    # 56
    # 76
    # 98
    
    if (row.student == "Simon"):
        print(row.score)
        # 56