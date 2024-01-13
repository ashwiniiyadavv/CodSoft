import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'UserID': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4,1,1,2,3],
    'BookID': [101,103, 101, 102, 103, 101, 102, 103, 101, 103,102,104,104,104],
    'Rating': [5, 3, 4, 5, 2, 3, 2, 4, 5, 3,4,4,3,2]
}
# creating a data frame using pandas
data_df=pd.DataFrame(data)
user_book_matrix=data_df.pivot(index="UserID",columns="BookID",values="Rating").fillna(0)
print(user_book_matrix)
#calculating similarity using cosine similarity
user_similarity=cosine_similarity(user_book_matrix.fillna(0))
user_similarity=pd.DataFrame(user_similarity,index=user_book_matrix.index,columns=user_book_matrix.index)
def recommend(userid):
    user_ratings=user_book_matrix.iloc[userid-1]
    weighted_sum=user_similarity.iloc[userid-1].dot(user_book_matrix)
    recommended_books=weighted_sum[user_ratings==0].sort_values(ascending=False)
    return recommended_books
if __name__=="__main__":
    user_id=int(input("Enter userId :")) 
    print(f"Recommended books from most to least likely :\n\n {recommend(user_id)}")
    print(f"\nMost Recommended: {recommend(user_id).index[0]}")

