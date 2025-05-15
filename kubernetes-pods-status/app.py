from kubernetes import client, config

config.load_kube_config()  # loads ~/.kube/config
v1 = client.CoreV1Api()
def pods_view():

    if(user_input == 1):
        print("Listing pods:")
        for pod in v1.list_pod_for_all_namespaces().items:
            print(f"{pod.metadata.namespace} - {pod.metadata.name}")

    elif(user_input == 2):
        print("Running Pods:")
        for pod in v1.list_pod_for_all_namespaces().items:
            if(pod.status.phase == "Running"):
                print(f"{pod.metadata.namespace} - {pod.metadata.name}")

    elif(user_input == 3):
        print("Not Running Pods:")
        for pod in v1.list_pod_for_all_namespaces().items:
            if(pod.status.phase != "Running"):
                print(f"{pod.metadata.namespace} - {pod.metadata.name}")

    else:
        print("Incorrect Value !!!! Please Enter the Value Correctly...")
        return True

while True:
    user_input = int(input("\n Enter the choice you want to display: 1.) Listing all pods 2.) Listing Running pods 3.) Not Run) To Exit  \n"))
    if(user_input == 0):
        print("Thankyou...")
        break
    pods_view()
