# Datapack Builder Compressed-Step Practices: Quick Reference

## 📌 One-Page Summary

### ✅ What's Done Well (Keep These)

| Phase | Practice | Why It's Good |
|-------|----------|--------------|
| **Phase 1** | Extract directly from source, record page references | Preserves source information; avoids premature conversion |
| **Phase 2.1** | Within-source normalization only (no cross-source conversion) | Avoids a complex central layer |
| **Phase 2.2** | Determine format from context; consult source doc when uncertain | Source document is the specification |
| **Phase 2.4** | Create adjustment schedule: raw → adjustment → final | Full traceability of the conversion process |
| **Color coding** | Blue = raw, Black = converted, Green = reference | Data nature is clear at a glance |
| **RULE 1–6** | Concise format rules based on data meaning | Easy to maintain; easy to extend for new sources |

---

## ⚠️ Areas for Improvement (Prioritized)

### Priority ⭐⭐⭐⭐⭐ (This Week)

#### Improvement 1: Create MCP Source Data Format Specifications

**Current problem:** No explicit MCP source format documentation; consumers must guess.

**Proposed solution:**
```markdown
# Create the following documents (one per source)

📄 Daloopa Data Format Specification.md
├─ Return format for each interface
├─ Numeric precision (float? int?)
├─ Date format
├─ Missing-value handling (null? NaN?)
└─ Which Rule to apply in Datapack

📄 FactSet Data Format Specification.md
📄 AKShare Data Format Specification.md
📄 LSEG Data Format Specification.md
```

**Template (Daloopa example):**
```markdown
# Daloopa API Data Format Specification

## Interface: get_financials()

### Return format
- Data format: JSON
- Numbers: Float, 2 decimal places
  - Example: 1234567.89 (no $ symbol)
  - Precision: 2 decimal places
- Dates: String, YYYY-MM-DD
  - Example: "2023-12-31"
- Missing values: null (not NaN, not "", but null)
- Currency: USD uniformly; no symbol in the response

### Application in Datapack Builder
- Received: revenue = 1234567.89 (from JSON)
- Apply: RULE 1 (financial data → $ format)
- Convert: millions-scale → $1,234.6M
- Record: [Daloopa] [get_financials] [AAPL]

### Common questions
Q: Why is the returned value missing a decimal point?
A: The unit is USD; the integer represents whole dollars. Divide by 1,000,000 to get millions.
```

---

### Priority ⭐⭐⭐⭐ (This Month)

#### Improvement 2: Refine Format Detection Guidance for Step 2.2

**Current problem:** "Apply format detection logic" is too vague; newcomers don't know how to decide.

**Proposed solution:**
```markdown
# Step 2.2 Format Detection Decision Tree (Detailed)

## Quick Decision Flow

```
See a data point (e.g., "50")
    ↓
Q1: Which table is this data in?
├─ Executive Summary?  Balance Sheet?  Historical Financials?
│
Q2: What is the column header?
├─ "2023A" → year column
├─ "Revenue" → financial metric
├─ "Stores" → operational metric
│
Q3: What is the row label?
├─ "Revenue", "EBITDA", "Cash" → financial data
├─ "Stores", "Employees", "Units" → operational data
├─ "Growth Rate", "Margin" → percentage
│
Decision → Apply rule
```

## Concrete Examples

| Data | Table Name | Row Label | Column Header | Judgment | Rule Applied | Final Format |
|------|-----------|-----------|---------------|----------|-------------|-------------|
| 50 | Historical Fin. | Revenue | 2023A | Financial data | RULE 1 | $50.0M |
| 50 | Operating Metrics | Stores | 2023A | Operational data | RULE 2 | 50 |
| 50 | Historical Fin. | EBITDA Margin | 2023A | Percentage | RULE 3 | 50.0% |
| 2023 | Historical Fin. | Year | Column header | Year | RULE 4 | 2023 |
```

---

