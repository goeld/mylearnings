## Services

**Service Types**
- NodePort
- ClusterIP
- LoadBalancer (This is usually in cloud providers)

[Node Port](./Service_NodePort.png)
**Note:**
>When you use expose command, it will use the pod's label as selectors.

```shell
$ k expose pods nginx --port=6379 --name service-nginx

OR 

$ k create service service-clusterip 
```