# Core Concepts

>Part 1 <br> 
>*   Know very well how to create a Pod manifest via CLI.
>*  Practice command to create the command a pod, output to yaml file.

> Part 2
> - Be aware not everything can be modified within a live object. 
> - 3 Step Approach
>	- In case you need to modify, practice to save object's manifest file,  delete object and create object again from the manifest file.

### Pods [Notes](core_concepts/pods.md)
  - [ ] Basic Pod [Yaml](./core_concepts/pod-nginx.yaml)	
  - [ ] Pod - Command & Arguments [Yaml](./core_concepts/pod-command-args.yaml)
  - [ ] Pod - Another Command [Yaml](./core_concepts/pod-commands.yaml)	
  - [ ] Pod - Port [Yaml](./core_concepts/pod-ports.yaml)
  - [ ] Pod - PVC Claim [Yaml](./state-persistence/pvc-pod.yaml)
  - [ ] Pod - Config map 
    - [ ] Pod - Config map - Whole [Yaml](./configuration/pod-configmap-all.yaml)
    - [ ] Pod - Config Map - Single Value [Yaml](./configuration/pod-configmap-single-value.yaml)
    - [ ] Pod - Config Map - From Volume [Yaml](./configuration/pod-configmap-from-volume.yaml)
  - [ ] Pod - Secrets 
    - [ ] Pod - Secrets - Whole [Yaml](./configuration/pod-secret-all.yaml)
    - [ ] Pod - Secrets - Single Value [Yaml](./configuration/pod-secret-single-value.yaml )
    - [ ] Pod - Secrets - From Volume [Yaml](./configuration/pod-secret-from-volume.yaml)
  - [ ] Pod - Toleration [Yaml](./configuration/pod-toleration.yaml)
  - [ ] Pod - Node Selector [Yaml](./configuration/node-selector.yaml) / [Notes](configuration/node-selector.md)
  - [ ] Pod - Resource requests

### Deployment - Replicaset - Replication Controller [Notes](core_concepts/deployment-replicaset-replica-controller.md)	
  - [x] Replicaset [Yaml](./core_concepts/replicaset.yaml)
  - [x] ReplicationController
  - [x] Deployment [Yaml](./core_concepts/deployment.yaml)
  - [ ] Comparison - Replication Controller vs Replicaset vs Deployment[Notes](core_concepts/deployment-replicaset-replica-controller.md)  

###  Namespaces [Notes](core_concepts/namespaces_resource-quota_limit-range.md)
  - [x] Basic understanding [Yaml](./core_concepts/namespace.yaml)
  - [ ] Resource Quota [Yaml](./core_concepts/resource-quota.yaml) / [Notes](core_concepts/namespaces_resource-quota_limit-range.md)
  - [ ] LimitRange [Yaml](./core_concepts/limitrange.yaml) / [Notes](core_concepts/namespaces_resource-quota_limit-range.md)
    


# Configuration
> Part 1
> - Be very familiar with basics of creating a config map
> - Know how you can mount config map to container on specific path via volumes. 

> Part 2
> - Have a basic understanding of Security Context.
> - understand runAsUser, runAsGroup and fsGroup

> Part 3
> - Having a good idea of resource quota
> - You should know about request quota and limits and should know how to set them at Pod level.
> - Know what will happen if Node does not have match the minimum request values.

> Part 4
> - Having a good understanding of Secrets is important.
> - Know how to create secret and mount them as environment variable and volumes.
> - Be familiar with environment variables.

> Part 5
> - You should know how you can associate a service account with existing deployments or with a Pod.
> - Know that each namespace has its own service account.



- [x] Commands & Arguments in Kubernetes
- [x] Entrypoint and Command in docker
     - [ ] Comparison [Image](./configuration/docker-entrypoint-command.png)
- [x] Config Maps [Yaml](./configuration/configmap.yaml)
    - [ ] Pod config map - All [Yaml](./configuration/pod-configmap-all.yaml)
    - [ ] Pod Config Map - Single Value [Yaml](./configuration/pod-configmap-single-value.yaml)
    - [ ] Pod Config Map - From Volume [Yaml](./configuration/pod-configmap-from-volume.yaml)
- [x] Secret
  - [ ] Basic Secrets[Yaml](./configuration/secrets.properties)
  - [ ] Secrets No Encoding [Yaml](./configuration/secrets-no-encoding.yaml)
    - [ ] Pod Secrets - All [Yaml](./configuration/pod-secret-all.yaml)
    - [ ] Pod Secrets - Single Value [Yaml](./configuration/pod-secret-single-value.yaml)
    - [ ] Pod Secrets - From Volume [Yaml](./configuration/pod-secret-from-volume.yaml)
    
- [ ] Security Context [Yaml](./configuration/pod-security-context.yaml)
- [x] Resource Requirements / Resource Limits
- [x] Taints
    - [ ] Taint Toleration[Commands](./configuration/taint-toleration.md) 