#### Improvement 3: Establish a Standard Adjustment Schedule Template

**Current problem:** Adjustments must be documented, but there is no standard format.

**Proposed solution:**
```markdown
# Standard Adjustment Schedule Format

## Standard Template

| Adjustment Item | 2022A | 2023A | Reason | Source | Recurrence Risk | Notes |
|----------------|-------|-------|--------|--------|----------------|-------|
| Reported EBITDA | $100.0M | $120.0M | | S-1 p.47 | - | |
| | | | | | | |
| Adj: Restructuring | $5.0M | $2.0M | Non-recurring | CIM p.15 | Low | Plant closure |
| Adj: SBC | $3.0M | $3.5M | Industry standard | Proxy p.22 | Medium | Annual grants |
| Adj: M&A costs | - | $1.0M | One-time | CIM p.20 | Low | Earn-out completed |
| | | | | | | |
| Adjusted EBITDA | $108.0M | $126.5M | | | | |

## Documentation Rules
1. Reported data → raw value from the source
2. Each adjustment → separate row
3. Source → explicit page number or document name
4. Recurrence risk → Low/Medium/High (assess whether it will repeat in future)
5. Adjusted total → auto-sum formula (=SUM(...))
```

---

#### Improvement 4: Build an MCP Source Format Matrix

**Current problem:** No quick-reference table; understanding each source's format requires consulting multiple documents.

**Proposed solution:**
```markdown
# MCP Source Format Quick-Reference Matrix

| Feature | Daloopa | FactSet | AKShare | LSEG | S&P Global |
|---------|---------|---------|---------|------|-----------|
| **Numeric precision** | Float, 2 dec. | Float, 4 dec. | Float, 4 dec. | Int/Float | Float, 2 dec. |
| **Date format** | YYYY-MM-DD | YYYY-MM-DD | YYYYMMDD | YYYY-MM-DD | YYYY-MM-DD |
| **Missing values** | null | null | NaN | null | "" |
| **Currency symbol** | None | None | None | Sometimes | None |
| **Field naming** | snake_case | snake_case | Chinese | camelCase | snake_case |
| **Return format** | JSON | JSON | DataFrame | JSON | JSON |
| **Units** | Millions USD | Millions USD | Units CNY | Mixed | Millions USD |
| **Datapack rule** | RULE 1 | RULE 1 | RULE 1 + convert | Special | RULE 1 |

## Usage Guide
1. Choose the MCP source you are using
2. Consult this table to understand its format
3. Apply the appropriate conversion at the consumer
4. Record the conversion process in the adjustment schedule
```

---

### Priority ⭐⭐⭐ (Later)

#### Improvement 5: Cross-Source Data Merge Standards

**Proposed solution:**
```markdown
# When Merging Data from Multiple MCP Sources

## Principles
1. **Designate a primary source**
   - If using Daloopa Revenue, stick with it
   - Other sources serve as validation, not as the primary data source

2. **Document the conversion process**
   - Source A: 1000 (in thousands)
   - Conversion: 1000 / 1 = 1000 (still thousands)
   - Source B: 1 (in millions)
   - Converted comparison: 1,000 thousands = 1 million ✓ consistent

3. **Retain source references**
   - [Daloopa] [get_financials]
   - [AKShare] [stock_financial_analysis_indicator]

## Conflict Resolution
If two sources disagree:
```
1. Are the units the same? (e.g., both in millions?)
2. Is the period the same? (both FY2023?)
3. If both are identical but data differs, record the discrepancy
4. Note in Datapack footnotes which source was used
```

---

#### Improvement 6: New MCP Source Checklist

**Proposed solution:**
```markdown
# Checklist for Adding a New MCP Data Source

## When adding a new MCP source

### [ ] Step 1: Collect source information
- [ ] Source name and primary function
- [ ] List of supported interfaces
- [ ] Return data format (JSON/CSV/DataFrame)
- [ ] Obtain sample data and analyze its format

