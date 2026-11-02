# Data Guide

Welcome to the data!

Under `data` you'll find all of the raw files. I'm including everything that we recorded this summer, even the failed/weird things and bad ideas. The more standardized field study is entry 7 in the list below, everything before it is exploratory. If you're looking at this in the future, this is from 2026!

Here's a walkthrough of the context for each of the files:

## 1. Getting Started

### June 15: [`morcer_test1`](../data/2026-06-15-1020_logdata_morcer_test1) and [`morcertest2_Acicurve`](../data/2026-06-15-1053_logdata_morcertest2_Acicurve%20%281%29)

This is an A/Q curve and A/Ci curve on a Morella cerifera from outside the field station (Anheuser-Busch Coastal Research Center, Cheriton, VA).

They fit the FvCB model, but Jmax and Vcmax came out well below what we were expecting.

These two logs have no MPF, FastKntcs or Raw columns.

### June 19: [`phrag_aq`](../data/2026-06-19-1144_logdata_phrag_aq) and [`phrag_cai`](../data/2026-06-19-1209_logdata_phrag_cai)

This is an A/Q curve and A/Ci (we ran with the typo) curve. The A/Ci curve was done incorrectly: the A/Q curve left the light at zero after it finished and we forgot to turn the light back on. The A/Ci curve ran in the dark. Perhaps not very useful but it's here if you're curious.

## 2. Trying to Open Stomata


### June 21: [`sun_control`](../data/2026-06-21-0833_logdata_morcer_sun_control)

Outdoor test on a Morella cerifera sun leaf. We mistakenly controlled on air temperature, not leaf temperature. The leaf got hotter than we wanted, 29C instead of standardized 25C.

### June 22: [`afternoon_bluelight`](../data/2026-06-22-1105_logdata_morcer_afternoon_bluelight)

Outdoors test to see if blue light would help increase stomatal conductance, an idea we got from the literature. Was very windy that day and our test setup blew over, tearing the leaf mid-run.

### June 22: [`afternoon_bluelight_indoors`](../data/2026-06-22-1405_logdata_morcer_afternoon_bluelight_indoors)

We reloaded the same test indoors on a new leaf from the same tree. We cut a branch and re-cut it underwater, holding it in the bucket for the duration of the test. This is the test that made us excited about low CO2.

### June 22: [`indoor_overnight`](../data/2026-06-22-1756_logdata_morcer_indoor_overnight)

We left the leaf out in the bucket overnight and kept it logging just to see what it would do. The CO2 cartridge lasted about 10 hours.

## 3. First Phragmites 3D (A/Q/Ci) Surface

### June 27: [`phrag_qci_surface`](../data/2026-06-27_phrag_qci_surface)

Our first crack at a 3D measurement surface on Phragmites australis: seven separate A/Ci curves at Q = [0, 200, 400, 700, 1000, 1300, and 1600]. Note that Ci ends lower every time we increase the light further, a stomatal limitation!

The `phrag_fl_dark` log has a header but no data.

## 4. Early Attempts at a Dynamic-Ramp Surface

From July 6 on, logs use LI-COR's dynamic method (the Dynamic columns), and `A` equals `Adyn`.

### July 6: [`phrag_bptest_dynamic_ramp`](../data/2026-07-06_phrag_bptest_dynamic_ramp)

Machine issues: dry chamber, flow rate weirdly split between 500 and 900. A/Ci numbers not trustworthy here.

### July 7: [`phrag_aq_dark_rerun`](../data/2026-07-07_phrag_aq_dark_rerun)

Recalibrated and changed chemicals. Flow = 500 here. Stomatal conductance low. Fluorometry flashes were firing too often and eventually they were dialed down to 60 sec.

### July 8: [`phrag_bucket_highq`](../data/2026-07-08_phrag_bucket_highq)

Updated the program: longer low-CO2 period, light going up to 2000, flow back to 900. Unable to reach a CO2 plateau, machine could push up to 2000 in our configuration.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 9: [`morella_aqc_surface`](../data/2026-07-09_morella_aqc_surface)

Big morella leaf, big enough to cover the whole device aperture. Phragmites always covers the whole device, Morella required us to select out relatively large leaves to cover the whole chamber. Oddly wavy outputs.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 9: [`phrag_brownsville_low_elevation_salinity_edge`](../data/2026-07-09_phrag_brownsville_low_elevation_salinity_edge)

First samples from Brownsville, all previous were from around the field station. We took from the highest-elevation and lowest-elevation Phragmites stands we could find along the boardwalk. This was the low-elevation (high-salinity) plant. This was a shaded leaf in its original position. VPD was inconsistent on this run.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 9: [`phrag_brownsville_upland`](../data/2026-07-09_phrag_brownsville_upland)

