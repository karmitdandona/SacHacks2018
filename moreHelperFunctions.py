import json

import vehicleInit

def main():
  # --- REMOVE ALL NON-SIMULATIONS FROM DATA.JSON --- #
  allVehicles = vehicleInit.getVehicleDataAsDict()
  dictCopy = allVehicles.copy()
  for key, val in allVehicles.items():
    if "simulation" not in key and "Simulation" not in key:
      del dictCopy[key]
  with open('data.json', 'w') as outfile:
    json.dump(dictCopy, outfile)

if __name__ == "__main__":
  main()