### [ ] Step 2: Normalize format specification
- [ ] Number type and precision
- [ ] Date format
- [ ] Missing-value handling
- [ ] Currency handling
- [ ] Field naming convention

### [ ] Step 3: Map to Datapack Rules
- [ ] Which RULEs (1–6) should be applied
- [ ] Whether unit conversion is needed (thousands → millions)
- [ ] Whether currency conversion is needed (CNY → USD)

### [ ] Step 4: Write usage documentation
- [ ] Create "[Source Name] Data Format Specification.md"
- [ ] Provide at least 3 usage examples
- [ ] Document common questions and solutions

### [ ] Step 5: Update quick-reference materials
- [ ] Add this source to the "MCP Source Format Matrix"
- [ ] Update "Cross-Source Merge Standards" (if applicable)

### [ ] Step 6: Test
- [ ] Successfully use this source in Datapack Builder
- [ ] Successfully use it in multi-source merge scenarios
- [ ] All adjustment schedules correctly record conversions
```

---

## 🚀 Immediate Actions

### Today (5 minutes)
```
1. Review Datapack Builder's current practices
2. Confirm the "6 things done well" are all present
3. List the 6 areas to improve
```

### This Week (1–2 hours)
```
1. Create format specification documents for Daloopa, FactSet, AKShare, and LSEG
2. Reference these specifications in the Datapack Builder documentation
   └─ Update Step 1.1 to read:
      "Refer to the corresponding MCP Source Data Format Specification document"
```

### This Month (4–8 hours)
```
1. Refine the Step 2.2 decision tree (with real examples)
2. Create the standard adjustment schedule template
3. Build the MCP Source Format Matrix
4. (Optional) Create the new-source checklist
```

---

## 📊 Before vs. After Improvement

### Before

```
Datapack Builder documentation
│
├─ Phase 1: Extraction ✅
├─ Phase 2: Normalization (but Step 2.2 is vague)
├─ Phase 3: Build Excel
├─ Color coding ✅
├─ RULE 1–6 ✅
└─ Missing: source format specification docs ❌
            cross-source merge standards ❌
            templates ❌
            quick reference ❌
```

### After

```
Datapack Builder documentation
│
├─ Phase 1: Extraction ✅
│  └─ Reference: MCP Source Data Format Specification documents
│
├─ Phase 2: Normalization ✅
│  ├─ Step 2.2: Decision tree (detailed)
│  └─ Step 2.4: Adjustment schedule (standard template)
│
├─ Phase 3: Build Excel ✅
├─ Color coding ✅
├─ RULE 1–6 ✅
│
├─ New documents:
│  ├─ Daloopa Data Format Specification ✅
│  ├─ FactSet Data Format Specification ✅
│  ├─ AKShare Data Format Specification ✅
│  ├─ LSEG Data Format Specification ✅
│  ├─ MCP Source Format Matrix ✅
│  ├─ Cross-Source Merge Standards ✅
│  ├─ Adjustment Schedule Template ✅
│  └─ New-Source Checklist ✅
```

---

## 💡 Why These Improvements Matter

### Current State
```
Datapack Builder is already good (80%), but:
├─ New hires must figure out MCP source formats on their own
├─ Consumers must judge for themselves whether the right rule is applied
├─ No quick-reference tool
└─ No clear process for extending to new sources
```

### State After Improvement
```
✅ New hires → consult the docs; up to speed in 5 minutes
✅ Consumers → follow the decision tree; no mistakes
✅ Quick reference → matrix table gives the answer at a glance
✅ New source → follow the checklist; complete and consistent
✅ Maintenance → when a source format changes, only one document needs updating
```

---

## 📝 Completeness Check

- [ ] Are all 6 things done well still preserved?
- [ ] Are all 6 improvement areas listed?
- [ ] Is the priority ordering reasonable?
- [ ] Does each improvement have a concrete implementation plan?
- [ ] Are the time estimates realistic?

✅ Ready to start improving?
