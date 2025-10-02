# Import required libraries
import multiprocessing
import time
import logging

# ------------------ Logging Setup ------------------
logging.basicConfig(
    filename='process_log.txt',   # Log file
    level=logging.INFO,           # Logging level
    format='%(asctime)s - %(processName)s - %(message)s'
)

# ------------------ Process Function ------------------
def system_process(task_name):
    """Simulates a system process by logging start and end, with delay."""
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate process execution
    logging.info(f"{task_name} ended")

# ------------------ Main Program ------------------
if __name__ == '__main__':
    print("System Starting...")

    # Create processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    print("System Shutdown.")
