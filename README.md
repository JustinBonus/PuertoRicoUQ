# PuertoRicoUQ
### Henry Watson, Pedro Arduino, Justin Bonus

Puerto Rico's automated workflow for state-of-the-art tsunami hazard analysis with automated inventory generation, near-real time wave simulation, structural analysis, uncertainty quantification, and surrogate modeling. 

> ``Probabalistic Tsunami Hazard Analysis (PTHA)`` 

> ``Bathymetry and Topography Acquisition (NOAA/NCEIS/USGS)`` 

> ``AI inventory generation (BRAILS++)`` 

> ``Boussinesq Wave Simulation (CelerisAi)`` 

> ``Hydrodynamic and Structural Response (OpenSees)`` 

> ``Uncertainty Quantification and Surrogate Modeling (HydroUQ)`` 

> ``Damage and Loss Estimation (pelicun/PBE)`` 

> ``Regional Risk and Resilience Assessment (R2D)``


## Run cases parametrically through HydroUQ

For parametric simulations, where you want to probabilistically sample hydrodynamic and structural parameters, you can run from HydroUQ. If you want to couple hydrodynamic forces to OpenSees, you should also run from HydroUQ.

```powershell

..\HydroUQ_Windows_Download\Hydro_UQ.exe

```

or 

```bash

../HydroUQ/build/Hydro_UQ

```

and go to 

`Top Bar` >> `Examples` >> `Near-Real Time - Loiza - CelerisAi` 

then select the appropriate configuration, bathymetry, and wave files from the PuertoRicoUQ project. 

> ⚠️ All three input files (config.json, bathy.txt, and waves.txt) are required to be in the specified directory (`./src/sites/Loiza/example_case`).


## Run cases individually through Celeris

For one-off simulations, you can run the Celeris simulation directly from the command line.

```bash

python3 ../SimCenterBackendApplications/modules/createEVENT/Celeris/setrun.py -d ./src/sites/Loiza/example_case -f config.json -b bathy.txt -w waves.txt

```
> ⚠️ All three input files (config.json, bathy.txt, and waves.txt) are required to be in the specified directory (`./src/sites/Loiza/example_case`).

## How-to Cite

Bonus, J., Arduino, P., Watson, H., Xiao, D., Pakzad, A., & McKenna, F. (2025). PuertoRicoUQ (0.0.1). Zenodo. https://doi.org/10.5281/zenodo.15491891

Zenodo: https://zenodo.org/records/15491890
DOI: https://doi.org/10.5281/zenodo.15491890
