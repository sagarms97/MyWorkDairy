# 📓 Project Work Log: KUD

---

## 📅 05-11-2026

### 🔹 Task 1: Crystal Reports Display Failure / Error
- **Error**: `cers#cert_rpt#16u10828#4465#22-23#0#-1#abs-admin#1258`
- **Solution**: Built the latest project code and copied the compiled `release` folder contents into the Crystal Reports directory.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Adjust Font Size in Crystal Report
- **Application**: Crystal Report Designer
- **Solution**: Opened the Crystal Report file (`.rpt`), navigated to **Format Field**, updated font size styling, and saved changes.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 3: Specialization Displaying Incorrectly for Specific Departments
- **Issue**: Departments beginning with `"POST GRADUATE IN..."` do not have specializations, yet a specialization entry is erroneously displayed in their student details.
- **Solution**: Investigate codebase logic and corresponding database tables to conditionally hide the specialization field for these post-graduate departments.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

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
