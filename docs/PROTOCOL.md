## Title

An Automated Photosynthetic Characterization Method With Fluorescence

Riley Leff (George Washington University), Acadia Conboy, Keryn Gedan (George Washington University)

## Abstract

We're interested in characterizing photosynthetic machinery to better predict how plants will fare under changing climate and learn a bit about the world. In the long term, we hope to scale up and standardize precise measurement of plant mechanics. This protocol documents the approach we ran as a pilot experiment in summer 2026: an automated program for the LI-6800 built on the dynamic assimilation method. We added low-CO2 holding periods between ramps and frequent fluorometry flashes. The program outputs a detailed 3D surface of carbon assimilation (A), intercellular carbon dioxide concentration (Ci), and light levels (Q), and takes about 3 hours to run. This method is not perfect and remains under development: we link to a discussion of some of its limitations below. [LINK: technical report]

## Before starting

This protocol assumes the reader is trained in using the LI-6800 to measure gas exchange and fluorescence.

It is good practice to allow your LI-6800 machine approximately 30 minutes to warm up after turning it on, and to ensure that it passes all warm-up tests before beginning your work.

We started dark-adapting our first leaf at the same time we turned on the machine, so it would be ready to go as soon as the machine was warmed up. This is simple and just involves blocking all the light from the leaf with aluminum foil.

Before your first set of measurements, you need to complete the dynamic calibration. Note that the 6800's dynamic calibrations are flow-dependent. We used 600 umol s-1, and we were only able to decide on 600 via trial and error. The optimal setting for you depends on the leaf architecture, boundary layer characteristics, and other things that will likely vary across studies -- higher flow trades a larger concentration difference for faster chamber air exchange. You may find that you need a value different than 600, just be sure to recalibrate the dynamic equations every time you try a different value.

We found it worthwhile to plug an ethernet cable into the 6800 and allow a frontier LM to handle the filesystem back-and-forths for us. We highly recommend doing the same: we found that the agent was much less likely to make devastating typos than we were. We did not need to provide any special instructions for the agent to orient itself beyond pointing it to the LI-COR documentation site.

Plan at least three hours of measurement time for each leaf. Be mindful that on these very long measurement runs with very high CO2 concentrations, you'll need to replace the CO2 cartridges frequently. We found that we could usually get 2 runs done on a single brand-new cartridge, three was borderline, and we could not complete four without a replacement. Make sure to check for yourself, though: slight leaks could affect the longevity of your gas cylinders.

## Steps

### Default settings

1. Table:

| Setting | Value |
|---|---|
| Flow | 600 umol s-1 |
| Fan | 10,000 rpm |
| Leaf-temperature target | 25 C |
| Reference water vapor, H2O_r | 21 mmol mol-1 |
| Light spectrum | r90B40, selected on console |
| Dark equilibration | Q = 0, CO2_r = 420 ppm, 5 min, followed by 60 s baseline and a dark flash |
| Low-CO2 conditioning | Q = 600 umol photons m-2 s-1; CO2_r = 120 ppm; 18 min |
| Measured Q ladder | 50, 100, 200, 350, 600, 1000, 1400, 1700, 2000 umol photons m-2 s-1 |
| CO2_r ramp | 120 to 2000 ppm at 200 ppm min-1 |
| Active flashes | First at 60 s into ramp, then every 90 s |
| Low-CO2 parks | First Q: 10 min; subsequent Q: 5 min; each followed by 90 s settling |

These controls will be automated while the program runs, this is just for your reference.

### A Note On Humidity control

2. We initially controlled on leaf VPD, targeting 1 kPa, but the machine would not hold VPD stable during the automated runs.
3. By controlling on H2O_r instead, e.g. H2O_r = 21 mmol mol-1, we got a far more consistent VPD than controlling directly on VPD allowed. This was at a flow of 600 umol s-1 and a leaf-temperature target of 25 C. We therefore use that setting throughout this protocol and monitor measured leaf VPD. For other measurement conditions, we recommend choosing H2O_r based on the resulting leaf VPD you desire.

### Sample preparation

