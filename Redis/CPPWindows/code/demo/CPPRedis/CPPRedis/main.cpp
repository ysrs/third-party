#include <hiredis.h>
#include <win32fixes.h>
#include <iostream>
#include <string>


using namespace std;

class Redis
{
public:
    Redis()
    {
        m_pContext = nullptr;
    }

    ~Redis()
    {
        redisFree(m_pContext);
        m_pContext = nullptr;
    }

    bool connect(string host, int port)
    {
        auto bRet = true;
        m_pContext = redisConnect(host.c_str(), port);
        if (m_pContext && m_pContext->err)
        {
            cout << "connect error: " << m_pContext->errstr << endl;
            bRet = false;
        }
        return bRet;
    }

    string get(string key)
    {
        auto pReply = (redisReply*)redisCommand(m_pContext, "GET %s", key.c_str());
        string str = pReply->str;
        freeReplyObject(pReply);
        return str;
    }

    void set(string key, string value)
    {
        redisCommand(m_pContext, "SET %s %s", key.c_str(), value.c_str());
    }

private:
    redisContext* m_pContext;
};


int main()
{
    Redis* r = new Redis();
    if (!r->connect("127.0.0.1", 6379))
    {
        cout << "connect error!" << endl;
        return 0;
    }
    r->set("name", "Hello");
    cout << "Get the name is " << r->get("name").c_str() << endl;
    delete r;

    return 0;
}

