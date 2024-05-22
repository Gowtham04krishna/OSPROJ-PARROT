import matplotlib.pyplot as plt

class Task:
    def __init__(self, id):
        self.id = id
        self.runtime = 0
        self.vruntime = 0

def execute_task(task):
    print(f"Executing task {task.id}")
    task.vruntime += 1

def find_next_task(tasks):
    return min(tasks, key=lambda task: task.vruntime)

def main():
    num_tasks = int(input("Enter the number of tasks: "))
    tasks = [Task(i) for i in range(num_tasks)]

    # Input task runtimes
    for task in tasks:
        runtime = int(input(f"Enter runtime for Task {task.id}: "))
        task.runtime = runtime

    # Simulate task execution
    gantt_data = []
    for time in range(sum(task.runtime for task in tasks)):
        next_task = find_next_task(tasks)
        execute_task(next_task)
        gantt_data.append((next_task.id, time))
        if(next_task.runtime == next_task.vruntime):
            tasks.remove(next_task)
            print(f"Task {next_task.id} completed at time {time+1}")


    # Plot Gantt chart
    fig, ax = plt.subplots()
    for task_id, time in gantt_data:
        ax.barh(task_id, 1, left=time, color='blue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Task ID')
    ax.set_title('Gantt Chart')
    ax.invert_yaxis()
    plt.show()

if __name__ == "__main__":
    main()