4. Pick a leaf: On Phragmites australis, our definition of a sun leaf was the tallest one on a stalk situated along the boundary of a stand, and a shade leaf was a lower one on a stalk internal to a stand. Instead of collecting the leaf, collect the whole stem! This is the best time to put ID tags on your samples and mark the leaf of interest (e.g. with a sharpie mark on the stalk immediately adjacent to the leaf) as well.
5. Cut the stem in the field: Cut the stem with sharp shears as low to the ground as you can. Immediately put a wet paper towel on the open cut, rubber-band it to the stem, and place the base of the stem in a ziplock bag.
6. Transport: We collected our stems within a window of about 30 minutes in the field, and we had a roughly 30 minute drive back to the laboratory from the field site.
7. Re-cut under water: Immediately upon return, we removed the ziplock bag, rubber band, and wet paper towel. Then we submerged the stems in a Home Depot bucket full of filtered water from the lab sink. We re-cut at least one segment of the stem fully underwater to mitigate hydraulic failures (Wheeler et al. 2013; Sperry 2013).
8. Hold until measurement: Stems stayed in a bucket in an air-conditioned and dark laboratory room throughout the day until it was their turn to be measured. Stems were always collected and measured on the same day. The cut end of each stem stayed submerged in the bucket while its leaf was clamped in the chamber.

### Warm Up: Start the machine and dark-adapt the leaf

9. Turn on the LI-6800.
10. Don't forget to track and label your sample IDs.
11. Wrap the leaf in foil and start a 30-minute timer.
12. Check CO2, humidifier water, desiccant, soda lime, power, and storage.
13. Run the LI-6800's warm-up tests while the leaf adapts.

### Configure the measurement

14. Stop other programs and automatic control routines.
15. Set flow to 600 umol s-1. Range-match the analyzers across the intended concentrations and make sure your dynamic calibration is set up at the correct flow rate. The supplied background program sets flow to 600 when it starts. To use another flow, change the program's flow setting and recalibrate DAT at the new flow before running it.
16. Enable Add Dynamic Equations and Use dynamic.
17. After range-matching, under Log Setup > Match Options, set CO2 match and H2O match to Never match for the run. You don't want matching to interrupt the CO2 ramps. See LI-COR's matching-options documentation [LINK: LI-COR match options].
18. Select Full fluorometer, the optimized MultiPhase flash configuration, and r90B40.
19. Set Fluorometer Action at Log to 0: Nothing.
20. Load the background program from GitHub [LINK: program file in repo]. Use the default-settings table for its parameters.

### Clamp in the leaf and start recording

21. After at least 30 minutes of dark adaptation, turn the chamber light off. (e.g. set Q to 0 in the environment tab).
22. Turn off the lights in the lab, and block the windows if possible.
23. Unwrap and clamp the leaf with minimal light exposure.
24. Check the leak rate before proceeding, it should be at or near 0%.
25. Open a new log with a very descriptive name.
26. Make sure you include gas-exchange, fluorescence, and diagnostic fields. Be certain to include Txchg, Txchg_sp, H2O_r_sp, and CO2_r_sp, those are useful for troubleshooting!
27. Launch the program one time, review the settings, and continue.
28. Confirm the log count increases and that you can hear the pleasant "ba-dop" sound effect on log actions (if sound is enabled).

### Let the program run, enjoy the beauty and splendor of automation

29. This happens automatically, but here's an overview of how it works:
    - Dark baseline: 5 minutes at Q = 0 and CO2_r = 420, then 1 minute of gas-exchange logging plus a dark flash.
    - Low-CO2 conditioning: 18 minutes at Q = 600 and CO2_r = 120.
    - First light level: Q = 50 at low CO2 for ten minutes, then 90 seconds of settling time.
    - CO2 ramp: 120 to 2000 ppm at 200 ppm per minute. The first active flash occurs at 60 seconds, then again every 90 seconds.
    - Remaining light levels: repeat these steps at Q = 100, 200, 350, 600, 1000, 1400, 1700, and 2000. Between the ramps, return to low CO2 for five minutes plus another 90 seconds of settling.
    - Finish: restore CO2_r = 420 and Q = 0, then close the log.

### Periodically check in on the run

30. When we did our project, we would check back in every 20-30 minutes.
    - If something fails (for example, if CO2 runs out), the program will not stop itself, so runs that fail early can be very costly time-wise.
    - Expect the program to run roughly three hours after launch.

