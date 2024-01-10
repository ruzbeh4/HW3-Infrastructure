from decouple import config
import nginx, os

DJANGO_REPLICAS= config('DJANGO_REPLICAS')
GO_REPLICAS= config('GO_REPLICAS')
print(os.environ)
c = nginx.loadf('default.conf')
server = c.server
list = []
for i in range(0, int(DJANGO_REPLICAS)):
    list.append(nginx.Key('server', ('http://127.0.0.1:' + str(9000+i))))
for i in range(0, int(GO_REPLICAS)):
    list.append(nginx.Key('server', ('http://127.0.0.1:' + str(8000+i))))

u = nginx.Upstream('backend',
*list)
c = nginx.Conf()
c.add(server)
c.add(u)

nginx.dumpf(c, 'default.conf')