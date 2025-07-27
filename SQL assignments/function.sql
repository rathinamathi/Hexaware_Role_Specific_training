alter function dbo.fn_getListPriceByProdId
( @product_id int)
returns decimal(10,2)
begin
declare @listPrice decimal(10,2)
select @listPrice = list_price from production.products
where product_id=@product_id
return @listPrice
end

SELECT dbo.fn_getListPriceByProdId(10) AS ProductPrice;

create function dbo.fn_getProdByCategoryId
( @category_id int)
returns table
as 
return
(
select * from production.products where category_id = @category_id
);

SELECT * FROM dbo.fn_getProdByCategoryId(2);


create function dbo.getSalesamntbyStoreId
( @store_id int)
returns decimal(18,2)
begin
declare @total_amount decimal(20,2);
select @total_amount = sum(oi.list_price*oi.quantity)
from sales.orders o
join sales.order_items oi
on o.order_id = oi.order_id
where o.store_id = @store_id

return @total_amount;
end;

SELECT dbo.getSalesamntbyStoreId(3) AS TotalSales;

create function dbo.fn_getOrdrsBtwnDates
( @date1 date, @date2 date)
returns @orders table
( order_id int, order_date date, store_id int, customer_id int)
as
begin
insert into @orders 
select order_id,order_date,store_id,customer_id
from sales.orders
where order_date between @date1 and @date2

return;
end;

SELECT * FROM dbo.fn_getOrdrsBtwnDates('2016-01-01', '2016-12-31');


create function dbo.fn_cntProByBrand
( @brand_id int)
returns int
as
begin
declare @total_cnt int;
select @total_cnt = count(*)
from production.products
where brand_id=@brand_id

return @total_cnt;
end;

SELECT dbo.fn_cntProByBrand(8) AS BrandProductCount;



