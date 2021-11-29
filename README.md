# second_project

Note to Roger given the extra time for revisions

Although I wanted to, I chose not revise the notebook itself since I figured that transforming seemingly repetitive functions to for loops did not help much (and I might afraid that if I mess around to much, I might somehow break the code and it might take too long for me to fix it. 

But here is my attempt to improve a part:

For example, I had a code which looked like this in the original version.

df_type_1 = X_train[X_train['Cover_Type'] == 1]

df_type_2 = X_train[X_train['Cover_Type'] == 2]

df_type_3 = X_train[X_train['Cover_Type'] == 3]

df_type_4 = X_train[X_train['Cover_Type'] == 4]

df_type_5 = X_train[X_train['Cover_Type'] == 5]

df_type_6 = X_train[X_train['Cover_Type'] == 6]

df_type_7 = X_train[X_train['Cover_Type'] == 7]

I've tried to make a function (only works for this specific notebook since I did not want to have it to have too many arguments) and it looked like this:

def df_per_class(i):
    while i in range(7):
        df = X_train[X_train['Cover_Type'] == i]
        return df

df_1 = df_per_class(1)

df_2 = df_per_class(2)

df_3 = df_per_class(3)

df_4 = df_per_class(4)

df_5 = df_per_class(5)

df_6 = df_per_class(6)

df_7 = df_per_class(7)

For me, it still does not look to dry. I couldn't avoid the repetitions since I'm storing it to objects with its name in strings becoming different from one class to another. I think there is also a way do do for loops on strings but I am not yet that familiar with it yet.

Thank you!
