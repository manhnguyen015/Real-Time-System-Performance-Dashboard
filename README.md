# Live System Performance Monitoring

## Overview

This project enables real-time monitoring and recording of essential system performance metrics—including CPU usage, memory usage, network activity, and disk usage—into a SQL Server database (SQL Server Management Studio or Azure Data Studio). The collected data is stored and can be visualized and analyzed using Power BI with the included Power BI report file (System Performance.pbix).

## Features

- Real-time monitoring and data collection
- SQL Server database storage
- Visualization via Power BI dashboard

## Prerequisites

- **Python 3.x**
- **SQL Server**
- **Power BI Desktop**

### Python Libraries

Install the necessary libraries:

```bash
pip install psutil pymssql pyodbc
```

## Database Setup

1. Create a database (e.g., `SystemInformation`) and a table `Performance`:

```sql
CREATE TABLE Performance (
    Time DATETIME ,
    cpu_usage NUMERIC(5,2),
    memory_usage NUMERIC(5,2),
    cpu_interrupts NUMERIC(18,0),
    cpu_calls NUMERIC(18,0),
    memory_used NUMERIC(18,0),
    memory_free NUMERIC(18,0),
    bytes_sent NUMERIC(18,0),
    bytes_received NUMERIC(18,0),
    disk_usage NUMERIC(5,2)
);
```
### Docker Setup on macOS

If you are using macOS, you can run SQL Server in a Docker container. Here’s how to do it:

1. **Install Docker**: Make sure Docker Desktop is installed and running on your macOS.
2. **Pull the SQL Server image**:
    ```bash
    docker pull mcr.microsoft.com/mssql/server
    ```
3. **Run the SQL Server container**:
    ```bash
    docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourStrong!Passw0rd' \
    -p 1433:1433 --name sqlserver \
    -d mcr.microsoft.com/mssql/server
    ```

4. **Connect to the container** using Azure Data Studio by entering `localhost` as the server name and `SA` as the username with the password you set.

## Script Overview

The Python script:

1. **Collects metrics** with `psutil`
2. **Stores data** in SQL Server via `pyodbc` or `pymssql`
3. **Visualizes metrics** in Power BI, connecting to the `Performance` table.

## Usage

1. **Run the script** to start data collection.
2. **Visualize in Power BI** by connecting to SQL Server and designing a custom dashboard.

## License

Open-source under the MIT License.
