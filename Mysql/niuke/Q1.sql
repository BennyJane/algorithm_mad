/*
总结：
sum, max, min，count 函数，均会跳过null类型的值，且可以在不使用group by的情况下使用
avg() 函数：必须搭配group by方法使用
count(distinct case when <condition> then <res> else <res> end)
distinct key1, key2: 根据组合字段去重

round(value, limit)

if(condition, trueRes, falseRes)
ifnull(value, default)
case when <condition> then <res> else <res> end


using()函数：简化连表操作语句，表示两个表中都必须要存在该字段，且值相等
union
知识点是UNION后的排序问题，ORDER BY子句只能在最后一次使用。 如果想要在UNION之前分别单独排序，那么需要这样：
SELECT * FROM
( SELECT * FROM t1  ORDER BY 字段 ) newt1 ## 一定要对表重新命名，否则报错
UNION
SELECT * FROM
( SELECT * FROM t2  ORDER BY 字段 ) newt2



DATE_FORMAT(submit_time,'%Y%m')
DATE_FORMAT(submit_time,'%Y%m%d')
DAYOFMONTH(LAST_DAY(submit_time)) 统计当前月份的天数, dayofmonth(last_day(<time_str>))
select DATE('2020-01-01 10:00:00');  -》 2020-01-01

TimeStampDiff(SECOND, start_time, submit_time) < duration * 30

with <name> as (<子查询>); 给子查询命名，可重复使用
with rollup; 计算汇总数据

group_concat(distinct concat_ws(':', date(start_time), tag) SEPARATOR ';') as detail
group_concat: 行转列运用的group_concat()函数，可以将多行拼接为列函数group_concat([DISTINCT]
distinct
concat_ws


inner join left join right join full join

-- FIXME where语句需要放到join语句后面


*/


-- SQL4 SQL类别高难度试卷得分的截断平均值  ------------------------------------------------------

-- 执行速度快，但内存占用高
-- 如果使用count(e.id) 方法，则需要先过滤掉exam_record中score为null的数据
select m.tag,
       m.difficulty,
       round((sum(e.score) - max(e.score) - min(e.score)) / (count(e.score) - 2), 1) as clip_avg_score
from exam_record e
         join (select exam_id, tag, difficulty from examination_info where tag = 'SQL' and difficulty = 'hard') m
              on m.exam_id = e.exam_id;

-- 运行速度较慢，但内存使用较少
select tag,
       difficulty,
       round((sum(score) - max(score) - min(score)) / (count(score) - 2), 1) as clip_avg_score
from exam_record
         join examination_info using (exam_id)
where tag = "SQL"
  and difficulty = "hard";

-- SQL15 统计作答次数  ------------------------------------------------------
-- 总数: 选择非空字段统计
-- 排除null的总数：count函数自动跳过null
-- 排除null且不重复的总数： 需要结合distinct使用
select count(e.id)                                                                as total_pv,
       count(e.submit_time)                                                       as complete_pv,
       count(distinct case when e.score is not null then e.exam_id else null end) as complete_exam_cnt
from exam_record e;

-- 第三个指标的其他方案
select count(distinct if(t.score is not null, t.exam_id, null))
           as complete_exam_cnt
from exam_record t;
--select (select count(distinct exam_id) from exam_record) as complete_exam_cnt from exam_record t;

-- 可以执行，但写法不太推荐？默认检测为提示异常
select count(start_time) as total_pv,
       #有开始作答时间可视为一次作答 count(submit_time) as complete_pv,#有交卷时间可视为完成一次作答
count(distinct exam_id and score is not null)
as complete_exam_cnt #将试卷去重，同时将筛选完成的试卷
from exam_record;


-- SQL16 得分不小于平均分的最低分 -------------------------------------------------
-- order by score limit 1 => 可以更换为 min() 函数
select score as min_score_over_avg
from exam_record
where score >= (
    select avg(score)
    from exam_record
             join examination_info using (exam_id)
    where tag = "SQL"
)
  and exam_id in (select exam_id from examination_info where tag = "SQL")
