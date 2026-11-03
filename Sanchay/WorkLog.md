# 📓 Project Work Log: Sanchay

---

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
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

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
