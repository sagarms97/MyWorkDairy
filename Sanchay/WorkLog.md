# 📓 Project Work Log: Sanchay

---

## 📅 13-11-2026

### 🔹 Task 1: Hide Dedicated GRN Document Upload Section at Institute Level
- **Page**: Store / Goods Receipt Section (Institute Level)
- **Issue**: Due to client-side browser caching, some users experienced visual display overlap between GRN and Invoice previews. The institute opted to scan both the GRN sheet and Invoice together as a single combined PDF document.
- **Solution / Implementation**: Advised institute administrators on browser cache clearing, and conditionally hid the separate GRN document upload section from the interface so users submit the single combined document under Invoice upload without confusion.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Provide Alternate Specification / Remarks Textbox for Vendors During Bidding
- **Page**: Vendor Bidding Portal (`VendorBidSubmission.aspx`)
- **Issue**: During RFQ bidding, vendors occasionally do not stock the exact item specification requested and wish to propose an equivalent higher or lower variant/grade. Currently, there is no field to convey this deviation.
- **Solution / Next Steps**: Discuss with the product team and stakeholders regarding adding a "Vendor Proposed Specification / Remarks" field to the item bidding grid and defining whether deviation alerts should be highlighted during quotation comparisons.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 12-11-2026

### 🔹 Task 1: Remove Mobile Number Validation for Vendor Registration at Admin Level (Follow-up from 06-11)
- **Original Date**: `06-11-2026`
- **Page**: `AddVendors.aspx` (Admin Level)
- **Issue**: Certain vendors do not have or provide a mobile number during initial registration, but the form blocks submission.
- **Solution / Resolution**: Removed the mandatory required-field validation for the mobile number field on the admin's `AddVendors` page.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

### 🔹 Task 2: Enable Submission Date Extension for RFQ (Follow-up from 11-11)
- **Original Date**: `11-11-2026`
- **Requirement**: Provide authorized users the capability to extend active RFQ deadlines.
- **Solution / Resolution**: Added an "Update RFQ Date" action allowing authorized personnel to extend valid RFQ submission dates with system audit tracking.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

### 🔹 Task 3: GST Percentage Validation & Auto-Handling for Composite / Unregistered Vendors
- **Issue 1**: Input field fails to accept `0%` as a valid GST percentage value.
- **Issue 2**: Composite and Unregistered vendors are exempt from GST; only Regular registered vendors charge GST.
- **Solution / Next Steps**: Auto-detect vendor registration type upon selection. If Composite or Unregistered, lock and default the GST field to `0%`; enable user GST input only for Regular registered vendors.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 4: Dedicated Credential Provisioning Module for Legacy / Manually Registered Vendors
- **Page**: Custom Vendor Credential Management Page
- **Issue**: A blanket default password was unviable because multiple legacy vendors share duplicate contact details or generic emails.
- **Solution / Implementation**: Developed a dedicated admin interface filtering active vendors offering Goods, Services, or Goods & Services. Set the vendor's Mobile Number as their User ID, generated credentials combining Phone and Email, inserted credentials into the `Users` table upon admin confirmation, and automatically dispatched account setup notification emails.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 5: Automated Email Notification on Vendor Password Reset
- **Issue**: Vendors currently receive no confirmation receipt or email backup after updating their password on first login.
- **Solution / Implementation**: Configured an automated email trigger dispatched immediately upon successful password change, providing vendors with written confirmation and self-service password recovery instructions.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 6: Provide OTP Verification for Vendors Post-Login
- **Requirement**: Implement OTP-based multi-factor authentication for vendors upon successful credential verification.
- **Solution / Next Steps**: Map and list vendors under the admin-side `Users` management page to support two-factor authentication provisioning, telephone binding, and OTP delivery dispatch.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 11-11-2026

