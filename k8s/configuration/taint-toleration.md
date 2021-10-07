## Taint & Toleration Commands

### Taint

kubectl taint nodes <NodeName> <key>=<value>:<Effect>

There are three types of effect
* NoSchedule
* PreferNoSchdule
* NoExecute

**Apply a taint**
```shell
$ kubectl taint nodes node1 key1=value1:NoSchedule
```

**Remove a taint**
Just add a "-v" sign at the end
```shell
$ kubectl taint nodes node1 key1=value1:NoSchedule-
```
