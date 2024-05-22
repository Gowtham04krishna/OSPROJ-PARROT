class VariablePartition:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.partitions = []
        self.memory_map = {}

    def add_partition(self, start_address, size):
        self.partitions.append((start_address, size))

    def allocate_memory(self, process_id, memory_required):
        for i, partition in enumerate(self.partitions):
            start_address, size = partition
            if size >= memory_required:
                self.memory_map[process_id] = (start_address, memory_required)
                self.partitions[i] = (start_address + memory_required, size - memory_required)
                return True
        return False
    
    def deallocate_memory(self, process_id):
        if process_id in self.memory_map:
            start_address, size = self.memory_map[process_id]
            self.partitions.append((start_address, size))
            del self.memory_map[process_id]
            return True
        return False
    
    def display_memory_map(self):
        print("Memory Map:")
        if not self.memory_map:
            print("No allocated memory.")
        else:
            for process_id, (start_address, size) in self.memory_map.items():
                print("Process", process_id, ": Start Address", start_address, ", Size", size)
        print("")
def main():
    total_memory = int(input("---> Enter total available memory: "))
    memory_manager = VariablePartition(total_memory)
    #******************************************************************************************
    num_partitions = int(input("---> Enter number of partitions: "))
    for i in range(num_partitions):
        start_address = int(input("---> Enter start address for partition {}: ".format(i+1)))
        size = int(input("---> Enter size for partition {}: ".format(i+1)))
        memory_manager.add_partition(start_address, size)
    #******************************************************************************************
    num_processes = int(input("---> Enter number of processes: "))
    for i in range(num_processes):
        process_id = i + 1
        memory_required = int(input("---> Enter memory required for process {}: ".format(process_id)))
        if memory_manager.allocate_memory(process_id, memory_required):
            print("Memory allocated for process", process_id)
        else:
            print("Memory allocation failed for process", process_id)
    #******************************************************************************************
    memory_manager.display_memory_map()


if __name__ == '__main__':
    main()