### Export and inspect the data

31. Export the gas-exchange log and complete flash folder: an LLM agent (preferably a smart one) can do this if you've plugged in an ethernet cable.
32. Follow the GitHub analysis guide [LINK: analysis guide] for some details on working with the data.

### Data processing

33. Example analyses are in the GitHub repository:
    - examples go here

### Expected outputs

34. A complete default run should contain:
    - A dark gas-exchange baseline.
    - One dark FoFm measurement.
    - A low-CO2 conditioning time series.
    - Nine gas-exchange ramps.
    - 54 active flash events: six per ramp across nine light levels.

## Guidelines

Symbols table: A, gsw, Q, CO2_r, Ca, Ci (calculated intercellular, not chloroplastic Cc), H2O_r/H2O_s, VPDleaf, Tleaf, Cc (estimated), gm (mole-fraction basis), Fo/Fm, Fs/Fm', Fv/Fm, PhiPSII (exported as PhiPS2), ETR, NPQ = (Fm - Fm')/Fm', qL (lake model), J, Rd (positive CO2 release), Gamma*.

Data and code availability: Program, example observations, fluorescence events, analysis code, and existing results: [LINK: GitHub repo]

See our pilot data at [LINK: Zenodo DOI] !

Licenses: Code: MIT. Original data and documentation: CC BY 4.0, with third-party exceptions described on the Github repo.

Other acronyms: MPF = MultiPhase Flash, DAT = Dynamic Assimilation Technique, PSII = Photosystem II.

## Warnings

Safety warnings: Follow LI-COR instructions for CO2 cartridges, chemicals, electrical power, and instrument handling.

Here are some disclaimers, things to consider, and a bit more background info:

* Low CO2 does not necessarily guarantee maximum stomatal conductance or eliminate limits on diffusion. We added this with the intent of increasing stomatal conductance, though results were mixed and confounded by machine artifacts. Please see the technical report here: [LINK: technical report]

* This method, like many other photosynthetic characterization approaches, requires us to choose between measuring intact plants in field conditions, or cut/damaged plants brought back to the lab. Here, we used cut plants and re-cut them under water well before measurement: see the sample preparation steps. This is a tradeoff where the best approach likely depends on your field site: we found that our instrument was not able to hold internal conditions (e.g. temperature, humidity) constant throughout the day in the humid Virginia summer, and elected to accept the more consistent penalty of cutting each stem, unlocking laboratory measurement conditions. Please be sure to report how your samples were handled, as well as the exact timestamps and the order you processed them in, as the effect size of the handling decision can be large relative to biological differences of interest.

* This protocol is built on top of the Dynamic Assimilation Technique, which accounts for CO2 accumulating in or leaving the chamber air during a ramp. It requires the chamber to be well-mixed, accurate flow measurements, a good match on your IRGAs, and dynamic tuning appropriate to the chamber and flow settings. See LI-COR's DAT setup instructions [LINK: LI-COR DAT setup].

* I'm putting this part again for visibility. Before your first set of measurements, you need to complete the dynamic calibration. Note that the 6800's dynamic calibrations are flow-dependent. We used 600 umol s-1, and we were only able to decide on 600 via trial and error. The optimal setting for you depends on the leaf architecture, boundary layer characteristics, and other things that will likely vary across studies -- higher flow trades a larger concentration difference for faster chamber air exchange. You may find that you need a value different than 600, just be sure to recalibrate the dynamic equations every time you try a different value.

* We flash the fluorometer frequently during this measurement series, which causes a brief deviation in photosynthetic output after each flash. These short instances are not representative of how the leaf is responding to the average conditions set by the measurement device, and should be smoothed out or clipped in post. We provide scripts on our Github repository that show our approach to this.

* While we seek to isolate how a leaf's photosynthetic apparatus responds to CO2 levels, the intercellular carbon concentration (Ci) is not the CO2 concentration at Rubisco. Truly isolating responses to CO2 would require a researcher to measure mesophyll conductance (gm). Direct measurement of gm is beyond the scope of this protocol, though this protocol could be combined with online carbon-isotope discrimination to yield improved accuracy. From the data yielded by the protocol documented here, it is possible to attempt a fluorescence-based estimate of gm, as we show in our analysis. Our estimates were sensitive to our assumptions, so we are treating those as exploratory.

