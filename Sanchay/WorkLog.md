# 📓 Project Work Log: Sanchay

---

## 📅 05-11-2026

### 🔹 Task 1: Provide PO Preview Option Before Forwarding to Purchase Section
- **Page**: Store Section / `Purchase_order_report.aspx`
- **Issue**: Store in-charge is unable to verify saved PO details prior to transfer, leading to frequent PO reverts.
- **Solution**: Added a "PO Preview" button that navigates directly to `Purchase_order_report.aspx`, allowing verification before submission to reduce reverts.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Provide Edit Option for Item Specifications Without Affecting Master Data
- **Page**: Indent Management / Specification
- **Issue**: Operators require custom item specifications on the indent without altering the default specifications defined in the Item Master table.
- **Solution**: Provide an inline edit option for item specifications scoped strictly to the indent transaction without triggering an update to the master table.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 3: GRN and Invoice Uploads Displaying Same Document in Store Section
- **Page**: `Store_GoodsDelivery.aspx`
- **Issue**: Users upload separate files for GRN document and Invoice document, but after submission, opening the GRN document erroneously displays the uploaded Invoice document.
- **Solution**: Investigate file upload and binding logic in `Store_GoodsDelivery.aspx` and verify document storage paths/columns in the database table.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 04-11-2026

### 🔹 Task 1: Fix "Conversion failed" Error on PO Entry in Store Section (ApproxValue Column)
- **Page**: `Pages/Sections/PurchaseOrderForAwardedRFQ.aspx.cs`
- **Issue**: Received a SQL conversion failure exception when clicking the "PO Entry" button in the Store section caused by the `ApproxValue` column.
- **Solution**: Updated SQL query to safely parse `ApproxValue` as a decimal before evaluating `NULLIF`:
  ```sql
  ISNULL(NULLIF(TRY_CONVERT(decimal(18,2), d.ApproxValue), 0), ...)
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Change BLDE Association Name
- **Requirement**: Update the institutional name to **"Bharathia Lingayat Development Association"**.
- **Solution / Next Steps**: Planning and procedural review required; need to coordinate with the project team before applying database and interface changes.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 3: Item Description Field for Store In-Charge in PO (Follow-up from 03-11)
- **Original Date**: `03-11-2026`
- **Page**: PO Generation / Store Section
- **Requirement**: Provide a textbox allowing the Store In-charge to input a specific description for each item, displayed directly below the item on the PO.
- **Solution / Resolution**: Inspected and debugged the workflow; verified that item descriptions are already supported under the "Specification" field. Users can modify this specification during Indent Forwarding and Indent Reviewing, fulfilling the requirement without redundant schema changes.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

<br/>

## 📅 03-11-2026

### 🔹 Task 1: Transfer 3 Approved Indents to Store Section for PO Generation
- **Indent Ref**: `IN/SBMPINS/26-27/4138`, `IN/SBMPCBSE/26-27/4144`, `IN/HO/26-27/4131`
- **Page**: Database / Manual Update
- **Issue**: These were Emergency Indents mistakenly created as Normal Indents and were queued for RFQ.
- **Solution**: Manually transferred them to the Store section for PO generation by updating their section codes.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Fix Redirection Link in Accounts Section
- **Page**: `Erlier_Indent_Requests.aspx`
- **Issue**: In the Accounts section, when forwarding to the CAO section, the "Next Indent" button appeared immediately after submit and redirected incorrectly to the Purchase section.
- **Solution**: Corrected the `href` navigation link to point to the appropriate destination page.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 3: Fix "Conversion failed" Error on PO Entry in Store Section
- **Page**: `Pages/Sections/PurchaseOrderForAwardedRFQ.aspx.cs`
- **Issue**: Received a SQL conversion failure exception when clicking the "PO Entry" button in the Store section.
- **Solution**: Updated SQL query to safely parse `VendorPrice` as a decimal before evaluating `NULLIF`:
  ```sql
  ISNULL(NULLIF(TRY_CONVERT(decimal(18,2), d.VendorPrice), 0), ...)
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 4: Provide Item Description Field for Store In-Charge in PO
- **Page**: PO Generation / Store Section
- **Requirement**: Add a textbox allowing the Store In-charge to input a specific description for each item, which must display directly below the item row on the generated Purchase Order.
- **Solution**: Requirement under review; need to discuss implementation details and UI placement with senior developer.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 04-11-2026)*

---

<br/>

## 📅 02-11-2026

### 🔹 Task 1: GRN Buttons Disabled
- **Solution**: Updated button properties to be enabled by default.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

### 🔹 Task 2: Custom Search Filters on Admin Vendors Page
- **Solution**: Added multiple filter buttons for vendor search criteria.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

### 🔹 Task 3: Update Vendor User Manual and Eligibility Criteria PDFs
- **Solution**: Updated file paths and uploaded the latest PDF documents.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

### 🔹 Task 4: RFQ Dashboard UI Redesign
- **Solution**: Made the RFQ Dashboard UI responsive and user-interactive.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---
