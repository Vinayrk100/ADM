import pandas as pd

user = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/user_details.csv')
rfm = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/customer_segmented.csv')
promotion = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/promotion.csv')

user_df = pd.DataFrame(user)
rfm = pd.DataFrame(rfm)
promotion = pd.DataFrame(promotion)
user_merge = user_df.merge(rfm, on='user_id')
user_det = user_merge[user_merge["First Name"] == "Cody Hodge"]

a = user_det['RFMScore']

if a.values[0] <= 244:
       promotion_det = promotion[promotion['promotionid'] == 1]
if a.values[0] > 244 & a.values[0] < 344:
            promotion_det = promotion[promotion['promotionid'] == 2]
if a.values[0] >= 344:
            promotion_det = promotion[promotion['promotionid'] == 3]
# print(promotion_det.promotion_offer)
promo = promotion_det.values[0][1]
# promo = promotion_det[0][1]
print(promo)
