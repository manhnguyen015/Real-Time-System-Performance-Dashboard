import psutil
import time
import pyodbc
from datetime import datetime

con = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};Server=localhost\\SQLEXPRESS;Database=master;Trusted_Connection=yes;TrustServerCertificate=yes;")
cursor = con.cursor()

while 1 == 1:
    Time = datetime.now()
    # Get CPU usage
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    # CPU interrupts
    cpu_interrupts = psutil.cpu_stats().interrupts
    cpu_calls = psutil.cpu_stats().syscalls

    # NMemory data
    memory_used = psutil.virtual_memory().used
    memory_free = psutil.virtual_memory().free

    # Bytes data
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_received = psutil.net_io_counters().bytes_recv

    # Disk data
    disk_usage = psutil.disk_usage("/").percent

    cursor.execute("USE system_information")

    # Insert data into SQL Server
    cursor.execute(
    "INSERT INTO dbo.Performance (Time, cpu_usage, memory_usage, cpu_interrupts, cpu_calls, memory_used, memory_free, bytes_sent, bytes_received, disk_usage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        Time,
        cpu_usage,
        memory_usage,
        cpu_interrupts,
        cpu_calls,
        memory_used,
        memory_free,
        bytes_sent,
        bytes_received,
        disk_usage,
    ),
)

    con.commit()
    time.sleep(1)