order by score asc limit 1;

select min(score) as min_score_over_avg
from exam_record
         join examination_info using (exam_id)
where tag = "SQL"
  and score >= (
    select avg(score)
    from exam_record
             join examination_info using (exam_id)
    where tag = "SQL"
);

-- 使用with 语句，提取公共查询语句
with c as (
    select score
    from exam_record
             inner join examination_info using (exam_id)
    where tag = 'SQL'
)
select min(score) min_score_over_avg
from c
where score >= (select avg(score) from c);


-- SQL17 平均活跃天数和月活人数 -------------------------------------------------
select date_format(submit_time, '%Y%m') as month,
      round(
      (count(distinct uid, date_format(submit_time, '%Y%m%d')) / count(distinct uid)
      , 2) as avg_active_days,
      count(distinct uid) as mau
from exam_record where submit_time is not null
 and year(submit_time) = 2021
  group by date_format(submit_time, '%Y%m');

-- 该题的重点在于计算不同用户月活天数的总和，会有天数重复，要用distinct函数划分时间。另外，注意是2021年数据
select date_format(start_time,"%Y%m") as month,
       round(count(distinct uid,date_format(start_time,"%Y%m%d"))/count(distinct uid),2) as avg_active_days, # 计算月活平均天数,
       count(distinct uid) as mau # 计算月活人数
from exam_record
where score is not null and year(start_time)=2021
group by month


-- SQL18 月总刷题数和日均刷题数 -------------------------------------------------

-- 方案01
select coalesce (date_format(submit_time,'%Y%m'),'2021汇总') as submit_month,
count(submit_time) as month_q_cnt,
round (count(submit_time)/max(Day(last_day(submit_time))),3)as avg_day_q_cnt
from practice_record
where year(submit_time)=2021
group by date_format(submit_time,'%Y%m') with rollup;

-- 方案02
select
    submit_month,
    count(*) as month_q_cnt,
    round(count(*)/max(monthday),3) as avg_day_q_cnt #用了聚合函数所以必须加max，取出一个天数的值
FROM(
    select
        DATE_FORMAT(submit_time,'%Y%m') as submit_month,
        day(last_day(submit_time)) as monthday
    from practice_record
    where score is not null and year(submit_time)=2021
    ) AS dt
GROUP BY submit_month

union

select
    '2021汇总' as submit_month,
    count(*) as month_q_cnt,
    round(count(*)/31,3) as avg_day_q_cnt
from practice_record
where score is not null and year(submit_time)=2021
order by submit_month;

-- 方案03
select ifnull(y_m, '2021汇总') as submit_month,
    count(1) as month_q_cnt,
    round(count(1) / max(days_of_month), 3) as avg_day_q_cnt
from (
    select question_id,
        DAYOFMONTH(last_day(submit_time)) as days_of_month,
        DATE_FORMAT(submit_time, "%Y%m") as y_m
    from practice_record
    where year(submit_time)='2021'
) as t_month_stat
group by y_m
with rollup;

-- SQL19 未完成试卷数大于1的有效用户 -------------------------------------------------
-- 使用score统计会报错，因为存在score不为null，但start_time为null的测试数据
select uid, sum(if(submit_time is null, 1, 0)) as incomplete_cnt ,
            count(submit_time) as complete_cnt,
            group_concat(distinct concat_ws(':', date(start_time), tag) SEPARATOR ';') as detail
from exam_record join examination_info on exam_record.exam_id = examination_info.exam_id
where year(start_time) = 2021
group by uid
having count(submit_time) >= 1 and sum(if(submit_time is null, 1, 0)) between 2 and 4
order by sum(if(submit_time is null, 1, 0)) desc;


select uid, count(incomplete) as incomplete_cnt,
    count(complete) as complete_cnt,
    group_concat(distinct concat_ws(':', date(start_time), tag) SEPARATOR ';') as detail
from (
    select uid, tag, start_time,
        if(submit_time is null, 1, null) as incomplete,
        if(submit_time is null, null, 1) as complete
    from exam_record
    left join examination_info using(exam_id)
    where year(start_time)=2021
) as exam_complete_rec
group by uid
having complete_cnt >= 1 and incomplete_cnt BETWEEN 2 and 4
order by incomplete_cnt DESC;


-- SQL20 月均完成试卷数不小于3的用户爱作答的类别 --------------------------------------------
-- ERROR: 应该计算用户每月平均答题数量 -》 平均数
-- 最后返回值，统计数量，只能使用count(tag), 使用submit_time字段报错，因为最后统计tag是可以包含未提交的试卷信息的
select tag, count(tag) as tag_cnt
from exam_record
join examination_info using(exam_id)
where uid in (
    select uid
    from exam_record
    -- 因为计算月份时，不能使用count忽略不满足条件的数据，所以需要提前处理
    where submit_time is not null
    group by uid
    having count(submit_time) / count(distinct DATE_FORMAT(submit_time, '%Y%m')) >= 3
)
group by tag
order by tag_cnt desc;

-- SQL21 试卷发布当天作答人数和平均分 --------------------------------------------

-- 使用in 结合子查询
select
    exam_id,
    count( distinct uid ) as uv,
    round(avg( score ), 1) as avg_score
from exam_record
where (exam_id, date(start_time)) in (
    select exam_id, date(release_time)
    from examination_info where tag = "SQL"
) and uid in ( select uid from user_info where `level` > 5 )
GROUP BY exam_id
ORDER BY uv DESC, avg_score ASC;


-- 理解where语句进行三表相连操作： 保留所有数据
-- 三表相连：以exam_record表为主
select
    d2.exam_id,
    count(distinct d1.uid) as uv,
    round(avg(d2.score),1) as avg_score
from user_info d1,exam_record d2,examination_info d3
where d1.uid=d2.uid and d2.exam_id=d3.exam_id
and tag='SQL'
and d1.level>5
and d2.score is not null
and date(d3.release_time)=date(d2.start_time)
group by d2.exam_id
order by uv desc,avg_score asc

-- SQL22 作答试卷得分大于过80的人的用户等级分布 --------------------------------------------
-- 参考上一道题目：使用where多表连接
select
    -- 不去重，也可以通过
    level, count(score) as level_cnt
from user_info d1,exam_record d2,examination_info d3
where d1.uid=d2.uid and d2.exam_id=d3.exam_id
and tag='SQL'
and score > 80
group by level
order by level_cnt desc;
-- 使用join on 进行多表连接
-- FIXME 统计数量需要去重：即同一个人多次重复回答超过80
-- 存在数量相同的测试用例，所以还是需要对level排序
select level, count(distinct t1.uid) as level_cnt
from exam_record t1 join examination_info t2
on t1.exam_id = t2.exam_id
join user_info t3
on t1.uid = t3.uid
where tag='SQL'
and score > 80
group by level
order by level_cnt desc, level desc;

-- SQL23 每个题目和每份试卷被作答的人数和次数 --------------------------------------------
-- 考察 UNION 使用后排序与子排序不同
-- 计算pv时，需要将没有完成提交，即submit_time为null也考虑进入
select *  from (
    select exam_id as tid, count(distinct uid) as uv, count(start_time) as pv
    from exam_record group by exam_id order by uv desc , pv desc
) t1

union all
select * from (
     select question_id as tid, count(distinct uid) as uv, count(submit_time) as pv
    from practice_record group by question_id order by uv desc , pv desc
) t2


-- 使用tid左侧第一个数来排序
select exam_id as tid, count(distinct exam_record.uid) uv,
COUNT(*) pv FROM exam_record
GROUP BY exam_id

UNION

select question_id as tid, count(distinct practice_record.uid) uv,
COUNT(*) pv FROM practice_record
GROUP BY question_id

ORDER BY LEFT(tid,1) DESC, uv DESC, pv DESC;

-- SQL24 分别满足两个活动的人 --------------------------------------------
-- 所有值都大于85 ==》 即最小值大于85； 或者 使用子查询
select distinct uid, 'activity1' as activity
from exam_record
where uid not in (select distinct uid from exam_record where score <85 and year(start_time) = 2021)) and year(start_time) = 2021;



