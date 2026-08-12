# ecom-responsive-qa

Purpose: verify layout integrity across required viewport widths.

## Viewports
700, 820, 960, 1200, 1500, 1648 px.

## Checks
- no clipped labels or controls
- no horizontal overflow unless contract explicitly allows it
- cards reflow without losing hierarchy
- controls remain reachable and readable
- sticky/header/sidebar behavior remains coherent
- RU/DE/EN/RO strings do not break layout
- currency/shop/role controls remain independent and visible
- empty states stay compact

Return PASS matrix per viewport plus defects with exact component ownership.
