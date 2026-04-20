# Emergency Room Triage System
## Heap-Based Priority Queue Implementation

### Simulation Dashboard
![Emergency Room Triage Dashboard](screenshots/dashboard.png)

> Interactive version: open `dashboard.html` in your browser for live charts.

### Project Overview
This project implements an Emergency Room Triage System using a Max Heap priority queue. 
Patients are treated based on priority (10=Most Critical, 1=Least Critical) rather than 
arrival time, simulating real hospital triage systems.

### Course Information
- **Course:** Design and Analysis of Algorithms
- **Language:** Java
- **Data Structure:** Array-based Max Heap
- **Indexing:** Zero-based (Parent(i) = floor((i-1)/2))

### Features Implemented
- ✅ Array-based Max Heap with zero-based indexing
- ✅ insert() - O(log n)
- ✅ extractMax() - O(log n)  
- ✅ increasePriority() - O(log n)
- ✅ isEmpty() - O(1)
- ✅ maxHeapify() - O(log n)
- ✅ buildMaxHeap() - O(n) Floyd's Algorithm
- ✅ 1000+ synthetic patient dataset
- ✅ 24-hour ER simulation with random arrivals
- ✅ CSV input/output for all data
- ✅ Complete complexity analysis with proofs
- ✅ Real-world relevance discussion

### CSV Files Generated
| File | Description | Columns |
|------|-------------|---------|
| `data/patients.csv` | Initial 1000+ patients | PatientID, Priority, Hour, Minute, Second |
| `data/arrivals.csv` | New patients during simulation | PatientID, Priority, Hour, Minute, Second |
| `data/treatments.csv` | Complete treatment log | PatientID, Priority, ArrivalTime, TreatmentTime |
| `data/results.csv` | Final statistics | Statistics and hourly report |

### How to Compile and Run

#### Using Command Line:
```bash
# Navigate to project directory
cd EmergencyRoomTriage

# Compile
javac emergency/room/triage/system/EmergencyRoomTriage.java

# Run
java emergency.room.triage.system.EmergencyRoomTriage
