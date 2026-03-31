# Solar System Recommendations

Based on analysis of solar data from 2025-12 to 2026-03 (120 days).

## Executive Summary

Your 6.5 kWp system is performing well and the main story is seasonal improvement: self-sufficiency rose from 54.3% in December 2025 to 76.5% in March 2026 as solar production climbed from ~16.5 to ~27.2 kWh/day. Across the four months, the system cut estimated grid spend by about 69% and is tracking toward a simple payback of ~4.0 years on a reported ₱400,000 investment.

The single highest-impact optimization is PHEV charging timing. On detected EV/PHEV days, average daily load jumps to ~42.5 kWh and grid import jumps to ~20.2 kWh, versus ~23.8 kWh load and ~6.3 kWh import on non-EV days. Your battery is doing useful work, but the vehicle load is still large enough to force heavy afternoon grid draw when charging extends beyond the solar peak.

No inverter-capacity issue is visible. Peak PV output reached 5.4 kW, which is only 68% of your 8 kW inverter rating, so the system is not clipping. Action worth taking now: review 2026-01-02 in the inverter logs because generation was ~74% below its rolling baseline.

The system is projected to avoid about 4.4 tonnes of CO2 per year, roughly equivalent to 200 trees or 20,967.0 km of driving emissions.

## System Profile

- **Location**: Cavite, Philippines
- **PV capacity**: 6.5 kWp, inverter: 8.0 kW AC (DC/AC ratio: 0.81)
- **Battery**: 14.3 kWh nominal, ~14.4 kWh estimated usable in the data; treat that as effectively full nominal capacity rather than true >100% usable because the estimate is sensitive to SOC reporting
- **EV/PHEV**: PHEV present; 30 EV-like charging days detected in 120 full days
- **Tariff**: Flat rate at ₱14/kWh
- **Feed-in tariff**: 50% of import rate

## Alerts

### PV Generation Alerts

**Action required:** On 2026-01-02, PV generation was 4.7 kWh against an expected ~17.8 kWh (74% below baseline). If this does not match known bad weather or downtime, check inverter logs for that date.
| Date | Daily PV (kWh) | Expected (kWh) | Deviation |
|---|---|---|---|
| 2025-12-07 | 9.9 | ~17.5 | -43% |
| 2025-12-08 | 9.6 | ~16.4 | -41% |
| 2025-12-09 | 8.6 | ~15.5 | -45% |
| 2026-02-08 | 10.9 | ~19.4 | -44% |
| 2026-03-17 | 15.8 | ~28.3 | -44% |
These dips are large enough to review against weather and inverter logs, but most look more like weather-driven weak-solar days than a persistent hardware issue.

### Load Alerts

- 2025-12-04: 35.6 kWh consumed versus a non-EV baseline of ~23.8 ± 5.4 kWh. If that day was not a missed PHEV classification, it likely reflects an unusual household load spike worth checking if it recurs.
- 2026-03-13: 36.1 kWh consumed versus a non-EV baseline of ~23.8 ± 5.4 kWh. If that day was not a missed PHEV classification, it likely reflects an unusual household load spike worth checking if it recurs.
- 2025-12-03: 35.0 kWh consumed versus a non-EV baseline of ~23.8 ± 5.4 kWh. If that day was not a missed PHEV classification, it likely reflects an unusual household load spike worth checking if it recurs.
- 2026-01-07: 36.0 kWh consumed versus a non-EV baseline of ~23.8 ± 5.4 kWh. If that day was not a missed PHEV classification, it likely reflects an unusual household load spike worth checking if it recurs.

### Battery Alerts

- 2026-03-17: round-trip efficiency was 78.7% on 8.6 kWh charged and 6.8 kWh discharged. Treat this as a monitor-for-recurrence item rather than a fault on its own unless it repeats.

## Recommendations

### 1. Shift PHEV charging into the late-morning solar window

