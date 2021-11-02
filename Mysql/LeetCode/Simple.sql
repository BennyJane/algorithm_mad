# 175. 组合两个表
-- 左连接：显示左侧表所有数据，右表没有数据，使用null补充
-- 默认join语句为中连接，只显示两个表中都有数据的情况
select p.FirstName, p.LastName, t.City, t.State
from Person p
         right join Address t on p.PersonId = t.PersonId;

# 其他解决方案:子查询
select FirstName,
       LastName,
       (select City from Address a where a.PersonId = p.PersonId)  as City,
       (select State from Address a where a.PersonId = p.PersonId) as State
from Person p;

-- 补充内容：
/**
from子句中on条件主要用来连接表，其他不属于连接表的条件可以使用where子句来指定；
join连接分为三种，1内连接，2外连接，3交叉连接；
1：inner join ，默认，所以可以省略inner关键字
2：left outer join ，左外连接，结果表中除了匹配行外，还包括左表有而右表中不匹配的行，对于这样的行，右表选择列置为null
right outer join ，右外连接，结果表中除了匹配行外，还包括右表有而左表中不匹配的行，对于这样的行，左表选择列置为null
natural join，自然连接，分为natural left outer join和natural right outer join，语义定义与inner join相同
3：cross join，交叉连接，实际上就是将两个表进行笛卡尔积运算，结果表的行数等于两表行数之积
交叉连接可以归为内连接，不设置任何条件，就自动进行笛卡尔积运算。
 */


# 196. 删除重复的电子邮箱
-- 自连接：找到重复数据，然后，添加比较条件
-- 删除：使用delete,delete 语句中也可以使用条件查询等技巧
select p1.*
from Person p1,
     Person p2
where p1.Email = p2.Email
  AND p1.Id > p2.Id;

-- 窗口函数解法
delete
from Person
where id not in
      (select keep_id
       from (select min(Id) over (partition by Email) as keep_id
             from Person) t1);
-- 子查询
/**
  delete t1 from t1 left join t2 on t1.id = t2.id where t2.id = null;
  删除左连接后，t2表中id为null，即t1中id在t2中没有匹配到的记录
 */


-- 584. 寻找用户推荐人
-- ERROR: 缺失null记录
select name
from customer
where referee_id != 2;
-- CORRECT: 添加新的条件;NULL 需要使用is，而不是=
-- 不等于： != <> 两种方式
select name
from customer
where referee_id != 2
   or referee_id is NULL;

/**
  MYSQL使用三值逻辑，true false unknown
  任何值与NULL值比较，都会是unknown，也包括NULL自身对比；
  MYSQL提供了 is null 与 is not null 两种操作对比NULL
 */


-- 586. 订单最多的客户
select customer_number
from orders
group by customer_number
order by count(customer_number) desc
limit 1;
select customer_number, count(orders_number) as orders_sum
from orders
group by customer_number
order by orders_sum desc
limit 1;

-- 595. 大的国家
select name, population, area
from World
where area > 3000000
   or population > 25000000;
-- 优化： 不适用or，or造成索引失效
SELECT name,
       population,
       area
FROM world
WHERE area > 3000000
UNION
SELECT name,
       population,
       area
FROM world
WHERE population > 25000000;

/**
   对于单列来说，用or是没有任何问题的，
  但是or涉及到多个列的时候，每次select只能选取一个index，
  如果选择了area，population就需要进行table-scan，即全部扫描一遍，
  但是使用union就可以解决这个问题，
  分别使用area和population上面的index进行查询。
  但是这里还会有一个问题就是，UNION会对结果进行排序去重，
  可能会降低一些performance(这有可能是方法一比方法二快的原因），所以最佳的选择应该是两种方法都进行尝试比较。
 */

# 596. 超过5名学生的课
-- FIXME 每门课程中student存在重复值，如何去重？
-- count 嵌套 distinct使用
select class
from courses
group by class
having count(distinct student) >= 5;

-- 使用where
-- 子查询
select class, count(distict student) as num
from courses
group by class;
-- 嵌套语句
select temp.class
from (select class, count(DISTINCT student) as num from courses group by class) as temp
where temp.num >= 5;

SELECT class
FROM (SELECT class,
             COUNT(DISTINCT student) AS num
      FROM courses
      GROUP BY class) AS temp_table
WHERE num >= 5;

-- 597. 好友申请 I：总体通过率
-- 重点！！！
# 计算被通过的总数量
SELECT count(*) num
FROM RequestAccepted
GROUP BY requester_id, accepter_id;
# 计算不重复的申请数量
SELECT count(*) total
FROM FriendRequest
GROUP BY sender_id, send_to_id;

-- 子查询：必须使用as 定义新的表名
select round(
               IFNULL(
                           (select count(*) from (select distinct requester_id, accepter_id from RequestAccepted) as A)
                           /
                           (select count(*) from (select distinct sender_id, send_to_id from FriendRequest) as A)
                   , 0
                   ), 2
           ) as accept_rate;

SELECT CASE
           WHEN t.frc = 0 THEN 0.00
           ELSE round((
                          SELECT COUNT(DISTINCT requester_id, accepter_id)
                          FROM RequestAccepted
                      ) / t.frc, 2)
           END AS accept_rate
FROM (
         SELECT COUNT(DISTINCT sender_id, send_to_id) AS frc
         FROM FriendRequest fr
     ) t;


-- 进阶1:你能写一个查询语句得到每个月的通过率吗？


-- 进阶2：你能求出每一天的累计通过率吗？

-- 603. 连续空余座位
-- 重要！！！
-- FIXME 连续空余座位的定义是大于等于 2 个连续空余的座位
select seat_id
from cinema
where free = 1
order by seat_id asc;

-- 笛卡尔积：
select distinct a.seat_id
from cinema a
         join cinema b
              on abs(a.seat_id - b.seat_id) = 1
                  and a.free = true and b.free = true
order by a.seat_id;

select distinct s1.seat_id
from cinema s1,
     cinema s2
where s1.free = 1
  and s2.free = 1
  and (
        s1.seat_id = s2.seat_id - 1
        or
        s1.seat_id = s2.seat_id + 1
    )
order by s1.seat_id;


-- 1179. 重新格式化部门表
-- 核心
    -- case 语句对分组结果筛选，可以获取非筛选字段
    -- ==》 对比 having 语句，只能筛选一类数据，且只能对分组字段进行处理
    -- case when `expression` then `expression` end
    -- 聚合函数，处理null情况
SELECT id,
MIN(CASE WHEN month='Jan' THEN revenue END) AS Jan_Revenue,
AVG(CASE WHEN month='Feb' THEN revenue END) AS Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue END) AS Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue END) AS Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue END) AS May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue END) AS Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue END) AS Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue END) AS Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue END) AS Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue END) AS Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue END) AS Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue END) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id;

-- 1873. 计算特殊奖金
select a.employee_id,
       (CASE
         WHEN mod(a.employee_id, 2) = 1 AND a.name not like 'M%' THEN
          a.salary
         ELSE
          0
       END) bonus
  from Employees a
  order by a.employee_id

select
    employee_id,
    if(
        employee_id&1 and name regexp '^[^M]',
        salary,
        0
    ) as bonus
from employees
order by employee_id;

select
    employee_id,
    if(
        employee_id&1 and left(name, 1)<>'M',
        salary,
        0
    ) as bonus
from employees
order by employee_id;

select
    employee_id,
    salary * (
        employee_id&1 and substr(name, 1, 1)<>'M'
    ) as bonus
from employees
order by employee_id;

-- substr和substring都可以