* Low stomatal conductance can make estimates of Ci unreliable. For example, if stomatal conductance is low, cuticular conductance can be misattributed to stomata, altering estimates of Ci (Hussain et al. 2024). There are also complex interactions with mesophyll conductance that might not be accounted for with simple or typical FvCB model assumptions.

* In this protocol, light only runs from low to high. Leaf induction is stateful, and we're not fully capturing the possible range of responses here.

* While we have tens of thousands of data points observed, it's only across about a dozen individual leaves. There are likely many avenues to build on and improve this protocol, or at least make it more general across other species and circumstances. You are welcome to explore our data and reach out to me to ask questions if you'd like! rileyleff@gmail.com. I just like plants and photosynthesis, in general if you're using this I'd like to hear what you're up to.

## References

- Saathoff AJ, Welles J (2021). Gas exchange measurements in the unsteady state. Plant, Cell & Environment 44:3509-3523. https://doi.org/10.1111/pce.14178
- Harley PC, Loreto F, Di Marco G, Sharkey TD (1992). Theoretical considerations when estimating the mesophyll conductance to CO2 flux by analysis of the response of photosynthesis to CO2. Plant Physiology 98:1429-1436. https://doi.org/10.1104/pp.98.4.1429
- Pons TL et al. (2009). Estimating mesophyll conductance to CO2: methodology, potential errors, and recommendations. Journal of Experimental Botany 60:2217-2234. https://academic.oup.com/jxb/article/60/8/2217/563289
- Hussain SB, Stinziano J, Pierre MO, Vincent C (2024). Accurate photosynthetic parameter estimation at low stomatal conductance: effects of cuticular conductance and instrumental noise. Photosynthesis Research 160:111-124. https://doi.org/10.1007/s11120-024-01092-8
- Sperry J (2013). Cutting-edge research or cutting-edge artefact? An overdue control experiment complicates the xylem refilling story. Plant, Cell & Environment 36:1916-1918. https://doi.org/10.1111/pce.12148
- Wheeler JK, Huggett BA, Tofte AN, Rockwell FE, Holbrook NM (2013). Cutting xylem under tension or supersaturated with gas can generate PLC and the appearance of rapid recovery from embolism. Plant, Cell & Environment 36:1938-1949. https://doi.org/10.1111/pce.12139
- LI-COR. LI-6800 operating instructions. https://www.licor.com/support/LI-6800/manuals.html
- Additional references: [LINK: Literature Cited in repo README]

## Troubleshooting

Problem: Vapor Pressure Deficit Unstable.
Cause: If you're controlling on temperature and vapor pressure deficit at the same time, it confuses the machine on how it should handle it -- e.g. it's trying to control [temperature and temperature + humidity] concurrently.
Solution: It makes the machine's life easier if you control on H2O_r instead, and calculate the H2O_r you need to achieve the desired vapor pressure deficit before you start! That gives the machine a clean separation of its temperature control and humidity control.

Problem: Stomatal Conductance spikes, goes negative, or otherwise behaves strangely.
Cause: It's possible the machine was adjusting its temperature and humidity controls, and that could leave artifacts in the data!
Solution: Check the temperature and humidity controls carefully and be sure to look at the raw, unsmoothed data.

## Materials

- LI-COR 6800 with 6800-01 fluorometer chamber and a working leaf-temperature sensor. CO2 supply, water supply for the humidifier, desiccant (we used Sorbead Orange Chameleon, Drierite works too), power (battery or AC), and storage.
- Opaque cover for dark-adapting the leaves. We used aluminum foil and covered the lab's lone window with a tarp.
- If cutting branches: we used Fiskars plant clippers, a Home Depot bucket, paper towels, filtered sink water, ziplock bags, field flagging to write IDs on, and a sharpie.
- Program: aciq_dat_biochemical_limits_fixed_h2or_flow600.py.
- Repository: [LINK: GitHub repo]

## Metadata

Keywords: Photosynthesis, CO2, dynamic assimilation, LI-6800, chlorophyll fluorescence, Phragmites australis, Morella cerifera, jmax, vmax, vcmax, stomata, FvCB, C3.
Image attribution: Riley Leff (this is a Morella cerifera near Nassawadox, VA).