The high-elevation counterpart to the above leaf.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 9: [`phrag_brownsville_upland_late_repeat`](../data/2026-07-09_phrag_brownsville_upland_late_repeat)

Same leaf, again, back to back.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 10: [`morella_outside_regular_aqc`](../data/2026-07-10_morella_outside_regular_aqc)

Outdoors at CRC (the field station, not Brownsville). All-time Morella assimilation record on our machine. Temperature control went awry, leaf got way too hot.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 13: [`phrag_crc_indoor_controller_test`](../data/2026-07-13_phrag_crc_indoor_controller_test)

Indoors phragmites leaf from the CRC, trying to wrangle the machine's environmental controls. Temperature held at 25C this time, but VPD increased a bit. Developed the idea that we should dial in the flow rate at 600 on the next attempt.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 20: [`phrag_crc_indoor_vpd_flow600`](../data/2026-07-20_phrag_crc_indoor_vpd_flow600)

Flow 600 was going well, until the machine suddenly maxed out its desiccant and dried everything out, for reasons that remain unclear to us.

### July 21: [`phrag_crc_fixed_h2or_async_mpf`](../data/2026-07-21_phrag_crc_fixed_h2or_async_mpf)

We never figured out why controlling on VPD was a problem, but we did find in this run that controlling on H2O_r (at a level we calculated to equal the VPD we wanted, H2O_r = 21) kept VPD between about 0.9 - 1.1, which we were happy with. Temporarily had a filesystem issue with this file but turning machine off and on again fixed it.

## 5. TPU Step Tests

### July 10: [`morella_tpu_step_test`](../data/2026-07-10_morella_tpu_step_test)

Briefly became curious if we could find anything about limitation of photosynthesis by Triose Phosphate Utilization and incorporate it into the program. This was outdoors at the CRC on a Morella. The battery died about an hour into the run, but the data up until then are fine.

H2O control was off for most of this run (desiccant and humidifier valves read −30).

### July 14: [`phrag_indoor_tpu_controller_test`](../data/2026-07-14_phrag_indoor_tpu_controller_test)

Recalibrated dynamic flow at 600, set fan to 10k rpm. CRC Phragmites, indoors.

H2O control was off for about half of this run (desiccant and humidifier valves read −30).

## 6. Flash Diagnostic

### July 20: [`phrag_crc_h2o_flash_diagnostic`](../data/2026-07-20_phrag_crc_h2o_flash_diagnostic)

Quick test of whether fluorometry flashes disturb environmental controls.

## 7. Brownsville Sampling Cohort

This was the main data collection effort, using the automated program that you can find [here](../bp/aciq_dat_biochemical_limits_fixed_h2or_flow600.py).

An exact setup protocol can be found [here](PROTOCOL-NEW-DRAFT.md).

Field sampling design details and notes about the various chunks of bad or quarantined data are below.

### July 24: [`P01`](../data/2026-07-24_phrag_brownsville_p01_biochemical_limits) and [`P04`](../data/2026-07-24_phrag_brownsville_p04_biochemical_limits)

### July 26: [`P02`](../data/2026-07-26_phrag_brownsville_p02_biochemical_limits) and [`P03`](../data/2026-07-26_phrag_brownsville_p03_biochemical_limits)

### July 27: [`P05`](../data/2026-07-27_phrag_brownsville_p05_biochemical_limits), [`P06`](../data/2026-07-27_phrag_brownsville_p06_biochemical_limits), and [`P07`](../data/2026-07-27_phrag_brownsville_p07_biochemical_limits)

### July 28: [`P08`](../data/2026-07-28_phrag_brownsville_p08_biochemical_limits) and [`P09`](../data/2026-07-28_phrag_brownsville_p09_biochemical_limits)

### July 30: [`P10`](../data/2026-07-30_phrag_brownsville_p10_biochemical_limits), [`P11`](../data/2026-07-30_phrag_brownsville_p11_biochemical_limits), [`P12`](../data/2026-07-30_phrag_brownsville_p12_biochemical_limits), and [`P13`](../data/2026-07-30_phrag_brownsville_p13_biochemical_limits)

### July 31: [`P14`](../data/2026-07-31_phrag_brownsville_p14_biochemical_limits) and [`P15`](../data/2026-07-31_phrag_brownsville_p15_biochemical_limits)

