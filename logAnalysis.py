import psycopg2

DBNAME = "news"

q1 = """
    select title, count(*) as views from articles ,
    log where concat('/article/' , articles.slug) = 
    log.path group by articles.title order by views desc 
    limit 3;
"""

q2 = """
    select authors.name , count(*) as views from articles ,
    log , authors where concat('/article/' , articles.slug) 
    = log.path and authors.id = articles.author group by 
    authors.name order by views desc;
"""

q3 = """
    select * from (select a.day , round(cast((100*b.error) as numeric) 
    / cast(a.total as numeric), 2) as p_error from
    (select date(time) as day, count(*) as total from log group by day) as a
    join
    (select date(time) as day, count(*) as error from log where status
    like '%404%' group by day) as b on a.day = b.day) as c where p_error > 1.0;
"""

def get_report(q):
    """get report from news database."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    q_result = c.fetchall()
    db.close()
    return q_result

def query_1_report(q):
    q_result = get_report(q)
    print('\n1.The most popular three articles of all time:\n')
    for result in q_result:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def query_2_report(q):
    q_result = get_report(q)
    print('\n2.The most popular article authors of all time are:\n')
    for result in q_result:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def query_3_report(q):
    q_result = get_report(q)
    print('\n3.Days with more than 1% of request that lead to an error:\n')
    for result in q_result:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' %')

if __name__ == '__main__':
    # print query result
    query_1_report(q1)
    query_2_report(q2)
    query_3_report(q3)
