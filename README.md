Simple base for MySQL to use and implement in your code towards your likings.

When adding a account to the database the table will look like this






+----+------------------------------------------------------------------+----------+------------------------------------------------------------------+
| id | email                                                            | username | password                                                         |
+----+------------------------------------------------------------------+----------+------------------------------------------------------------------+
|  1 | b526b164bb1971ee9d90e000a0b16e4f2207921e0a3ea99a4a9df831f398c022 | xHookah  | 284d96fc795db926af662fde7c9b871009fd828877132899a16107fcc55a2624 |
+----+------------------------------------------------------------------+----------+------------------------------------------------------------------+






 id = for every account that gets added it will automatically increment the id by + 1.
 
 email = When the email is entered it will hash the email and store it in the row/table to protect against data-breaches.
 
 password = When the password is entered it will hash the password and store it in the row/table to protect against data-breaches.
 
 This has been made as a simple base for those who would like to learn off a simple program and implement it towards their own code/program.
 
 Later on the future i will be making an advanced version of this program that will cover sanitize input, protect against SQL Injections and using the full indexing thats possible towards MySQL.
