# 📓 Project Work Log: KUD

---

## 📅 04-11-2026

### 🔹 Task 1: Deployment & Old Batch Confercode Configuration (Follow-up from 03-11)
- **Original Date**: `03-11-2026`
- **Issue**: Configure new confercode for pre-1992 student batches and publish updates.
- **Solution / Resolution**: Successfully added confercode and result declaration year mappings into the `[ConvocationConfirmation]` table. Built and published project updates to production.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

<br/>

## 📅 03-11-2026

### 🔹 Task 1: Create Separate Confercode for Pre-1992 Batch Students
- **Requirement**: Allocate distinct confercode series for pre-1992 batches.
- **Solution**: Configured confercode batch range from 250 to 300.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 04-11-2026)*

---

### 🔹 Task 2: Update Windows Application for Confercode Selection
- **Application**: Windows Desktop App
- **Solution / Progress**: Modified the `GetAnnualFilter` method to correctly target the new confercode range. Changes completed; building and releasing the new executable (`.exe`) file is pending.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 3: Annual / Earlier Code Mismatch During Admin Verification
- **Section Contact**: `8892225850`
- **Issue**: During administrative verification, students are receiving mismatched Annual/Earlier codes, forcing staff to update them manually.
- **Root Cause & Solution**: The system is currently deriving the Annual/Earlier code from the student's individual result declaration date. Instead, it must be updated to reference the designated **section declaration date** for accurate code generation.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 02-11-2026

### 🔹 Task 1: BSHM Stream Not Displayed in Designated Stream Group
- **Solution**: Corrected the stream group name mapping in the system.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

### 🔹 Task 2: Add Specialization Option
- **Solution**: Added Mechanical Specialization under the relevant stream.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---
