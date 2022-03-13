# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import redis


# 普通连接方式
redis_conn = redis.Redis(host='127.0.0.1', port=6379)

# 连接池连接方式
# redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# redis_conn = redis.Redis(connection_pool=redis_pool)

# redis中字符返回值类型都是字节（bytes）类型


def get_name():
    name_1 = redis_conn.get("name_1")
    print(str(name_1, 'utf-8'))

    try:
        name_2 = redis_conn.get("name_")
        print(str(name_2, 'utf-8'))
    except BaseException:
        print("exception")


def get_names():
    names = redis_conn.mget('name_1', 'name_2')
    name_s = [str(name, 'utf-8') for name in names]
    print(name_s)


def test_string_single():
    redis_conn.set("name_1", "张三")
    redis_conn.set("name_2", "李四")
    get_name()


def test_string_multiple():
    # redis_conn.mset(name_1='张三', name_2='李四')
    names = {
        'name_1': '张三',
        'name_2': '李四'
    }
    redis_conn.mset(names)
    get_names()


def test_list():
    sz = redis_conn.lpush("list_1", 1, 1, 1, 1, 1)
    # print(sz)
    # print(redis_conn.llen('list_1'))
    # print(redis_conn.lpop('list_1'))
    # print(redis_conn.llen('list_1'))
    # print(redis_conn.lrange('list_1', 0, 20))
    # print(redis_conn.rpop('list_1'))
    # print(redis_conn.lrange('list_1', 0, 20))

    print(redis_conn.lrange('list_1', 0, 20))
    print(redis_conn.lrem('list_1', 2, 1))
    print(redis_conn.lrange('list_1', 0, 20))


def test_hash():
    # print(redis_conn.hset('hash_1', 'key_1', 'value_1'))
    # print(redis_conn.hset('hash_1', 'key_2', 'value_2'))
    # print(redis_conn.hget('hash_1', 'key_1'))
    print(redis_conn.hkeys('hash_1'))
    print(redis_conn.hvals('hash_1'))
    print(redis_conn.hgetall('hash_1'))
    print(redis_conn.hlen('hash_1'))


def test_set():
    print(redis_conn.sadd('set_1', 'val_1', 'val_2', 'val_3', 'val_4'))
    # print(redis_conn.smembers('set_1'))
    # print(redis_conn.spop('set_1'))
    print(redis_conn.smembers('set_1'))
    print(redis_conn.srem('set_1', 'val_1', 'val_3'))
    print(redis_conn.smembers('set_1'))


def test_zset():
    mapping = {
        '1': 10,
        '1': 20,
        '1': 30,
        '2': 40,
        '2': 50,
        '3': 60
    }
    print(redis_conn.zadd('zset_1', mapping))
    print(redis_conn.zrange('zset_1', 0, 3))
    print(redis_conn.zrangebyscore('zset_1', 10, 60))
    # print(redis_conn.zrem('zset_1', '1', '2'))
    # print(redis_conn.zremrangebyrank('zset_1', 1, 2))
    print(redis_conn.zremrangebyscore('zset_1', 10, 30))


def test_keys():
    print(redis_conn.keys())
    # print(redis_conn.type('list_1'))
    # print(redis_conn.exists('list_1'))
    # print(redis_conn.delete('list_1'))
    # print(redis_conn.exists('list_1'))
    # print(redis_conn.expire('myzset', 60))
    # print(redis_conn.persist('myzset'))
    print(redis_conn.ttl('myzset'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test_string_single()
    # test_string_multiple()
    # test_list()
    # test_hash()
    # test_set()
    # test_zset()
    test_keys()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
