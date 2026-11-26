# 📓 Project Work Log: KUD

---

## 📅 26-11-2026

### 🔹 Task 1: Resolve Missing M.A Rank Students in Address List Report
- **Page / Report**: Convocation / Address List Report
- **Issue**: M.A rank holder students were not appearing in the generated Address List report.
- **Solution / Resolution**: Identified that administrative filters were set to query `InPerson` attendees, but the candidate records were recorded as `Absentia`; updated the attendance mode status to `InPerson` in the backend database for these eligible rank holders so they populate correctly.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Configure New Academic Stream — Master of Technology (M.Tech)
- **Requirement / Scope**: Introduce and configure the "Master of Technology" postgraduate stream in the university master tables.
- **Solution / Resolution**: Created and configured the new Master of Technology stream with necessary stream codes and academic master parameters.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 25-11-2026

### 🔹 Task 1: Adjust Font Size in Crystal Report
- **Requirement / Issue**: Modify font size within the Crystal Report layout to improve document presentation.
- **Solution / Implementation**: Opened the Crystal Report definition, navigated to the Formula Workshop / tab, and updated the formula to set the desired font size.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Resolve Stream Missing from Selection List
- **Issue**: Academic stream was not appearing in the active selection dropdown list.
- **Solution / Resolution**: Identified a mismatch in the stream group name mapping; corrected the stream group name, and the stream immediately appeared in the selection list.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 24-11-2026

### 🔹 Task 1: Configure New Academic Stream — Master of Journalism and Mass Communication
- **Requirement**: Introduce and configure the new post-graduate academic stream: "Master of Journalism and Mass Communication" in the system.
- **Solution / Implementation**: Inserted and mapped the new stream definitions, stream code, and eligibility parameters in the backend database masters.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 18-11-2026

### 🔹 Task 1: Resolve Candidate Count Mismatch in Audit Summary (Follow-up from 17-11)
- **Original Date**: `17-11-2026`
- **Page**: `Admin/AuditSummary.aspx`
- **Issue**: Total Candidates count did not equal `InPerson + Absentia` due to non-rank holders having inconsistent attendance mode records.
- **Solution / Resolution**: Standardized non-rank holder attendance modes for Academic Year 2024–25 via backend database update:
  ```sql
  UPDATE [ApplicationMaster] 
  SET isPerson = 0, PersonAbsentia = 'Absentia'
  WHERE AcademicYear = '24-25' 
    AND (PersonAbsentia = 'Person' OR isPerson = '1') 
    AND isRankHolder != '1'
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

### 🔹 Task 2: Add Annual / Earlier / All Filter Dropdown to Audit Summary (Follow-up from 17-11)
- **Original Date**: `17-11-2026`
- **Page**: `Admin/AuditSummary.aspx`
- **Requirement**: Provide a dropdown allowing administrative users to filter summary metrics by *Annual*, *Earlier*, or *All*.
- **Solution / Resolution**: Added the dropdown control to the filter panel and integrated the selected parameter into the backend summary aggregation queries.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

<br/>

## 📅 17-11-2026

### 🔹 Task 1: Investigate Candidate Count Mismatch in Audit Summary
- **Page**: `Admin/AuditSummary.aspx`
- **Issue**: Total Candidates count does not equal the sum of `InPerson` + `Absentia` candidate counts (`Total != InPerson + Absentia`).
- **Solution / Next Steps**: Audit backend aggregation queries and group-by logic in `AuditSummary.aspx.cs` to identify unmapped/NULL attendance modes causing the discrepancy.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 18-11-2026)*

---

### 🔹 Task 2: Add Annual / Earlier / All Filter Dropdown
- **Page**: `Admin/AuditSummary.aspx`
- **Requirement**: Provide a new dropdown allowing administrative users to filter summary metrics by *Annual*, *Earlier*, or *All*.
- **Solution / Next Steps**: Add the dropdown control to the filter panel and wire it into the summary query parameters.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 18-11-2026)*

---

<br/>

## 📅 12-11-2026

### 🔹 Task 1: Batch Update M.Com 2024–25 Students to Absentia Mode
- **Issue**: Several M.Com students mistakenly selected `InPerson` mode instead of `Absentia`.
- **Solution**: Executed backend SQL script targeting M.Com 24–25 batch:
  ```sql
  UPDATE [ApplicationMaster]
  SET isperson = 0, personAbsentia = 'Absentia'
  WHERE StreamGroup = 'MCOM' AND batch = '24-25'
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Investigate MBA Student Appearing in M.Com Student Filter
- **Issue**: An MBA student record unexpectedly appeared within the M.Com student list.
- **Root Cause & Solution**: Identified user operational issue—staff had chosen the `"ALL"` stream group filter instead of isolating the specific stream group. Guided staff to select the dedicated `"MCOM"` stream group filter.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 11-11-2026

### 🔹 Task 1: Correct Result Declaration Date and Confercode for M.Com 2024–25 Batch
- **Issue**: Declaration date incorrectly recorded as `15-04-2025` instead of `18-12-2024` for MCOM batch.
- **Solution**: Executed backend SQL update in `[ApplicationMaster]`:
  ```sql
  UPDATE [ApplicationMaster] 
  SET CONFERCODE = '52', DateofDeclaration = '18-12-2024'
  WHERE DateofDeclaration = '15-04-2025' AND StreamGroup = 'MCOM'
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 07-11-2026

### 🔹 Task 1: Add "Outstanding" Class Obtained in Crystal Report
- **Issue**: An "Outstanding" classification was recently introduced in the project business logic, but was missing from the Crystal Report layout.
- **Solution**: Updated the Crystal Report template to include and map the "Outstanding" class obtained field.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

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
