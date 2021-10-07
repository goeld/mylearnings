

- Nodes -> Worker machine, where container runs
- Cluster -> Set of nodes
- Master -> Another node configured as master
	- Responsible for orch of containers

Kubernetes Components
- API Server
	- Frontend for k8s.
- etcd
	- Distributed, reliable key store to store all data to manage cluster.
	- Responsible to implement logs to ensure there are no conflicts between the masters
- kubelet
	- Agent that run on each nodes
	- Ensure that containers are running as expected.
- Container runtime
	- Underlying software to run the containers
- Controller
	- Brain behind orc.
	- Responsible for noticing down when nodes, containers end point goes down
	- Makes decision to bring up new nodes, container end point goes down
- Schedular
	- Is responsible for distributing work across multiple nodes
    


Master Node Vs Worker Node
Master : Has Kube-apiserver, etcd, controller, schedular
Worker: Kubelet (agent), Container Runtime