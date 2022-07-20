import csv
import requests

RP_RESULT = "G:\\PythonWorkshop\\RP_result.csv"

LOCATIONS = (
    'eastasia', 'southeastasia', 'centralus', 'eastus', 'eastus2', 'westus',
    'northcentralus',    'southcentralus', 'northeurope', 'westeurope',
    'japanwest', 'japaneast', 'brazilsouth', 'australiaeast',
    'australiasoutheast',  'southindia', 'centralindia', 'westindia',
    'canadacentral', 'canadaeast', 'uksouth', 'ukwest', 'westcentralus',
    'westus2', 'koreacentral', 'koreasouth', 'francecentral', 'francesouth',
    'australiacentral', 'australiacentral2', 'uaecentral', 'uaenorth',
    'southafricanorth', 'southafricawest', 'switzerlandnorth', 'switzerlandwest',
    'germanynorth', 'germanywestcentral', 'norwaywest', 'norwayeast',
    'brazilsoutheast', 'westus3'
)

OPTION = "productName eq 'General Block Blob v2' and skuName eq 'Cool LRS'"

result_prices = {}

for location in LOCATIONS:
    api_endpoint = f"https://prices.azure.com/api/retail/prices?$filter=armRegionName " \
                   f"eq '{location}' and {OPTION}"
    r = requests.get(api_endpoint)
    data = r.json()
    data_items = data['Items']
    SUM_RETAIL = 0
    for offer in data_items:
        SUM_RETAIL += offer['retailPrice']
        result_prices[location] = SUM_RETAIL

location_results = result_prices.keys()
retailPrices_results = result_prices.values()

with open(RP_RESULT, "w", encoding="utf8", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["location", "sum_prices"])
    for key, value in result_prices.items():
        writer.writerow([key, value])
    writer.writerow(["maxPrice", max(result_prices.values())])
    writer.writerow(["minPrice", min(result_prices.values())])
    writer.writerow(["avgPrice", sum(result_prices.values())/len(result_prices.values())])

