from pathlib import Path
from yaml import safe_load


projdir = Path(__file__).parents[1]
with open(projdir / "config.yaml") as file:
    config = safe_load(file)
    TOPM = config["TOPM"]
    AVAC = config["AVAC"]

bounds = TOPM["bounds"] | AVAC.get("bounds", dict())
xmin = bounds["xmin"]
xmax = bounds["xmax"]
ymin = bounds["ymin"]
ymax = bounds["ymax"]

nx = int((xmax - xmin) / TOPM["resolution"] / 66)
ny = int((ymax - ymin) / TOPM["resolution"] / 66)

nsim = 100

tmax = 300

dt_init = 0.002
cfl_desired = 0.95
nb_max_iter = 1000

refinement = 4
refinement_area = 0
nodatavalue = 99999
DryWetLimit = 1e-5