What is happening now: your solar output is strongest from 09:00 to 14:00, with the average peak around 12:00. On EV/PHEV days, the charging signature extends from 09:00 through 20:00, and the heaviest average EV-day load appears at 15:00 when household demand reaches ~4.3 kW. That timing forces the battery to discharge hard and still leaves the grid supplying about 0.8 kWh in that hour on average. The single highest grid-draw hour in the whole dataset was 8.7 kW on 2025-12-02 at 16:00, and it was an EV day.

Why it is suboptimal: the house-only baseline is already fairly well matched to the PV system. The data gap shows up when vehicle charging continues after the PV peak begins to fade. Non-EV days average ~6.3 kWh of import, while EV days average ~20.2 kWh. That means the car is the dominant driver of grid dependence, not a general undersizing problem in the house system.

What to change: if your PHEV or charger has scheduling, concentrate charging into roughly 10:00 to 15:00 on sunny days and avoid starting a large session after 15:00 unless you specifically need the range. Even partial improvement matters. The battery analysis suggests about ~1.9 kWh/day of avoidable import across the dataset as an upper-bound flexible-load opportunity, worth roughly ₱9,709 per year. Because much of that flexibility is likely tied to the vehicle, the real value of a better charging schedule could be a meaningful chunk of that figure while also reducing high afternoon peak draw.

### 2. Preserve battery energy for the evening instead of letting flexible daytime loads spill into late afternoon

What is happening now: on non-EV days, evening SOC averages about 63% and falls to about 23% by 05:00 to 06:00, so the battery is carrying a healthy overnight role. On EV days, evening SOC is only about 27%, which means the battery has already been pulled down heavily before the night period starts.

Why it matters: once the battery reaches the evening at a low SOC, the night and early-morning load has no buffer left and the home falls back to grid import. This is why EV days look much worse than non-EV days even though EV-day solar production is actually a bit higher (~22.2 versus ~20.4 kWh/day).

What to change: if you can choose when flexible loads run, keep the noon export window for the PHEV first, then avoid stacking other large discretionary loads into 15:00 to 20:00. Laundry, water heating, and similar timer-friendly loads are better earlier in the solar window. The goal is not just to consume solar, but to arrive at sunset with more battery remaining.

### 3. Do not spend money on more inverter or another battery before you optimize charging behavior

What the data says: there is no inverter bottleneck. Peak PV only reached 84% of panel nameplate and 68% of inverter capacity, with zero clipping hours detected. The battery is also not obviously too small for the house-only baseline: non-EV days average ~58% cycle depth and the system reaches ~73% to 76% self-sufficiency in February and March.

Why this matters: hardware upgrades should solve an actual constraint. Right now the data points to timing mismatch from PHEV charging, not inverter saturation. A second battery would also be a weak first move because projected annual export is only ~767 kWh, or about ~2.1 kWh/day on average. There is not a huge pool of unused midday surplus waiting to be captured.

How to act on it: keep the present hardware, improve charging schedule first, then reassess after another few months. If you later see persistent midday export rising well above current levels, that would be the right moment to revisit storage expansion.

### Not Recommended

- **Replacing the inverter for more headroom**: current data shows no clipping, so a larger inverter would not unlock meaningful extra generation.
- **Adding a second battery right now**: export volumes are modest and the present battery is already close to covering the house-only overnight profile; the bigger problem is when the PHEV load arrives relative to solar production.

## Bill Impact

### Monthly Electricity Cost Comparison

| Month | Without Solar | With Solar | Feed-in Credit | Net Savings |
|---|---|---|---|---|
| 2025-12 | ₱13,042 | ₱5,959 | ₱0 | ₱7,084 |
| 2026-01 | ₱11,628 | ₱4,654 | ₱76 | ₱7,051 |
| 2026-02 | ₱10,763 | ₱2,912 | ₱624 | ₱8,474 |
| 2026-03 | ₱12,341 | ₱2,899 | ₱874 | ₱10,317 |

- Estimated annual bill without solar: ₱145,313
- Estimated annual bill with solar: ₱49,956
- Estimated annual feed-in credit: ₱4,788
- **Estimated annual bill reduction: ₱100,150 (69%)**

## ROI Estimate