| Leaf | Date | Elevation | Salinity | Light | Status | Issues |
|---|---|---|---|---|---|---|
| P01 | Jul 24 | High | Lower | Shade | Pilot (shade) | |
| P04 | Jul 24 | High | Lower | Shade | Pilot (shade) | |
| P02 | Jul 26 | Low | Higher | Sun | Primary | Field note: thinner, drier. Had 8 extra fluorometry flashes that land near programmed ones, exclude this from fluorometry analysis. We think the gas exchange data are fine. Similar issues as P05 but less severe. |
| P03 | Jul 26 | Low | Higher | Sun | Primary | Dark-flash trace file missing |
| P05 | Jul 27 | Low | Higher | Shade | Quarantined | Severe overlapping flash perturbations: 40 extra, 38 of which are overlapping. Program may have been run twice on accident. |
| P06 | Jul 27 | Low | Higher | Sun | Primary | Field note: some dry leaves and dry spots, dark-flash trace file missing |
| P07 | Jul 27 | High | Lower | Shade | Pilot (shade) | Dark-flash trace file missing |
| P08 | Jul 28 | High | Lower | Shade | Pilot (shade) | |
| P09 | Jul 28 | High | Lower | Shade | Quarantined | CO₂ source ran out after Q 200, dark-flash trace file missing |
| P10 | Jul 30 | Low | Higher | Sun | Primary | |
| P11 | Jul 30 | Low | Higher | Sun | Primary | |
| P12 | Jul 30 | High | Lower | Sun | Primary | Field note: health "decent", some damage to the upper leaves |
| P13 | Jul 30 | High | Lower | Sun | Primary | Thermocouple glitch at 19:46 (3 rows); Tleaf switched to energy balance for those rows, so gas values are fine |
| P14 | Jul 31 | High | Lower | Sun | Primary | |
| P15 | Jul 31 | High | Lower | Sun | Quarantined | A and gsw fell steadily through the run while controls and CO₂ held, dark-flash trace file missing |

We ran out of time to sample shade leaves in the low elevation area. Shade leaves in the high elevation area lack a counterpart.

## Sampling Design For Main Data Collection

### Site and Conventions

We collected *Phragmites australis* leaves from the Brownsville Preserve near Nassawadox, VA.