select uid, 'activity1' as activity
from exam_record
where year (start_time) = 2021
group by uid
having min (score) >= 85
union
select distinct uid, 'activity2' as activity
from exam_record
         join examination_info using (exam_id)
where difficulty = 'hard' and score > 80 and year (start_time) = 2021
  and TimeStampDiff(SECOND
    , start_time
    , submit_time)
    < duration * 30
order by uid;


-- SQL25 满足条件的用户的试卷完成数和题目练习数 --------------------------------------------

select m1.uid,
       COUNT(DISTINCT m2.id) AS exam_cnt,
       COUNT(DISTINCT m3.id) AS question_cnt
from (
         select t1.uid
         from exam_record t1
            , user_info t2
            , examination_info t3
         where t1.uid = t2.uid
           and t1.exam_id = t3.exam_id
           and tag = 'SQL'
           and difficulty = 'hard'
           and level = 7
         group by uid
         having avg(t1.score) > 80
     ) m1
         left join exam_record m2 on m1.uid = m2.uid and year (m2.submit_time) = 2021
    left join practice_record m3
on m1.uid = m3.uid and year (m3.submit_time) = 2021
GROUP BY uid
ORDER BY exam_cnt, question_cnt DESC;



select tmp1.uid, ifnull(exam_cnt, 0) exam_cnt, ifnull(question_cnt, 0) question_cnt
from (
         select e1.uid as uid, count(score) as exam_cnt
         from exam_record e1
         where year (start_time) = 2021
         group by e1.uid
         having e1.uid in ( select t1.uid
             from exam_record t1
              , user_info t2
              , examination_info t3
             where t1.uid = t2.uid
            and t1.exam_id = t3.exam_id
            and tag = 'SQL'
            and difficulty = 'hard'
            and level = 7
             group by uid
             having avg (t1.score)
              > 80)
     ) tmp1
         FULL JOIN
     (select p1.uid as uid, count(score) as question_cnt
      from practice_record p1
      where year (submit_time) = 2021
      group by p1.uid
      having p1.uid in (
          select t1.uid
          from exam_record t1
           , user_info t2
           , examination_info t3
          where t1.uid = t2.uid
         and t1.exam_id = t3.exam_id
         and tag = 'SQL'
         and difficulty = 'hard'
         and level = 7
          group by uid
          having avg (t1.score)
           > 80
          )
     ) tmp2
     on tmp1.uid = tmp2.uid