| Metric | Value |
|---|---|
| System cost | ₱400,000 |
| Estimated annual savings (year 1) | ₱100,150 |
| **Simple payback** | **4.0 years** |
| Remaining payback | 3.7 years |
| 25-year lifetime savings | ₱2,359,129 |

Your reported cost already includes the battery and may include financing effects if applicable. At the current savings rate, the project is on track for a payback of about four years, which is strong relative to typical panel life. Even with degradation applied, the long-run economics remain favorable.

## Key Metrics

| Metric | Non-EV Days | EV Days |
|---|---|---|
| Daily PV generation | ~20.4 kWh | ~22.2 kWh |
| Daily consumption | ~23.8 kWh | ~42.5 kWh |
| Daily grid import | ~6.3 kWh | ~20.2 kWh |
| Daily grid export | ~2.2 kWh | ~1.0 kWh |
| Evening SOC | ~60% | ~25% |

- Overall self-consumption rate across the four months was 89.4%.
- Monthly self-sufficiency improved from 54.3% in December to 76.5% in March as solar production increased and grid dependence fell.
- Export is concentrated in the 12:00 to 15:00 window, typically after the battery has already climbed well above midday SOC levels.
- On non-EV days, the battery usually carries the home from about ~63% evening SOC down to ~23% by dawn, which is a healthy overnight role.
- On EV days, the battery reaches evening with much less stored energy, so the car effectively displaces the battery’s usual overnight support.

### Hourly Patterns

- PV is strongest from 09:00 to 14:00, with the average peak at 12:00 on both EV and non-EV days.
- Non-EV demand peaks around 15:00 at about ~1.4 kW, which is manageable within the solar-plus-battery profile.
- EV-day demand also peaks around 15:00, but at about ~4.3 kW, turning the afternoon into the main stress period.
- Export hours are mostly 12:00 to 15:00, which is the clearest opportunity window for scheduled charging or timed appliances.
- EV charging signatures appear from 09:00 through 20:00, so not all vehicle demand is currently being captured inside the best solar window.
- Overnight import still exists even on non-EV days, but it is moderate compared with EV days and consistent with a battery that is helping rather than sitting idle.

### Weekday vs Weekend

Weekday and weekend non-EV performance is similar overall: average daily load is ~23.8 kWh on weekdays and ~23.7 kWh on weekends, while self-sufficiency is 73% versus 76%. The main behavioral difference is timing rather than volume: weekends show more load around 11:00 to 12:00 and again around 20:00, which actually helps solar alignment at midday but slightly lifts evening demand.

### Peak Demand

- Peak grid draw: 8.7 kW on 2025-12-02 at 16:00 (EV day)
- Average daily peak grid draw: ~1.4 kW on non-EV days, ~5.8 kW on EV days
- Peak PV output: 5.4 kW on 2026-03-15 at 12:00 (68% of inverter capacity)

## System Size Assessment

Your array looks well-sized for the home’s non-EV baseline, but the PHEV creates demand spikes that are too large and too late in the day to be fully covered by the existing solar window.

### PV Array (6.5 kWp): correctly sized for the house, not for uncontrolled vehicle charging

- Peak output reached 5436 W, or 84% of panel nameplate and 68% of inverter capacity.
- No panel clipping or inverter clipping was detected.
- Peak sun hours improved from 2.5 in December to 4.2 in March.
- The non-EV PV/load ratio is 0.86, which means the array is close to matching the home’s base energy needs but not oversized enough to absorb frequent vehicle charging without timing help.

### Battery (14.3 kWh): adequate for the home, stretched on EV days

- Average charge is ~9.2 kWh/day and average discharge is ~8.8 kWh/day.
- Average cycle depth is ~61% overall, ~58% on non-EV days, and ~71% on EV days.
- Estimated avoidable import is ~1.9 kWh/day as a dataset-wide upper bound, which supports load-shifting recommendations more than hardware expansion.
- Monthly round-trip efficiency stayed in the 94.5% to 98.3% range, which is healthy.

### Verdict

