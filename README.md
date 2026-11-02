# Coupled A/Ci/Q and chlorophyll fluorescence surfaces for *Phragmites australis* across a coastal marsh elevation gradient

Riley Leff (1), Acadia Conboy (2), Keryn Gedan (1)

1 - George Washington University

2 - James Madison University

## Abstract

Here, we're releasing (to our knowledge) the densest per-leaf gas-exchange surface of photosynthetic measurements publicly available as of the time of writing. 15 *Phragmites australis* leaves were sampled at high or low salinity locations within a coastal forest on the Eastern Shore of Virginia, and 12 produced usable data. We're also releasing the exact LI-6800 program we ran to obtain them, our sampling protocols, the miscellaneous messy data we have from our initial testing, and a brief discussion of what we found.

The program outputs a detailed 3D surface of carbon assimilation (A), intercellular carbon dioxide concentration (Ci), and light levels (Q), and takes about 3 hours to run per leaf. Our method is built on the dynamic assimilation technique (Saathoff & Welles 2021), but we add low-CO2 periods between ramps and frequent fluorometric flashes. Our intent with the low-CO2 periods was to increase stomatal conductance (gsw), but despite a promising pilot on *Morella cerifera*, gsw remained roughly the same across the low-CO2 periods in our larger Phragmites dataset. This method is not perfect and remains under development.

## Background

### Biochemistry and Stomata

Photosynthetic output depends on both leaf biochemical capability and stomatal aperture. Prominent modeling approaches in plant physiology require us to identify these separately (Farquhar et al. 1980; Sperry et al. 2017). Improving our estimates will allow us to better predict how plants will respond to changing climates and explore novel modeling approaches better suited for our world of increasing computing power.

Nominally, our measurements of biochemical capability are independent of stomata: we measure carbon assimilation rate against a changing Ci, and map the chemistry from the resulting curves. We call this the A/Ci curve (Long & Bernacchi 2003). Even if stomatal conductance (gsw) is very low, if we know Ci, we can fit a model to capture the biochemical capability.

### Inherited Vulnerabilities In The Methods

But this independence is an assumption. We usually can't measure Ci directly, in real time, as is required for these sorts of gas-exchange analyses. There are a few challenges presented:

1. gsw and Ci are confounded: both are inferred from the rate that water vapor exits the leaf. If gsw is very low (e.g. <0.05 mol m⁻² s⁻¹ or so), the amount of water diffusing through the leaf's cuticle can be significant compared to gsw. Photosynthetic measurement devices cannot distinguish between stomatal water and cuticular water, so it all gets misattributed to gsw, artificially elevating the Ci estimate. See Hussain et al. (2024).

2. Photosynthesis happens in cells, not between them. There is an additional layer of diffusion, called mesophyll conductance (gm), between the intercellular spaces and the chloroplasts. Often, researchers make the assumption that Ci is equal to the chloroplast CO2 concentration (Cc), and that assumption is vulnerable to a limiting gm. If gm is a bottleneck, our A/Ci curves can look fine while our parameter estimates come out biased.
   
3. If gsw is low, you might not be able to get Ci very high. Since the most informative part of the A/Ci curve is near or below ambient CO2 levels, this is usually less of an issue than the other two points above.

### The Changing Methods Landscape

Older methods for deriving A/Ci curves required leaves to come to a full steady-state equilibration with the chamber environment. With these approaches, measuring individual leaves in extreme detail would have been challenging to complete within a single day.

More recently, researchers have shifted towards dynamic methods that don't require the leaf to be at steady-state (Stinziano et al. 2017; Saathoff & Welles 2021). This usually involves a continuously increasing CO2 ramp and a calculated correction for chamber gas capacitance. This is much faster: a single one of our CO2 ramps takes a little under 10 minutes.

### Our Approach

Stomata typically open under low CO2 conditions (Mott 1988). Our program scrubs CO2 down to 120 ppm before each ramp. This was our attempt at mitigating the cuticular conductance problem and the limit on maximum Ci.

We run dynamic A/Ci curves across 9 light levels ranging from 50-2000 µmol m⁻² s⁻¹.

Our program adds regular fluorometry flashes across all light levels and CO2 ramps. This gives us an external estimate of electron transport distinct from gas-exchange alone, overlaid across the surface of A, Q, and Ci.

Our program takes about 3 hours per leaf to run.

### Why This Level Of Detail?

Most photosynthesis papers using the LI-6800, our field’s primary tool, don’t make their raw data available. We found 4659 peer-reviewed papers that mentioned some permutation of “LI-6800” and were able to get full text for 2989, of which 2893 actually used the instrument. 947 of those papers claimed or linked to data, and we were able to examine 751 of them. If we exclude the 196 we couldn’t easily access programmatically (e.g. due to captchas and other scraping mitigation techniques), that leaves 2697 papers, of which only:

265 (9.8%) shared at least per-leaf values.
133 (4.9%) shared point-level data on gas exchange.
56 (2.1%) shared raw data straight from the instrument.

Full 2D curves are even rarer, and 3D curves barely exist. Our literature search found 469 papers that ran A/Ci curves, and we could check 415 of them.

44 (11%) shared point-level curves.
We found only 1 A/Ci/Q 3D surface dataset, used in two papers (Lochocki & McGrath 2025; Lochocki et al. 2025). It covers 11 tobacco plants, but each plant was measured at only 1–6 light levels, so the Q dimension runs across different plants. This is not a leaf-level characterization.

Outside of the literature we were able to find 2 other 3D cases: a single sunflower leaf saved as example data in an [R package](https://github.com/cdmuir/photosynthesis) (96 points) and a [lettuce dataset](https://github.com/ktrizzo/photorch-studio) that lacks fluorescence (~1,600 points; Lei et al. 2025). Methods for combining gas exchange and fluorometry have previously been described in the literature (Yin et al. 2009), but they're built on separate A/Ci and A/Q curves.

I want to help dial in the methods, and to do so, I think we need bigger data made broadly available. That's what we're doing here!

| | Ours | Tobacco (Lochocki et al. 2025) | Sunflower | Lettuce |
|---|---|---|---|---|
| Leaves measured | 12 usable (15 sampled) | 11 plants | 1 | not stated |
| Surface | per leaf | across plants | per leaf | not stated |
| Light levels | 9 per leaf | 13 total, 1–6 per plant | 8 | 6 |
| Gas-exchange points | ~5,050 per leaf (~3,600 after flash masking) | 19–130 per plant (689 total) | 96 | ~1,600 |
| Fluorescence flashes | ~55 per leaf | every point: 19–130 per plant | every point: 96 | none |

## Methods 

See [the data guide](docs/DATA.md) or the [protocols.io protocol](https://doi.org/10.17504/protocols.io.92ld3bnong5b/v2) for detailed information about setup and sampling. Download the exact LI-6800 program we used [here](bp/aciq_dat_biochemical_limits_fixed_h2or_flow600.py).

## Results And Discussion

See [docs/ANALYSIS.md](docs/ANALYSIS.md) for a rundown.

## Data Availability

It's here! See [`data/`](data/) for the raw data.

## Literature Cited

Duursma, R. A., Blackman, C. J., Lopéz, R., Martin-StPaul, N. K., Cochard, H., & Medlyn, B. E. (2019). On the minimum leaf conductance: its role in models of plant water use, and ecological and environmental controls. *New Phytologist*, 221, 693–705. https://doi.org/10.1111/nph.15395

Farquhar, G. D., von Caemmerer, S., & Berry, J. A. (1980). A biochemical model of photosynthetic CO2 assimilation in leaves of C3 species. *Planta*, 149, 78–90. https://doi.org/10.1007/BF00386231

Hussain, S. B., Stinziano, J., Pierre, M. O., & Vincent, C. (2024). Accurate photosynthetic parameter estimation at low stomatal conductance: effects of cuticular conductance and instrumental noise. *Photosynthesis Research*, 160, 111–124. https://doi.org/10.1007/s11120-024-01092-8

Lei, T., Rizzo, K. T., & Bailey, B. N. (2025). PhoTorch: a robust and generalized biochemical photosynthesis model fitting package based on PyTorch. *Photosynthesis Research*, 163, 21. https://doi.org/10.1007/s11120-025-01136-7

Lochocki, E. B., & McGrath, J. M. (2025). Widely used variants of the Farquhar-von-Caemmerer-Berry model can cause errors in parameter estimation. *in silico Plants*, diaf014. https://doi.org/10.1093/insilicoplants/diaf014

Lochocki, E. B., Salesse-Smith, C. E., & McGrath, J. M. (2025). PhotoGEA: an R package for closer fitting of photosynthetic gas exchange data with non-Gaussian confidence interval estimation. *Plant, Cell & Environment*, 48, 5104–5119. https://doi.org/10.1111/pce.15501

Long, S. P., & Bernacchi, C. J. (2003). Gas exchange measurements, what can they tell us about the underlying limitations to photosynthesis? Procedures and sources of error. *Journal of Experimental Botany*, 54, 2393–2401. https://doi.org/10.1093/jxb/erg262

Meadows, R. E., & Saltonstall, K. (2007). Distribution of native and introduced *Phragmites australis* in freshwater and oligohaline tidal marshes of the Delmarva peninsula and southern New Jersey. *The Journal of the Torrey Botanical Society*, 134, 99–107. https://doi.org/10.3159/1095-5674(2007)134[99:DONAIP]2.0.CO;2

Mott, K. A. (1988). Do stomata respond to CO2 concentrations other than intercellular? *Plant Physiology*, 86, 200–203. https://doi.org/10.1104/pp.86.1.200

Nguyen, L. X., Lambertini, C., Sorrell, B. K., Eller, F., Achenbach, L., & Brix, H. (2013). Photosynthesis of co-existing Phragmites haplotypes in their non-native range: are characteristics determined by adaptations derived from their native origin? *AoB PLANTS*, 5, plt016. https://doi.org/10.1093/aobpla/plt016

Saathoff, A. J., & Welles, J. (2021). Gas exchange measurements in the unsteady state. *Plant, Cell & Environment*, 44, 3509–3523. https://doi.org/10.1111/pce.14178

Saltonstall, K. (2002). Cryptic invasion by a non-native genotype of the common reed, *Phragmites australis*, into North America. *Proceedings of the National Academy of Sciences*, 99, 2445–2449. https://doi.org/10.1073/pnas.032477999

Shimazaki, K., Doi, M., Assmann, S. M., & Kinoshita, T. (2007). Light regulation of stomatal movement. *Annual Review of Plant Biology*, 58, 219–247. https://doi.org/10.1146/annurev.arplant.57.032905.105434

Sperry, J. S., Venturas, M. D., Anderegg, W. R. L., Mencuccini, M., Mackay, D. S., Wang, Y., & Love, D. M. (2017). Predicting stomatal responses to the environment from the optimization of photosynthetic gain and hydraulic cost. *Plant, Cell & Environment*, 40, 816–830. https://doi.org/10.1111/pce.12852

Stinziano, J. R., Morgan, P. B., Lynch, D. J., Saathoff, A. J., McDermitt, D. K., & Hanson, D. T. (2017). The rapid A–Ci response: photosynthesis in the phenomic era. *Plant, Cell & Environment*, 40, 1256–1262. https://doi.org/10.1111/pce.12911

Vasquez, E. A., Glenn, E. P., Brown, J. J., Guntenspergen, G. R., & Nelson, S. G. (2005). Salt tolerance underlies the cryptic invasion of North American salt marshes by an introduced haplotype of the common reed *Phragmites australis* (Poaceae). *Marine Ecology Progress Series*, 298, 1–8. https://doi.org/10.3354/meps298001

Yin, X., Struik, P. C., Romero, P., Harbinson, J., Evers, J. B., van der Putten, P. E. L., & Vos, J. (2009). Using combined measurements of gas exchange and chlorophyll fluorescence to estimate parameters of a biochemical C3 photosynthesis model: a critical appraisal and a new integrated approach applied to leaves in a wheat (*Triticum aestivum*) canopy. *Plant, Cell & Environment*, 32, 448–464. https://doi.org/10.1111/j.1365-3040.2009.01934.x


## Licenses

Code is [MIT](LICENSE). Data, figures, and documentation are [CC BY 4.0](LICENSE-DATA.md). If for some reason you need the source to be even more open than this, let me know and we can figure it out.

## Acknowledgements

Thank you to my advisor and labmates for big-time discussions about photosynthesis (Keryn Gedan, Juan Ignacio Martinez, Aidan Brown, Caroline Tone, and Lillie Congram).

Thanks to Alex Pivovaroff for always being on call regarding the strange matters of ecophysiology.

Thanks to everyone around the field station that volunteered some knowledge to us (Natasha Woods, Eddie Long, Katie Pline, many others).

Thanks to the ABCRC staff for supporting our work: Cora Baird, Buck Doughty, Donna Fauber, Sophia Hoffman, and Tom Burkett.

Most importantly, thank you to Acadia Conboy, an undergraduate student from James Madison University, who was tremendous in her contributions to this research all summer.

I'm indebted to all of the talented undergraduate researchers that I've worked with on summer projects throughout my PhD: Maggie Connolly, Ellyn Kinkel, Sehrin Hossain, Kaeden Rippon, and Shay Cihlar. You guys rock.

To my cats: meow.

## Relevant Links

- Zenodo: https://doi.org/10.5281/zenodo.23785367
- Protocols.io: https://doi.org/10.17504/protocols.io.92ld3bnong5b/v2
- Blog: https://rileyleff.com/blog/notes-on-measuring-plants

## AI Statement

The written documentation and public-facing prose (e.g. the root [README](README.md), [docs/DATA.md](docs/DATA.md), [docs/PROTOCOL.md](docs/PROTOCOL.md), and [docs/ANALYSIS.md](docs/ANALYSIS.md)) is human-made, with the exception of the some of the organization/legwork (e.g. large tables of parameter names, links to code in figure captions, references). Claude did those tasks. 

Everything else in this repo is AI generated. 100% of the code in this repository is AI-generated.