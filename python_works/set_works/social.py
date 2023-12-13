insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopy","lalu"}
mohanlal_followings={"prithvi","vijay","lalu"}
mohanlal_suggestions=insta_users.difference(mohanlal_followings)
mohanlal_suggestions.discard("mohanlal")
print(mohanlal_suggestions)

dq_friends={"prithvi","fahad","sureshgopy","lalu"}
mutual_friends=dq_friends.intersection(mohanlal_followings)
print(mutual_friends)



