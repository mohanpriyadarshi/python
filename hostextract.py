#!/usr/bin/env python
import hostlist
hosts=hostlist.expand_hostlist("ap100[8-88],{ap,ac}[1-3]")
hostrange=hostlist.collect_hostlist(hosts)
print hosts
print hostrange