order by exam_cnt asc, question_cnt desc;


-- SQL26 每个6/7级用户活跃情况 --------------------------------------------

select t2.uid,count(distinct t1.s1) as a1,
        count(distinct case when t1.s2 like '2021%' then t1.s2 else null end) as a2,
        count(distinct case when t1.s2 like '2021%' and md1=1 then t1.s2 else null end),
        count(distinct case when t1.s2 like '2021%' and md1=2 then t1.s2 else null end)
from(
    -- 挑选需要字段，将两表union，竖向连接，主要解决活跃月份的数据统计
select uid,left(submit_time,7) as s1,left(submit_time,10) as s2,1 as md1
from exam_record

union all

select uid,left(submit_time,7) as s3,left(submit_time,10) as s4,2 as md2
from practice_record) as t1

right join (
select uid
from user_info
where level=6 or level=7) as t2
on t1.uid=t2.uid
group by t2.uid

order by a1 desc,a2 desc

-- SQL27 每类试卷得分前3名 --------------------------------------------
select tag as tig, uid, score as ranking
from examination_info
join exam_record using(exam_id)
group by tag
order by

select tag, uid, ranking
from(
    select tag, e_r.uid,
    row_number() over (partition by tag order by tag, max(score) desc, min(score) desc, e_r.uid desc) as ranking
    from exam_record e_r join examination_info e_i
    on e_r.exam_id = e_i.exam_id
    group by tag, e_r.uid
)ranktable
where ranking <= 3