Long-term meteorological data for the Brownsville Preserve are available [here](https://www.vcrlter.virginia.edu/home2/?p=132) under PHCK/PHCK2 if anyone is interested.

We collected individual Phragmites stems across a salinity gradient: the highest-elevation stems we could find along the boardwalk at the preserve, and the lowest-elevation stems along the boardwalk.

This is a coastal forest:

- At high elevation locations, salinity is *low*.

- At low elevation locations, salinity is *high*.

- Naming generally follows elevation. I've tried to label both where possible. If there's a stray "low" or "high" stranded anywhere, it's labeled by elevation.

### Sampling Methods

We were not able to get our LI-6800 to maintain consistent internal conditions if we left it outdoors in the humid Virginia summer.

We made the decision to cut stems from the field site and transport them back to the laboratory, which gave us more consistency during the measurement runs.

We cut stems as low to the ground as possible, immediately wrapping the exposed surface in a wet paper towel, holding it in place with a rubber band, and inserting it in a ziplock bag.

It took approximately 30-60 minutes for a cut stem to make it back into a bucket of filtered water in the lab.

Upon arrival back at the lab, stems were inserted in the water bucket and re-cut at a length of at least one stem segment. This is on the order of several inches for a mature Phragmites. Re-cutting an ample amount of stem underwater reduces the risk of embolism and blockage in the hydraulic networks.

Leaves were dark adapted in a room with a blocked window and covered in aluminum foil for at least 30 minutes before measurement.

Plants remained in the bucket throughout the day for measurement, and were measured on the same day.

Sun leaves were defined as the highest leaf on a Phragmites located along the edge of its stand. Shade leaves were defined as a lower healthy leaf on a Phragmites internal to its stand. 

## Some Info About The Columns

Meanings follow LI-COR's [Summary of symbols](https://www.licor.com/support/LI-6800/topics/symbols.html)
and fluorometer pages. Meanings LI-COR doesn't give are marked with an asterisk. Here, "constant" means a variable has the same value in every log. Fluorescence values are relative units.

### IDs and file names

| ID | Meaning |
| --- | --- |
| `YYYY-MM-DD_<name>` folder | One run: acquisition date plus our description |
| `YYYY-MM-DD-HHMM_logdata_<name>` | LI-6800 log: when it was opened, then the name typed on the console. Typos are kept (`pharg`, `brws`, `Phra`; P15's log says `P0157312026`) |
| `P01`–`P15` (`run_code`) | Brownsville cohort leaf code |
| `plant_id` | Leaf code plus date as MDDYYYY: `P107302026` is P10 on 7/30/2026 |
| `obs` | Row number within a log |
| `MPF-<EVENT_ID>-<YYYYMMDD>-<HH_MM_SS>` | One fluorometer flash. Names its JSON, XLSX and `DarkAdapted_<ID>.txt`. The time in the ID is not the flash `TIME`; join flashes to log rows by ID |
| `EVENT_ID`, `ID` | The integer counter in that ID (`ID` in the log's MPF group) |
| `DarkAdaptedID`, `LightAdaptedID` | ID of the latest dark- and light-adapted flash, carried on every log row until the next one |
| `DarkPulseID` | ID of the latest dark pulse; `-` throughout (none were taken) |
| `Console s/n`, `Head s/n`, `Chamber s/n`, `Fluorometer`, `DEVICE` | Serials: console 68C-901292, head 68H-581292, fluorometer chamber MPF-551238. One instrument throughout |

### Instrument clock

Instrument clock times (`date`, `hhmmss`, file names, flash `TIME`) run 5 hours
behind the Unix `time` column, i.e. UTC−5. Local summer time is UTC−4.

### LI-6800 log columns

**SysObs**

| Field | Meaning | Units |
| --- | --- | --- |
| `obs` | Observation number | |
| `time` | Unix time (seconds since 1970) | s |
| `elapsed` | Time since the log's first observation | s |
| `date`, `hhmmss` | Instrument date and time | |
| `averaging` | Extra averaging; `none` throughout | s |

**GasEx**

| Field | Meaning | Units |
| --- | --- | --- |
| `TIME` | Time of the gas-exchange values; equals `time` without extra averaging. Repeated in Meas | s |
| `E`, `Emm` | Transpiration | mol m⁻² s⁻¹, mmol m⁻² s⁻¹ |
| `A` | Net CO2 assimilation. Where the log has a Dynamic group, `A` equals `Adyn` | µmol m⁻² s⁻¹ |
| `Ca` | CO2 at the leaf (chamber air) | µmol mol⁻¹ |
| `Ci` | Intercellular CO2; not chloroplast Cc | µmol mol⁻¹ |
| `Pci`, `Pca` | Ci and Ca as partial pressures | Pa |
| `gsw` | Stomatal conductance to water vapor | mol m⁻² s⁻¹ |
| `gbw` | Boundary-layer conductance to water vapor | mol m⁻² s⁻¹ |
| `gtw`, `gtc` | Total conductance to water vapor and to CO2 | mol m⁻² s⁻¹ |
| `Rabs` | Absorbed shortwave radiation | W m⁻² |
| `TleafEB` | Leaf temperature from the energy balance | °C |
| `TleafCnd` | Leaf temperature used in the calculations, weighted by `LTConst`. Thermocouple, except where the cohort table notes otherwise | °C |
| `SVPleaf` | Saturation vapor pressure at leaf temperature | kPa |
| `RHcham`, `VPcham`, `SVPcham` | Chamber relative humidity, vapor pressure, saturation vapor pressure | %, kPa |
| `VPDleaf` | Leaf-to-air vapor pressure deficit | kPa |
| `LatHFlux`, `SenHFlux`, `NetTherm`, `EBSum` | Energy balance: latent heat, sensible heat, net thermal radiation, and their sum | W m⁻² |
| `Asty`, `Esty` | A and E from the steady-state equations. In ramped runs `Asty` sits far above `A` because CO2 is never steady; use `A` | µmol m⁻² s⁻¹, mmol m⁻² s⁻¹ |

**Dynamic**

| Field | Meaning | Units |
| --- | --- | --- |
| `Adyn`, `Edyn` | A and E by the dynamic method | µmol m⁻² s⁻¹, mmol m⁻² s⁻¹ |
| `Crd` | Reference CO2, dry, shifted for the time lag | µmol mol⁻¹ |
| `Csd`, `dCsd/dt` | Sample CO2, dry, from a regression, and its rate of change | µmol mol⁻¹, µmol mol⁻¹ s⁻¹ |
| `Hr`, `Hs`, `dHs/dt` | The same three for H2O | mmol mol⁻¹, mmol mol⁻¹ s⁻¹ |
| `αVc`, `αVh` | Effective chamber volume for CO2 and for H2O | cm³ |

**Leak**

| Field | Meaning | Units |
| --- | --- | --- |
| `Leak`, `LeakPct` | Chamber leak, absolute and as % of flow | µmol s⁻¹, % |
| `CorrFact`, `CorrFactPct` | Leak correction factor | , % |
| `Fan` | Estimated flow from the mixing fan | µmol s⁻¹ |

**FLR** (fluorescence summary; values carry forward from the latest flash)

| Field | Meaning | Units |
| --- | --- | --- |
| `Fo`, `Fm` | Minimal and maximal F of the latest dark-adapted flash | |
| `Qmax_d`, `A_dark` | Peak light of that flash, and A just before it | µmol m⁻² s⁻¹ |
| `Fv/Fm` | Maximum PSII efficiency, 1 − Fo/Fm | |
| `Fs`, `Fm'` | Steady-state and maximal F of the latest light-adapted flash | |
| `Qmax` | Peak light of that flash | µmol m⁻² s⁻¹ |
| `PhiPS2` | Operating PSII efficiency, 1 − Fs/Fm′ | |
| `PS2/1` | Assumed share of absorbed light going to PSII; 0.5 throughout | |
| `Qabs_fs`, `A_fs` | Absorbed light and A when Fs was taken | µmol m⁻² s⁻¹ |
| `ETR` | Electron transport, PhiPS2 × Qabs_fs × PS2/1. An instrument estimate, not a measured flux | µmol m⁻² s⁻¹ |
| `PhiCO2` | (A_fs − A_dark)/Qabs_fs | µmol µmol⁻¹ |
| `NPQ` | (Fm − Fm′)/Fm′; an index, not a fraction of absorbed energy | |
| `Fo'`, `alt._Fo'` | Minimal F in the light. With no dark pulse, `Fo'` is the estimate Fo/(Fv/Fm + Fo/Fm′), so the two are equal here | |
| `Fmin` | Minimal F measured by a dark pulse; 0 throughout | |
| `Fv'/Fm'` | 1 − Fo′/Fm′ | |
| `qP`, `qN` | (Fm′ − Fs)/(Fm′ − Fo′) and (Fm − Fm′)/(Fm − Fo′) | |
| `qP_Fo`, `qN_Fo` | The same, using Fo instead of Fo′ | |
| `qL`, `1-qL` | Fraction of PSII centers open under the lake model, qP·Fo′/Fs, and the fraction closed | |

**MPF** (details of the latest multiphase flash)

| Field | Meaning | Units |
| --- | --- | --- |
| `P1_dur`, `P2_dur`, `P3_dur` | Phase durations | ms |
| `P1_Fmax`, `T@P1_Fmax` | Highest F in phase 1, and when | , ms |
| `Q@P1_Fmax` | Light at that moment\* | µmol m⁻² s⁻¹ |
| `P1_PredF`, `P1_ΔF` | Phase-1 F predicted from the phase-2 fit, and measured minus predicted\* | |
| `P2_ramp` | Percent drop in flash light across phase 2 | % |
| `P2_slp`, `P2_slp_se`, `P2_int`, `P2_int_se`, `P2_R2` | Phase-2 regression of F on light: slope, intercept, their SEs, and R²\*. The intercept is the Fm′ estimate (`P2_int` = `Fm'`) | centimol m⁻² s⁻¹ for slopes |
| `P2_dQdt` | Rate of light change in phase 2 | mol m⁻² s⁻² |
| `P3_Fmax`, `T@P3_Fmax`, `Q@P3_Fmax`, `P3_PredF` | Phase-3 versions of the phase-1 fields\* | , ms, µmol m⁻² s⁻¹ |
| `P3_ΔF` | Phase-3 F measured minus predicted | |

**FastKntcs** (induction-flash kinetics; empty throughout, no induction flashes were run)

| Field | Meaning | Units |
| --- | --- | --- |
| `ID`, `Dur` | Induction flash ID and duration | , ms |
| `Fo`, `F1`, `T@F1`, `F2`, `T@F2` | F before the flash, and two F points with their times | , ms |
| `T@HIR` | Time of half the initial rise | ms |
| `DCo`, `InitSlope`, `DCmax`, `T@DCmax`, `PhiPS2_dc` | Not defined by LI-COR; DC-signal versions of the above\* | , s⁻¹, , ms, |

**LeafQ**

| Field | Meaning | Units |
| --- | --- | --- |
| `Qin` | Light incident on the leaf, from the sources weighted in `QConst`; here only the fluorometer. Includes the flash spikes | µmol m⁻² s⁻¹ |
| `Qabs` | Absorbed light, Qin × alpha | µmol m⁻² s⁻¹ |
| `alpha` | Leaf absorptance, weighted over light sources | |
| `convert` | Energy per µmol of photons, for `Rabs` | J/µmol |

**Const**

| Field | Meaning | Units |
| --- | --- | --- |
| `S` | Leaf area in the chamber; 6 throughout | cm² |
| `K` | Stomatal ratio; 0.5 throughout | |
| `Geometry` | Leaf geometry for the boundary-layer model; `0: Broadleaf` throughout | |
| `Custom` | One-sided boundary-layer conductance for custom geometry; 2.0, unused here | mol m⁻² s⁻¹ |
| `UseDynamic` | Whether `A` and `E` are the dynamic values; `True` throughout | |

**Meas**

| Field | Meaning | Units |
| --- | --- | --- |
| `TIME` | Same as the GasEx `TIME` (duplicate name; drop one when reading) | s |
| `CO2_s`, `CO2_r` | Sample and reference CO2 | µmol mol⁻¹ |
| `H2O_s`, `H2O_r` | Sample and reference water vapor | mmol mol⁻¹ |
| `CO2_a`, `H2O_a` | Sample CO2 and H2O before the match adjustment | µmol mol⁻¹, mmol mol⁻¹ |
| `Flow` | Flow into the chamber | µmol s⁻¹ |
| `Pa` | Atmospheric pressure | kPa |
| `ΔPcham` | Chamber overpressure | kPa |
| `Tair` | Air temperature | °C |
| `Tleaf`, `Tleaf2` | Leaf thermocouples 1 and 2. `Tleaf2` reads 999.9 throughout: not connected | °C |
| `Offset`, `Offset2` | Thermocouple offsets; 0 throughout | °C |
| `Fan_speed` | Mixing fan speed | rpm |
| `Qamb_in`, `Qamb_out` | Ambient light inside the chamber (0 throughout) and at the external sensor | µmol m⁻² s⁻¹ |

**FlrLS** (fluorometer light source)

| Field | Meaning | Units |
| --- | --- | --- |
| `Q` | Light from the fluorometer; includes the flash spikes | µmol m⁻² s⁻¹ |
| `f_red`, `f_blue`, `f_farred` | Fraction of Q that is red, blue, far red (`f_farred` 0 throughout) | |
| `Q_red`, `Q_blue`, `Q_farred` | Each color's part of Q | µmol m⁻² s⁻¹ |
| `Q_modavg` | Measuring light's part of Q | µmol m⁻² s⁻¹ |
| `F`, `F_dc` | Modulated fluorescence signal and DC fluorescence signal | |
| `Pc` | Photodiode count | |
| `Tled`, `TDigital`, `TPreamp`, `TPwrSpy`, `TDrive` | Fluorometer temperatures: LED, digital board, preamp, power supply, LED driver | °C |
| `TSPF` | Time since the previous flash | s |
| `state` | 0 normal, 1 rectangular flash, 2 MPF, 3 induction, 4 dark | |

**FlrStats**

| Field | Meaning | Units |
| --- | --- | --- |
| `F_avg`, `F_dc_avg` | Mean F and F_dc over `period` | |
| `dF/dt`, `dF_dc/dt` | Their slopes | min⁻¹ |
| `period` | Window for those stats; 15 throughout | s |

**MchEvent** (the latest IRGA match)

| Field | Meaning | Units |
| --- | --- | --- |
| `time`, `hhmmss` | When it happened | s |
| `co2_t`, `h2o_t` | Time the CO2 and H2O match took\* | s |
| `count` | Number of matches | |
| `co2_adj`, `h2o_adj` | Error before matching, reference − sample | µmol/mol, mmol/mol |
| `co2_match`, `h2o_match` | Correction applied | µmol/mol, mmol/mol |
| `co2_at`, `h2o_at` | Concentration at the match | µmol/mol, mmol/mol |
| `co2_cv`, `h2o_cv` | Coefficient of variation during the match | % |

**Raw**

| Field | Meaning | Units |
| --- | --- | --- |
| `Vflow`, `VPchamber` | Flow-meter and chamber-pressure sensor signals | V |
| `abs_c_a`, `abs_c_b`, `abs_h_a`, `abs_h_b` | CO2 and H2O absorptance in IRGA A (sample) and B (reference) | |
| `Wc_s`, `Wc_r`, `Wco_s`, `Wco_r` | CO2 absorbing and non-absorbing detector counts, sample and reference | |
| `Ww_s`, `Ww_r`, `Wwo_s`, `Wwo_r` | The same for H2O | |
| `Flow_s_v`, `Flow_r_v` | Sample and reference flow signals | V |
| `Tleaf_mv`, `Tleaf2_mv` | Thermocouple signals (`Tleaf2_mv` 0 throughout) | mV |

**MchStatus**

| Field | Meaning | Units |
| --- | --- | --- |
| `MatchValveR`, `MatchValveS` | Match valve positions | % |
| `MatchCO2`, `MatchH2O` | Current match adjustments | µmol/mol, mmol/mol |
| `cf_co2_a`, `cf_co2_b`, `cf_co2_c`, `cf_co2_d`, `cf_h2o_a`, `cf_h2o_b`, `cf_h2o_c`, `cf_h2o_d` | Range-match coefficients | |
| `co2_fit_low`, `co2_fit_high`, `h2o_fit_low`, `h2o_fit_high` | Concentration range of the range-match fit | µmol mol⁻¹, mmol mol⁻¹ |
| `co2_elapsed`, `h2o_elapsed` | Time since the last match | min |

**ConStatus**

| Field | Meaning | Units |
| --- | --- | --- |
| `CO2_f`, `CO2_f_s` | CO2 injector flow signal and its status value | V |
| `Pump_f`, `Pump_f_s`, `Pump_p`, `Pump_p_s` | Pump flow and pressure signals, each with its status value | V |
| `Tboard` | Console board temperature | °C |
| `V_system` | System (battery) voltage | V |

**Status**

| Field | Meaning | Units |
| --- | --- | --- |
| `DIAG` | Head diagnostic code; 2 or 3 is normal | |
| `Flow_s`, `Flow_r` | Flow through the sample and reference cells | µmol s⁻¹ |
| `Txchg`, `Txchg_sp` | Heat-exchanger temperature and its setpoint | °C |
| `Tirga`, `Tchopper` | IRGA block and chopper temperatures | °C |
| `Ts`, `Tr` | Sample and reference cell inlet temperatures | °C |
| `CO2_%` | CO2 injector output | % |
| `Desiccant_%`, `Humidifier_%` | Desiccant and humidifier valve positions. −30 isn't documented; in our logs it appears when H2O control was off | % |
| `CO2_r_sp`, `H2O_r_sp` | Reference CO2 and H2O setpoints | µmol mol⁻¹, mmol mol⁻¹ |
| `SS_s`, `SS_r` | IRGA signal strength, sample and reference | % |

### Log header block

| Key | Meaning |
| --- | --- |
| `File opened` | When the log was created |
| `Console ver`, `Scripts ver`, `Head ver`, `Flr. Version` | Software and firmware versions |
| `Head cal` | JSON of the IRGA zero and span coefficients and span concentrations |
| `Factory cal date` | Last factory calibration |
| `CO2 rangematch`, `H2O rangematch` | When the last range match was done |
| `Chamber type`, `Chamber rev`, `Chamber cal` | Chamber model (6800-01 fluorometer chamber), revision and calibration codes |
| `Stability Definition` | Time-stamped line giving the stability criteria (e.g. ΔCO2 slope < 0.1 over 20 s) |
| `SysConst:AvgTime` | Averaging time; 4 in the July logs, 0 in June |
| `SysConst:Oxygen` | O2 % used in the calculations; 21 |
| `ChambConst:Chamber`, `ChambConst:Aperture` | Chamber and aperture used by the boundary-layer model |
| `ChambConst:blc_a`, `blc_b`, `blc_c`, `blc_d`, `blc_e` | Boundary-layer conductance model coefficients |
| `ChambConst:blc_minS`, `blc_maxS`, `blc_Po` | Leaf-area range the model holds for, and its reference pressure\* |
| `LTConst:fT1`, `fT2`, `fTeb` | Weights of thermocouple 1, thermocouple 2 and energy balance in `TleafCnd` |
| `LTConst:deltaTw` | Chamber wall minus air temperature, for the energy balance\* |
| `LQConst:Leaf`, `LQConst:Ambient` | Leaf absorptance preset and ambient light type |
| `LQConst:abs_*` | Leaf absorptance for each light source (ambient, red/green/blue/white LED, red/blue fluorometer) |
| `LQConst:k_*` | Energy per µmol of photons for each source (J/µmol) |
| `QConst:fQ_*` | Weight of each light sensor or source in `Qin`; only `fQ_Flr` is 1 here |
| `LeakConst:fan_a`, `fan_b`, `fan_c`, `fan_d` | Fan-flow model coefficients |
| `LeakConst:Fs_meas`, `Fs_true`, `leak_wt` | Leak calibration: measured vs true flow, and a weight\* |

### Flash files (`MPF-*.json`, `MPF-*.xlsx`)

One flash per file. The JSON and XLSX hold the same event. In the XLSX (sheet
`Measurements`), column A holds the key names and column B the single values; the traces
and the `MPF` and `FLR` copies are in the columns to the right. Top-level times are in seconds; the nested
`MPF` copy repeats them in ms under the log's names.

| Key | Meaning | Units |
| --- | --- | --- |
| `EVENT_ID`, `DEVICE` | See IDs | |
| `DATE`, `TIME`, `TIMESTAMP` | Instrument date and time of the flash, and Unix time | , , s |
| `TYPE`, `VERSION` | Flash type (MPF throughout) and file format version (5) | |
| `OUTRATE` | Trace sample rate; 100 | Hz |
| `MARGIN` | Samples before and after the flash; 5 | |
| `PHASE1_DURATION`, `PHASE2_DURATION`, `PHASE3_DURATION` | Programmed phase lengths; 300 each | ms |
| `RAMP` | Programmed phase-2 ramp; 25 | % |
| `Q_RED_SETPOINT` | Programmed flash intensity; 10000\* | µmol m⁻² s⁻¹ |
| `D_RED_PERCENT` | Not defined by LI-COR; 90 throughout | |
| `MODRATE` | Measuring-light modulation rate; 250000 | Hz |
| `DC_SECS_OFFSET`, `AC_SECS_OFFSET`, `PFD_SECS_OFFSET`, `FLASH_SECS_OFFSET` | Timing offset of each channel, around a microsecond\* | s |
| `T_OFFSET` | Time shift to the flash start | s |
| `Tled` | LED temperature | °C |
| `Pre_Qin`, `Pre_Qabs`, `Pre_Q_red`, `Pre_Q_blue`, `Pre_Q_farred` | Light just before the flash | µmol m⁻² s⁻¹ |
| `Pre_Favg`, `Pre_dF/dt` | Mean F and its slope just before the flash | , min⁻¹ |
| `Fs`, `Fo` | Steady-state F (light flashes, 1,775 files) or minimal F (dark flashes, 46 files) | |
| `SECS` | Time of each trace sample from the flash start (100 samples) | s |
| `FLUOR`, `DC` | Modulated and DC fluorescence traces | |
| `PFD`, `RED`, `REDMODAVG`, `FARRED` | Traces of total light, red actinic, measuring light, far red | µmol m⁻² s⁻¹ |
| `CODE` | Step of each sample: 2 leading margin, 4–6 phases 1–3, 7 trailing margin (3, rectangular, never appears) | |
| `Starts`, `Stops` | Sample index where each step starts and stops | |
| `Dspk_indices`, `Dspk_values` | Not defined by LI-COR; one per step, likely despiking\* | |
| `FMAX`, `T@FMAX` | The Fm′ estimate (= `P2_INT`) and its time | , s |
| `QMAX` | Peak flash light | µmol m⁻² s⁻¹ |
| `P1_dur`, `P1_MAXF`, `T@P1_MAXF`, `Q@P1_MAXF`, `P1_PREDF`, `P1_DELTAF` | Phase 1, as in the log's MPF group | s for times |
| `P2_dur`, `P2_ramp`, `P2_SLP`, `P2_SLP_SE`, `P2_INT`, `P2_INT_SE`, `P2_R2`, `P2_DQDT` | Phase 2, as in the log's MPF group | s for times |
| `P3_dur`, `P3_MAXF`, `T@P3_MAXF`, `Q@P3_MAXF`, `P3_PREDF`, `P3_DELTAF` | Phase 3, as in the log's MPF group | s for times |
| `MPF`, `FLR` | Nested copies of the log's MPF and FLR groups for this flash | |

### DarkAdapted TXT (`DarkAdapted_MPF-*.txt`)

| Key | Meaning |
| --- | --- |
| `DarkAdaptedID` | Flash ID |
| `Fo`, `Fm`, `Qmax_d`, `PS2/1` | As in the log's FLR group |
| `Adark` | A just before the flash (the log's `A_dark`) |
| `file` | Path of the flash JSON on the instrument |

### Sample metadata (`brownsville_phragmites_sample_metadata_2026.csv`)

| Column | Meaning |
| --- | --- |
| `plant_id` | See IDs |
| `spp` | Species; `phragmites_australis` |
| `demo` | `mature` for every leaf |
| `location` | Site; `brownsville` |
| `zone` | Elevation zone, `high` or `low` |
| `canopy_depth` | `exterior` for every leaf |
| `canopy_height` | `top` for sun leaves, `bottom` for shade leaves (same as `illum`) |
| `illum` | `sun` or `shade` |
| `health` | Field rating, `good` or `decent` |
| `notes` | Field notes |

### Release index files (`run_index.csv`, `manifest.csv`)

| Column | Meaning |
| --- | --- |
| `source_log` | Path of the log |
| `file_opened`, `console_firmware`, `instrument_scripts`, `head_version`, `fluorometer_version`, `chamber` | Copied from the log header |
| `species_from_filename` | Species read from the log name |
| `run_code`, `plant_id` | Cohort IDs; blank for method-development runs |
| `elevation_zone`, `canopy_light` | From the sample metadata |
| `status` | `primary_sun`, `pilot_shade`, `quarantined`, or `method_development` |
| `qc_reason` | Why a run was quarantined |
| `primary_fluorescence` | Whether the leaf is in the primary fluorescence comparison |
| `dark_reference_source` | Where Fv/Fm comes from: `event file` (dark-flash JSON) or `log summary` |
| `program_association` | Which program ran the log. Inferred, since the instrument records no program hash |
| `path`, `bytes`, `sha256` | `manifest.csv`: every file under `data/`, its size and checksum |

### Fields added in `outputs/`

| Field | Meaning | Units |
| --- | --- | --- |
| `Q_level` | Nominal light step a row belongs to | µmol m⁻² s⁻¹ |
| `minute` | `elapsed` / 60 | min |
| `YII`, `YNPQ`, `YNO` | Photochemical, regulated and unregulated yields (Kramer et al. 2004): `YII` = PhiPS2, `YNO` = 1/(NPQ + 1 + qL(Fm/Fo − 1)), `YNPQ` = 1 − YII − YNO | |

Other output tables name their columns after the source field plus a summary
(`_median`, `_last5`, …).