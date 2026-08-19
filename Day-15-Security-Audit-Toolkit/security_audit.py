import os
import sys
import platform
import socket
import json
import subprocess
from datetime import datetime

def get_system_specs():
    return {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": sys.version.split()[0],
        "hostname": socket.gethostname()
    }

def audit_open_ports():
    target = "127.0.0.1"
    common_ports = [21, 22, 80, 443, 3306, 8080, 5432]
    open_ports = []
    
    print("\nScanning local common ports for exposure...")
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

def get_disk_usage():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic logicaldisk get caption, freespace, size", shell=True).decode()
            return output.strip()
        else:
            output = subprocess.check_output("df -h", shell=True).decode()
            return output.strip()
    except Exception as e:
        return f"Could not retrieve disk specs: {e}"

def generate_audit_report():
    print("\n--- GENERATING SYSTEM SECURITY & RESOURCE AUDIT ---")
    specs = get_system_specs()
    open_ports = audit_open_ports()
    
    report = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "system_specs": specs,
        "open_local_ports": open_ports if open_ports else "No common risky ports open locally",
        "audit_status": "PASSED ✅" if not open_ports else "WARNING: Open ports detected ⚠️"
    }

    print("\n" + "=" * 60)
    print("             SYSTEM SECURITY & RESOURCE AUDIT             ")
    print("=" * 60)
    print(f" Timestamp      : {report['timestamp']}")
    print(f" Hostname       : {specs['hostname']}")
    print(f" OS / Arch      : {specs['os_name']} ({specs['architecture']})")
    print(f" Python Exec    : {specs['python_version']}")
    print(f" Local Ports    : {report['open_local_ports']}")
    print(f" Audit Status   : {report['audit_status']}")
    print("=" * 60 + "\n")

    return report

def export_report_to_json(report):
    file_name = "system_audit_report.json"
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"Success: Full audit exported to '{os.path.abspath(file_name)}'\n")
    except Exception as e:
        print(f"Error exporting report: {e}\n")

def main():
    report_cache = None
    while True:
        print("==================================================")
        print("    SYSTEM RESOURCE & SECURITY AUDIT TOOLKIT    ")
        print("==================================================")
        print(" 1. Run Complete System Audit")
        print(" 2. View Disk Space & Storage Diagnostics")
        print(" 3. Export Last Audit Report (.JSON)")
        print(" 4. Exit Suite")
        print("==================================================")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            report_cache = generate_audit_report()
        elif choice == "2":
            print("\n" + "=" * 60)
            print("                STORAGE DIAGNOSTICS                ")
            print("=" * 60)
            print(get_disk_usage())
            print("=" * 60 + "\n")
        elif choice == "3":
            if report_cache:
                export_report_to_json(report_cache)
            else:
                print("\nPlease run a system audit first (Option 1)!\n")
        elif choice == "4":
            print("\nCongratulations on graduating the 15-Day Python Challenge! Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == "__main__":
    main()