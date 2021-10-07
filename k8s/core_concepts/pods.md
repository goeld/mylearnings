
## Pod
Pods Status
- ContainerCreating
- Pending
- Running

Pod Conditions
- PodScheduled
- Initialised
- ContainerReady
- Ready


### Pod Phase

**Pending**	
  >The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.

**Running**	
  > The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting.

**Succeeded**	
  > All containers in the Pod have terminated in success, and will not be restarted.

**Failed**	
  > All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system.

**Unknown**	
  > For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.
  > 



# Pod Commands
### Basic commands
```shell
$ alias k=kubectl
$ k get pods
$ k get pods -l env=pods
$ k describe pods
$ k describe pod(s) my_pod
$ k edit pods my_pod
$ k run my_pod  --image=nginx --dry-run=client - o yaml > mypod.yaml
$ k apply -f mypod.yaml
$ k create -f mypod.yaml
$ k label pods mypod key=value 
```


### Pod with label
```shell
$ alias k=kubectl
$ k run pods my-pod-with-label --labels=key1=value1,key2=value2
```

### Pod with Port
```shell
$ alias k=kubectl
$ k run pods my-pod-port --port=8080 

$ k run pod deploy-label --image=nginx --replicas=3 --labels=m=n --dry-run=client -o yaml --port=80
```