# Data Handling Approaches Compared: Central Layer vs. Compressed-Step

## 📊 Core Comparison

### Architecture Diagram Comparison

```
[Central-Layer Approach (the criticized pattern)]

Daloopa ─┐
         ├─→ Central Data Normalization Engine ─→ Standard Format ─┬→ Comps Analysis
FactSet ─┤   (complex transformation logic)    (original format    ├→ DCF Model
AKShare ─┤   (must handle all permutations)     is lost)           ├→ Portfolio
LSEG ────┘   (high maintenance cost)                               └→ Pitch Deck

Problems:
❌ Middle-layer rot: original information is lost after format conversion
❌ Complexity explosion: O(N×M) — N sources × M targets
❌ Single point of failure: a bug in the central layer affects the whole system
❌ Hard to maintain: adding a source or a target both require changing the central layer


[Compressed-Step Approach (the recommended pattern)]

Daloopa ┐
        ├─→ Comps Analysis ──→ (RULE 1 conversion)
FactSet ┤                      └→ used here
AKShare ┤   Datapack Builder ─→ (format detection + minimal conversion)
LSEG ───┴─→ DCF Model ────────→ (apply source documentation)
           Portfolio
           Pitch Deck

Benefits:
✅ Information preserved: source format always visible
✅ Linear complexity: O(N+M)
✅ No single point of failure: each consumer is independent
✅ Easy to maintain: adding a source only requires providing documentation
```

---

## 🔍 Detailed Comparison Table

### 1. Data Source Handling

| Dimension | Central-Layer Approach | Compressed-Step Approach |
|-----------|----------------------|------------------------|
| **Source format clarity** | ❌ Hidden inside the central layer | ✅ Explicit in source documentation |
| **Adding a new data source** | ⚠️ Must modify the central layer | ✅ Only need to provide source docs |
| **Source format changes** | ⚠️ Must modify the central layer | ✅ Only need to update source docs |
| **Traceability** | ❌ Difficult | ✅ Easy (source references) |
| **Debug time** | ⚠️ Must trace through the central layer | ✅ Look directly at the source docs |

**Example: Adding Bloomberg as a new data source**
```
Central-layer approach:
  Must add to the central layer: Bloomberg format handling
  Locations that need to change: 6+ consumer mapping tables
  Test effort: High

Compressed-step approach:
  Only need to provide: Bloomberg data format specification document
  Code changes: each consumer handles it independently based on the spec
  Test effort: Low
```

---

### 2. Format Conversion Process

| Dimension | Central-Layer Approach | Compressed-Step Approach |
|-----------|----------------------|------------------------|
| **Where conversion happens** | Centralized | Distributed at each consumer |
| **Source format preserved** | ❌ Lost | ✅ Retained |
| **Conversion rule complexity** | High (handles all combinations) | Low (each consumer is independent) |
| **Maintenance location** | One large file | Multiple small files + source docs |
| **Scope of a change** | Entire system | Only that consumer |

**Example: Date format handling**
```
Central-layer approach:
  Received from source: 2024-01-31, 20240131, 01/31/2024, ...
  Central layer normalizes to: 2024-01-31 (ISO 8601)
  At point of use: all consumers use this format
  Problem: if a new source format is added → central layer changes → entire system re-tested

Compressed-step approach:
  Daloopa spec: returns 2024-01-31 (ISO 8601)
  AKShare spec: returns 20240131 (YYYYMMDD)
  Comps consumer:
    if source == 'Daloopa': use as-is
    elif source == 'AKShare': convert to YYYY-MM-DD
  Adding a new source: only add the conversion logic at that consumer; other consumers are unaffected
```

---

### 3. Traceability and Debugging

