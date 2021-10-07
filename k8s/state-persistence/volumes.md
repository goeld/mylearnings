# Persistent Volumes

There are 3 parts to it 
1. Yaml to create persistent volume. - Done by Administrator
2. Yaml file to claim (request) the persistent volume. (Done by User)
3. Yaml file in the pod to reference the PVC

```shell
$ kubectl get persistentvolumes
$ kubectl get pv
$ kubectl describe persistentvolumes

$ kubectl get pvc
$ kubect describe pvc
```

[Volumes Dynamic Provisioning](Volumes%20-%20Dynamic-Provisioning.png)

