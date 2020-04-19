import pandas as pd

rfm_score("Cody Hodge")

def rfm_score(name):
    user = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/user_details.csv')
    rfm = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/customer_segmented.csv')
    promotion = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/promotion.csv')

    user_df = pd.DataFrame(user)
    rfm = pd.DataFrame(rfm)
    promotion = pd.DataFrame(promotion)
    #
    # print(user_df)
    # print(rfm)
    # print(promotion)

    user_merge = user_df.merge(rfm, on='user_id')
    # df1.merge(df2, left_on='lkey', right_on='rkey')
    # print(user_merge.columns)
    #
    user_det = user_merge[user_merge["First Name"] == name]
    # a = (user_det['user_id'])
    # print(a)
    a = user_det['RFMScore']
    print(user_det)
    print(a)
    if a[1] <= 244:
        promotion_det = promotion[promotion['promotion_id'] == 1]
        # if user_det['RFMScore'] >244 & user_det['RFMScore'] <344:
        if a[1] > 244 & a[1] < 344:
            promotion_det = promotion[promotion['promotion_id'] == 2]
        # if user_det['RFMScore'] >=344:
        if a[1] >= 344:
            promotion_det = promotion[promotion['promotion_id'] == 3]
    # rfm_score = rfm[rfm['user_id'] == 4]
    # # print(user_det)
    # print(rfm_score)
    print(promotion_det)
