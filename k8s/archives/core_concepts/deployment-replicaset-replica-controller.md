
### Replicasets vs Deployments

> A ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless you require custom update orchestration or don't require updates at all.

# Deployment
### Commands

```shell
$ k create deployment my-deployment --image=nginx --replicas=3
$ k apply -f my-deployment.yaml
$ k create -f my-deployment.yaml
$ k set image deployment my-deployment my-pod-name=nginx:1.12 --record

kubectl get deployment
k get deployments --show-labels
kubectl describe deployments
kubectl describe deployments my-deployment
kubectl run my-deployment --image=nginx --replicas 3
kubectl apply -f my-deployment.yaml
kubectl create -f my-deployment.yaml
kubectl label nodes <node_name> <label_key>=<label_value>
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql # If the deployment named mysql's current size is 2, scale mysql to 3
kubectl set image deployment my-deployment nginx=nginx:1.9 --record
kubectl scale deployment my-deployment --relicas=10

```

### Deployment Rollout Commands

**Two important parameters when doing roll out.** 

maxSurge 
>Max numbers/percentage of pods that can be launched above the original configuration

maxUnavailable 
   >The numbers/percentage of  max number of pods that can go down.

```shell
$ k rollout status deployment my-deployment
kubectl rollout history deployment
$ k rollout history deployment my-deployment
$ k rollout undo deployment my-deployment
kubectl rollout undo deployment my-deployment --to-version=1
kubectl set image deployment my-deployment nginx=nginx:1.9 --record
```

### Label with Deployments
>Unlike pods deployments you can not have --labels when creating a deployment. You would need to create & then edit/apply. 

```shell

k create deployment deploy-label --image=nginx --replicas=3 --dry-run=client -o yaml --port=80 > deploy-label.yaml
k label deployments deploy-label j=k
k get deployments --selector j=k
```



# Replicaset
### Replicasets
```shell
$ alias k=kubectl
$ kubectl get replicasets
$ kubectl apply -f my-replicaset.yaml
$ kubectl create -f my-replicaset.yaml
$ k label rs my-replicaset new_la=new_va
$ k get rs --selector=new_la=new_va
$ kubectl delete replicaset my-replicaset
$ k scale --replicas=3 rs my-replicas
$ kubectl scale --replicas=3 rs/foo                # Scale a replicaset named 'foo' to 3
$ kubectl scale --replicas=3 -f foo.yaml              # Scale a resource specified in "foo.yaml" to 3
$ kubectl scale --replicas=5 rc/foo rc/bar rc/baz         # Scale multiple replication controllers
```


# Replication Controller
> **Note**: A Deployment that configures a ReplicaSet is now the recommended way to set up replication.

> A ReplicationController ensures that a specified number of pod replicas are running at any one time. In other words, a ReplicationController makes sure that a pod or a homogeneous set of pods is always up and available.

