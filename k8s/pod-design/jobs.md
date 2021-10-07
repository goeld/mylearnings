**Note**
- completions: No of times the jobs should complete successfully.
- parallelism : No of jobs that can run in parallel
- backofflimit: 
	- default is 6 if not mentioned
	- you may increase

# Jobs	
```shell
kubectl get jobs
kubectl describe jobs
kubectl describe jobs my-job
kubectl create -f my-jobs.yaml
kubectl delete jobs my-job
```



# Cron Jobs

```shell
kubectl get cronjobs
kubectl describe cronjobs
kubectl describe cronjobs my-cronjob
kubectl edit cronjob my-cronjob
kubectl create cronjob my-job --image=busybox --schedule="1 * * * *" --dry-run=client -o yaml > prac_test_dom_2_q5.yaml


```