| Scenario | Central Layer | Compressed-Step |
|----------|--------------|----------------|
| **Seeing a value and wanting to know its origin** | ⚠️ "Need to trace the central layer's conversion log" | ✅ "Look directly at the source reference and color coding" |
| **Data is wrong, need to find the bug** | ⚠️ "Might be in some conversion inside the central layer" | ✅ "Look directly at the consumer's conversion rule and source doc" |
| **Need to verify data accuracy** | ⚠️ "Need to understand the central layer logic" | ✅ "Compare against the source doc and raw value" |
| **Need to recalculate a metric** | ⚠️ "Need to undo the central layer conversion first" | ✅ "Go straight back to the raw value and calculate" |
| **Need to explain data to a user** | ⚠️ "Need to explain multiple conversion steps" | ✅ "Simply state the source and the consumer's rule" |

**Debug example: Revenue value anomaly**
```
Central-layer approach:
  User: Why is Revenue $1B in the DCF but $0.001B in the Comps?
  Engineer: Let me check... what format did the central layer receive...
            AKShare is in millions, Daloopa is in thousands...
            Did the central layer convert incorrectly somewhere?
            (Debug time: 30+ minutes)

Compressed-step approach:
  User: Why is Revenue $1B in the DCF but $0.001B in the Comps?
  Engineer: Check the source reference in Comps... ah, this one uses AKShare.
            AKShare spec: returns millions (not in $ format)
            Comps conversion rule: should multiply by 1M
            Let me check... it didn't multiply! Fixed.
            (Debug time: 3 minutes)
```

---

### 4. Code Complexity

| Dimension | Central-Layer Approach | Compressed-Step Approach |
|-----------|----------------------|------------------------|
| **Central layer lines of code** | 500–1,000 lines | 0 lines (no central layer) |
| **Conversion rule management** | Central configuration table | Source docs + consumer |
| **Test coverage** | Must cover all source × target combinations | Each consumer tested independently |
| **Locations to change when adding a source** | 6+ places | 1–2 places |

**Estimated line counts:**
```
Central layer (500+ lines):
  def convert_ticker(ticker, from_source, to_source): ...
  def convert_date(date_str, from_format, to_format): ...
  def map_field_name(field, from_source): ...
  def normalize_currency(value, currency): ...
  def handle_missing_values(value, source): ...
  ... plus mapping tables ...

Compressed-step (10–30 lines per consumer):
  # Comps consumer
  for ticker in tickers:
      if source == 'AKShare':
          ticker = convert_astock_to_symbol(ticker)
      
  # DCF consumer
  if source == 'AKShare':
      dates = [d.to_date() for d in dates]
  
  # Each location is simple because the source doc is explicit
```

---

### 5. Usability

| Aspect | Central Layer | Compressed-Step |
|--------|--------------|----------------|
| **New-hire learning curve** | Steep (must understand the central layer) | Gentle (just read the source docs) |
| **Code readability** | Low (complex mapping relationships) | High (direct logic) |
| **Difficulty of changes** | High (large blast radius) | Low (hard to break things) |
| **Where documentation lives** | "Where should this be written?" | Right next to the source + at the consumer |

---

### 6. Actual Maintenance Cost Comparison

```
[Scenario: migrating 30% of traffic from Daloopa to AKShare]

Central-layer approach work:
1. Modify central layer's date format handling (Daloopa: YYYY-MM-DD → AKShare: YYYYMMDD)
2. Modify central layer's currency unit handling (may differ)
3. Modify central layer's missing-value handling (may differ)
4. Modify source-detection logic at 6+ consumer locations
5. Test all possible source combinations (now 2×N instead of N)
6. Update documentation
Effort: 5–10 days
Risk: High (large scope of change)
Rollback difficulty: Hard (involves many places)


Compressed-step approach work:
1. Add at each consumer:
   if source == 'AKShare':
       dates = convert_dates(dates, 'YYYYMMDD', 'YYYY-MM-DD')
2. Test each consumer independently (no need to test all source combinations)
3. Update source docs and consumer comments
Effort: 2–3 days
Risk: Low (narrow scope of change)
Rollback difficulty: Easy (roll back one consumer at a time)
```

