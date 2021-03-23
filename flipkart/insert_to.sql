load data local INFILE "products.csv" into table books

fields terminated by ','
lines terminated by '/n'
ignore 1 lines

( Product_url, Product_name ,brand ,
Sale_price ,MRP , Discount_percentage ,Number_of_ratings ,Number_of_reviews,
Type_of_washing )

Error Code: 1054. Unknown column 'Product_url' in 'field list'
