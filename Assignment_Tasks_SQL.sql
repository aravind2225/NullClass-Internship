use sales ;

-- TASK 1

select s.sku_name,s.category, sum(o.qty_ordered ) as net_sales
from order_detail o join sku_detail s on o.sku_id=s.id
where year(o.order_date)=2022 and o.is_valid=1 and s.category="Mobiles & Tablets"
group by s.sku_name,s.category order by net_sales desc 
limit 5;


-- TASK 2 

with cust_tab as(
select o.customer_id, abs(round(sum(o.after_discount-s.cogs),2)) as PCB,
case 
when round(sum(o.after_discount-s.cogs),2)<0 then "LOSS"
when round(sum(o.after_discount-s.cogs),2)<100 then "LOW"
when round(sum(o.after_discount-s.cogs),2)>=100 and round(sum(o.after_discount-s.cogs),2)<500 then "MEDIUM"
when round(sum(o.after_discount-s.cogs),2)>=500 then "HIGH"
end as "Segment"
from order_detail o join sku_detail s on o.sku_id=s.id
where o.is_valid=1
group by o.customer_id
)
select Segment, round(sum(PCB),2) as net_Pofit_Per_Segment from cust_tab
group by Segment;