---

## 🎯 Actual Implementation in This Project

### How the Current Project (Datapack Builder) Does It

```markdown
[Phase 1: Raw Extraction] ✅ Compressed-step in practice
Steps 1.1–1.5:
  ├─ Extract directly from source (preserving format information)
  ├─ Record page references (Daloopa p.47, FactSet p.3)
  └─ No early-stage conversion

[Phase 2: Minimal Normalization] ✅ Compressed-step in practice
Step 2.1: Within-source normalization
  └─ Only ensures consistency within a single source; no cross-source conversion

Step 2.2: Context-based conversion
  ├─ Read: tab name, table title, column header, row label
  └─ Principle: when uncertain, consult the original source document
               (not a central layer conversion table)

Steps 2.3–2.4: Create adjustment schedule
  ├─ Document: raw data → what was adjusted → final data
  ├─ Full traceability
  └─ Source reference is explicit: [Company] [Document] ([Date])

[Phase 3: Final Formatting] ✅ Compressed-step in practice
Step 3.2: Apply display formatting
  ├─ RULE 1: Financial data → $ format (based on data meaning)
  ├─ RULE 2: Operational data → numeric format (no $)
  ├─ Trigger words are "source-level cues" (Revenue, Employees, etc.)
  └─ This is the last step; it does not change the data itself

[Traceability] ✅ Compressed-step in practice
Color coding:
  ├─ Blue: raw input data (user input or directly from source)
  ├─ Black: converted data (formula-derived)
  └─ Green: cross-sheet references
```

---

## 💡 The Elegance of This Approach

```
The concern raised:
"Avoid having a complex layer that normalizes all data source data;
 also, when data processing is done, the original data description
 is often lost, so at the point of use you no longer know the format."

This precisely identifies two problems:
1️⃣  "Complex intermediate layer" → violates the KISS principle
2️⃣  "Loss of original data description" → violates the traceability principle

This is exactly why the project uses the "compressed-step" approach:
✅ Avoids an intermediate layer
✅ Preserves original descriptions (source references + adjustment schedule)
✅ Each consumer handles its own conversion (based on source docs)
✅ Complete data lineage (source → adjustment → use)
```

---

## 📋 Summary Comparison Table

| Feature | Central-Layer Approach | Compressed-Step Approach |
|---------|----------------------|------------------------|
| **Information preservation** | ❌ Poor | ✅ Excellent |
| **Code complexity** | ❌ High | ✅ Low |
| **Maintainability** | ❌ Poor | ✅ Excellent |
| **Traceability** | ⚠️ Moderate | ✅ Excellent |
| **Learning cost** | ❌ High | ✅ Low |
| **Scope of a change** | ❌ Large | ✅ Small |
| **Debug time** | ❌ Long | ✅ Short |
| **Cost of adding a new source** | ⚠️ Medium | ✅ Low |

---

## 🎓 Supporting Engineering Principles

| Principle | Central Layer | Compressed-Step |
|-----------|--------------|----------------|
| KISS (Keep It Simple, Stupid) | ❌ Violated | ✅ Followed |
| DRY (Don't Repeat Yourself) | ✅ Followed | ✅ Followed |
| YAGNI (You Aren't Gonna Need It) | ❌ Over-engineered | ✅ Just enough |
| SRP (Single Responsibility) | ⚠️ Intermediate layer has blurry responsibilities | ✅ Clear |
| Traceability | ❌ Poor | ✅ Excellent |

---

## Conclusion

**The compressed-step approach is 100% correct.**

The project is putting this principle into practice with Datapack Builder. This is not a new idea; it is a widely proven best practice:

```
✅ Source explicitly specifies the format
✅ Minimal conversion at the point of use
✅ Full traceability preserved
✅ No single-point-of-failure intermediate layer
```

This is the power of the compressed-step approach.