### 🔹 Task 1: Display Institute Name, Beneficiary Name, and Payable Amount in Accounts PO Approval
- **Page**: `Request_PurchaseOrderApproval.aspx` (Accounts Section)
- **Issue**: Essential payment context was missing from the approval interface, requiring staff to cross-check multiple views.
- **Solution**: Updated backend queries and mapped Institute Name, Beneficiary Name, and Payable Amount directly into the repeater list display.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Duplicate Amount Calculation & Status Column in TDS Calculation Page
- **Page**: `Tds_Calculation.aspx`
- **Issue**: The page aggregates amounts redundantly by including both submitted GRN amounts as well as reverted/resubmitted GRN amounts.
- **Sub-Task (2.1)**: Add a dedicated "Status" column displaying transaction states: *Pending*, *Closed*, *Failed*, *Hold*, or *Revert*.
- **Solution / Next Steps**: Investigate calculation logic and query filters in `Tds_Calculation.aspx.cs` and coordinate with colleague to align on business rules for handling reverted GRNs.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 3: Integrate Rich Text Editor (CKEditor) for Indent Purpose Textbox
- **Page**: Indent Creation / Indenter Module
- **Issue**: When indenters format their purpose with bullet points or line breaks in the standard multiline textbox, formatting is lost and collapsed into a single plain text paragraph upon saving/printing.
- **Solution / Next Steps**: Replace or bind the Purpose textbox with CKEditor rich text control to preserve formatting, bullet points, and numbered lists into HTML storage.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 4: Enable Submission Date Extension for RFQ
- **Requirement**: Provide authorized users the capability to extend active RFQ deadlines.
- **Solution / Next Steps**: Add an "Update RFQ Date" interface action allowing valid date extensions with appropriate audit logging.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 12-11-2026)*

---

### 🔹 Task 5: Prepare Comprehensive User Manual for Indenter Module
- **Requirement**: Document the end-to-end indent creation, specification, and forwarding workflow for new indenters.
- **Solution / Next Steps**: Capture step-by-step UI screenshots and compile them into a standardized PDF user guide.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 06-11-2026

### 🔹 Task 1: Account Number Validation in Vendor Master
- **Issue**: The vendor master form allowed duplicate account numbers to be submitted across different vendors.
- **Solution**: Added validation logic and mandatory checks on the Account Number field to prevent duplicate submissions.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Approved Vendors from Accounts Section Missing in Purchase Section
- **Issue**: Once a vendor was approved by the Accounts section, the record failed to appear in the Purchase section's queue.
- **Solution**: Diagnosed the issue in the Vendor Master table where the `IsApproved` column was defaulted to `NULL`. Updated the record status to `0` so pending approvals reliably appear in the Purchase section's pending list.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 3: Enable Mobile Number Login for Vendors Without Email Addresses
- **Issue**: Vendors currently require an email address as their login identifier; however, several vendors do not possess an active email address. Praveen sir requested an option to allow mobile number as the login ID.
- **Solution / Next Steps**: Create a dedicated configuration interface allowing administrators to toggle/select whether a vendor's primary login identifier should be their Mobile Number or Email Address, followed by appropriate database schema updates.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

### 🔹 Task 4: Add Search Functionality in Vendor Approval Process
- **Page**: `Pages/Sections/VendorRequestApproval.aspx`
- **Issue**: Administrators had to manually scroll through long paginated lists (137+ pages) to locate a specific vendor during approval.
- **Solution**: Implemented a multi-column search textbox and search/clear buttons allowing instant filtering across Vendor Name, Mobile No, GSTIN, PAN, and Vendor Code with automatic pagination reset.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 5: Item Specification Edit Option Without Affecting Master Data (Follow-up from 05-11)
- **Original Date**: `05-11-2026`
- **Issue**: Operators require custom item specifications on the indent without altering default specifications defined in the Item Master table.
- **Solution / Resolution**: Provided an inline edit option for item specifications scoped strictly to the indent transaction without modifying the master table.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

### 🔹 Task 6: GRN and Invoice Uploads Displaying Same Document (Follow-up from 05-11)
- **Original Date**: `05-11-2026`
- **Issue**: Users upload separate files for GRN and Invoice, but after submission, opening the GRN document erroneously displays the Invoice file.
- **Solution / Resolution**: Fixed the document upload and binding logic in `Store_GoodsDelivery.aspx` and verified database path mappings so both files link and display independently.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved today)*

---

### 🔹 Task 7: Remove Mobile Number Validation for Vendor Registration at Admin Level
- **Page**: `AddVendors.aspx` (Admin Level)
- **Issue**: Certain vendors do not have or provide a mobile number during initial registration, but the form blocks submission.
- **Solution**: Remove mandatory required-field validation for the mobile number field on the admin's `AddVendors` page.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 12-11-2026)*

---

<br/>

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
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 06-11-2026)*

---

### 🔹 Task 3: GRN and Invoice Uploads Displaying Same Document in Store Section
- **Page**: `Store_GoodsDelivery.aspx`
- **Issue**: Users upload separate files for GRN document and Invoice document, but after submission, opening the GRN document erroneously displays the uploaded Invoice document.
- **Solution**: Investigate file upload and binding logic in `Store_GoodsDelivery.aspx` and verify document storage paths/columns in the database table.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square) *(Resolved on 06-11-2026)*

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