The system is fundamentally sound. The panels are not being limited by the inverter, the battery is active and useful, and the economics are already strong. The biggest remaining optimization is behavioral: capture more PHEV charging inside the midday solar window and avoid draining the battery before evening.

## Battery Health

- Nominal capacity: 14.3 kWh
- Estimated usable capacity from the data: ~14.4 kWh (101% of nominal)
- Round-trip efficiency: 94.5% to 98.3% across the four months
- Daily equivalent full cycles: ~0.61
- Estimated annual cycles: ~223
- Estimated remaining cycle life at current usage: ~27 years

The only caution here is interpretation: the computed usable-capacity estimate slightly exceeds nominal capacity, which usually means the metering and SOC-derived estimate is a little optimistic rather than the battery physically exceeding nameplate. In practical terms, the battery appears healthy and close to full rated performance.

## Month-over-Month Trends

| Period | Avg Daily PV (from) | Avg Daily PV (to) | Avg Daily Load (from) | Avg Daily Load (to) | Self-Sufficiency (from) | Self-Sufficiency (to) |
|---|---|---|---|---|---|---|
| 2025-12→2026-01 | 16.5 | 16.7 | 30.1 | 26.8 | 54.3% | 60.0% |
| 2026-01→2026-02 | 16.7 | 23.6 | 26.8 | 27.5 | 60.0% | 72.9% |
| 2026-02→2026-03 | 23.6 | 27.2 | 27.5 | 29.4 | 72.9% | 76.5% |

The clearest shift is seasonal, not degradational. PV production was nearly flat from December to January, then jumped 41% from January to February and another 15% into March. Load stayed in the same general band, so self-sufficiency improved sharply as the drier/brighter months arrived. Battery efficiency drifted down slightly month to month but remained comfortably healthy.

## Annual Projection

- Data coverage: 4 months (moderate confidence)
- Projected annual generation: ~7242 kWh in year 1, ~6888 kWh in year 10, ~6389 kWh in year 25
- Projected annual self-consumed energy: ~6475 kWh
- Projected annual grid export: ~767 kWh
- Environmental impact: ~4.4 tonnes CO2 avoided annually at 0.68 kg CO2/kWh

Because the dataset spans four months, this projection has moderate confidence. It is good enough for planning, but it will become more robust once you have a full wet/dry-season cycle in the data.

## Methodology Notes

- This report uses the repository’s deterministic `analyze.py` script for all calculations and then interprets the results in narrative form.
- EV/PHEV days are detected from unusually high daily load, so some atypical household-load days may be classified as EV-like if they resemble a charging event.
- Avoidable import is an upper-bound indicator of flexible-load opportunity, not a guarantee that every kWh can be shifted perfectly.
- Financial results assume a flat ₱14/kWh import tariff and feed-in credit at 50% of that rate.
- Annual projection confidence is moderate because only four months of data are available.

## Appendix

### Best and Worst Days

**Best day: 2026-03-19** — PV: 30.0 kWh, Load: 25.5 kWh, Import: 1.4 kWh, Export: 6.4 kWh, Peak SOC: 100%, Non-EV day, Self-sufficiency: 95%.

This day combined strong solar production with moderate household demand, allowing the battery to fill and still leave a useful export surplus.

**Worst day: 2026-01-02** — PV: 4.7 kWh, Load: 15.6 kWh, Import: 12.5 kWh, Export: 0.0 kWh, Peak SOC: 30%, Non-EV day, Self-sufficiency: 20%.

This was an extremely weak-solar day, so the system had very little generation to work with and grid dependence rose accordingly.

### Data Sources

- `data/solar_hourly_2025-12.csv`
- `data/solar_hourly_2026-01.csv`
- `data/solar_hourly_2026-02.csv`
- `data/solar_hourly_2026-03.csv`

### Disclaimer

This report was generated with an AI assistant using deterministic calculations from `skills/analyze/scripts/analyze.py`. The computed metrics are script-based, but the narrative interpretation and recommendations are still model-generated and should be sanity-checked against your own inverter records, utility bills, and operating experience before making spending decisions.