- [ ] Toleration
    - [ ] Taint Toleration[Commands](./configuration/taint-toleration.md)
    - [ ] Pod Toleration [Yaml](./configuration/pod-toleration.yaml)
- [ ] Affinity
    - [ ] Pod Node Affinity [Yaml](./configuration/pod-node-affinity.yaml)
    - [ ] Node Affinity [Docs](./configuration/affinity.md)
- [ ] Node Selector
    - [ ] Pod Node Selector [Yaml](./configuration/node-selector.yaml)
- [ ] Node Affinity - Node Selector Comparison  

# Multi Container pods

> Part 1
> - Be prepared for the questions based on the sidecar pattern
> - Practice questions related to HAProxy and FluentD 10 times before you sit for the exam.



- [x] Multiple containers in a pod
  - [ ] Ambassador Pattern
  - [ ] Sidecar Pattern
  - [ ] Adapter Pattern

    [Documentation on Patterns](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/)

# Observability

> Part 1
> - Understanding of Probes (Liveness & Readiness) are very important for the exams.
> - Know differences among them. 
> - Exam will not mention either of them directly however will mention the use-case instead and you would need to know which one to implement. 
> - Be aware of scenario on editing liveness/readiness probe of existing POD object. You can not do it on a live object.
> - Be aware of troubleshooting question related to this. 

> Part 2
> - Be aware of container logging command.
> - "kubectl logs" command is good enough for CKAD exam.
> - Also be aware how you can fetch the events associated with a POD.
> 	- kubectl describe pods <pod-name>
> 	- kubectl get events -o wide --field-selector=involvedObject.Name=nginx

> Part 3
> - Metrics server is preinstalled, so you do not have to worry about installation
> - Be familiar with on how you can use CPU/memory usage of specific pod or nodes.
> 	- kubectl top pods
> 	- kubectl top nodes

> Part 2
> - There will be many debugging related questions in the exam.
> - Be prepared with debugging aspect of related to various areas like:
> 	- Network Policies
> 	- Services
> 	- Liveness/Readiness Probe
> 	- Deployments
    

- [x] Readiness probe
- [x] Liveness probe
- [x] Container Logging
- [ ] Monitor and debug applications
- [ ] Monitoring nodes and pods
- [ ] Monitoring components
- [ ] Kubernetes events

# Pod Design

> Part 1
> - Be familiar with labels and selectors
> - Know on how you can apply to an object (both via manifest file as well as live modification)
> - Network policies also work based on the labels and selectors. For troubleshooting them you need to follow 3 step approach as above.

> Part 2
> - Be aware of deployments creation, and modification aspect. 
> - Understand the importance of labels and selectors in the deployments. 
> - Have a glimpse about maxSurge and maxUnavailable in deployments and how to modify them.
> - Be very thorough with rolling updates and rollbacks.

> Part 3
> - Be very familiar with creating Jobs and CronJobs.
> - Don't worry about setting cron job date/times.
> - Dedicate time to understand activeDeadlineSeconds  parameter within cron job.
  

- [ ] Labels, Selectors, Annotations
- [x] [Rolling updates & Rollback](./pod-design/rollout.md)
	- [x] Rollout strategies
        - [ ] RollingUpdate 
        - [ ] Recreate
- [ ] Jobs [Yaml](./pod-design/jobs.yaml)
- [ ] CronJobs [Yaml](./pod-design/cronjob.yaml)


# Services & Networkings

> Part 1
> - Be very familiar with NodePortService.
> - Understand the difference between service port and target port.
> - Try out a scenario where you have to change a service port of a live service object. 
> - Be ready to troubleshoot any question related to service.

> Part 2
> - Be very familiar with network policies.
> - Know that the network policies are attached to objects based on the label. 
> - Be ready to troubleshoot questions related to network policies.
  

- [ ] Services & End Points
- [ ] Ingress
- [ ] Egress
- [ ] Network Policies

# State Persistence

> Part 1
> - Be familiar with PV (Persistent Volume) and PVC  (Persistent Volume Claim)
> - For PV pay attention to hostPath and emptyDir
> - Exam question will not say you will need to use emptyDir but will give you a use case instead and you have to figure it out yourself. 
> 	- e.g., create a pod and attach a volume to it on path of /mounts in such a way that volume should be deleted once the pod is removed.


- [x] Volumes
- [x] Persistent Volume [Yaml](./state-persistence/pv.yaml)
- [x] Persistent Volume Claims 
   - [ ] Create PVC [Yaml](./state-persistence/pvc.yaml)
   - [ ] PVC Claim from Pod [Yaml](./state-persistence/pvc-pod.yaml) 


# Sep 2021 Onwards
- [x] Docker image
- [ ] Authentication
- [ ] Authorisation
- [ ] Certificates
- [ ] Roles
	- [ ] Role Base Access Controls - RBAC
	- [ ] Cluster Roles
- [ ] Admission Controller
- [ ] Helm Chart
