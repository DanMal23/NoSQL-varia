
# quering sets and sorted sets in Redis (Remote Directory Server)
# Redis is a key-value database

import redis
redis.__version__ # '3.3.11'

# creating redis client
rc= redis.Redis(host = '127.0.0.1', port = 6379, db =0)
rc.set('nosql','Cassandra')
# print(client.get('nosql')) # b'Cassandra'

# creating 2 sets:
rc.sadd('Redis', 'key-value db', '2009', 'by Salvatore Sanfilippo')
rc.sadd('Cassandra','column', '2008', 'by Lakshman & Malik')

# show all members of a set:
print(rc.smembers('Redis')) # {b'key-value db', b'2009', b'by Salvatore Sanfilippo'}

# number of members in a set:
print(rc.scard('Cassandra')) # 3

# removing one
print(rc.spop('Redis',1)) # [b'key-value db']
print(rc.smembers('Redis')) # {b'by Salvatore Sanfilippo', b'2009', b'S. Sanfilippo'}
print(rc.sadd('Redis', 'S. Sanfilippo')) # inserts from the head
print(rc.smembers('Redis')) # {b'by Salvatore Sanfilippo', b'2009', b'S. Sanfilippo'}

# removing specified member
print(rc.srem('Redis','by Salvatore Sanfilippo'))
print(rc.smembers('Redis')) # {b'key-value db', b'S. Sanfilippo'}
print(rc.sadd('Redis', '2009'))
print(rc.smembers('Redis')) # {b'key-value db', b'2009', b'S. Sanfilippo'}

# sorted sets - memebers can be sorted
# sorting is based on scores,

nosql_dbs = "noSQLs"
name1 = "Cassandra"
year1 = 2008
name2 = "MongoDB"
year2 = 2009
name3 = "Redis"
year3 = 2009

rc.zadd('nosql_dbs', {name1: year1, name2: year2, name3: year3})
# show all values in a set:
print(rc.zrange('nosql_dbs',0,3)) 
# [b'Cassandra', b'MongoDB', b'Redis']

# adding new items
name4 = "Google Bigtable"
year4 = 2005
name5 = "Oracle NoSQL Database"
year5 = 2011
rc.zadd('nosql_dbs', {name4: year4, name5:year5})

# sorted set in descending order
print(rc.zrange('nosql_dbs', 0, -1, desc=True)) 
# [b'Oracle NoSQL Database', b'Redis', b'MongoDB', b'Cassandra', b'Google Bigtable']

# sorted set with years
print(rc.zrange('nosql_dbs', 0, -1, withscores=True))
# [(b'Google Bigtable', 2005.0), (b'Cassandra', 2008.0),
# (b'MongoDB', 2009.0), (b'Redis', 2009.0), (b'Oracle NoSQL Database', 2011.0)]

# sorting based on a range of scores

print(rc.zrangebyscore('nosql_dbs', min=2009, max=2011,withscores = True))
# range of scores in reverse orders

print(rc.zrevrangebyscore('nosql_dbs', min=2009, max=2011,withscores = True))

# removing elements
print(rc.zrem('nosql_dbs', "Cassandra", "MongoDB")) # 2
print(rc.zrange('nosql_dbs', 0, -1, desc=True)) 
print(rc.zrange('nosql_dbs', 0, -1, desc=True, withscores = True)) 
# [b'Oracle NoSQL Database', b'Redis', b'Google Bigtable']

# removing elem by year - range of years
print(rc.zremrangebyscore('nosql_dbs', 2009, 2009))
print(rc.zrange('nosql_dbs', 0, -1, withscores = True)) 

