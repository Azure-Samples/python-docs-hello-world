itorres2 = User(user='itorres2@deepdatas.com', password='1234', azure_item_id='test_id')
fbloise = User(user='fbloise@deepdatas.com', password='2345', azure_item_id='test_id')
mgarcia = User(user='mgarcia@deepdatas.com', password='3456', azure_item_id='test_id')

db.session.add_all([itorres2])

db.session.commit()



print(itorres2.user)

db.drop_all()
db.create_all()