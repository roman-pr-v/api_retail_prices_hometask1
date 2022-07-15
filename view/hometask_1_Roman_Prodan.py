import requests
import csv

RP_result = "G:\\PythonWorkshop\\sum_RP_result.csv"

locations = ('eastasia', 'southeastasia', 'centralus', 'eastus', 'eastus2', 'westus', 'northcentralus', 'southcentralus', 'northeurope', 'westeurope', 'japanwest', 'japaneast', 'brazilsouth', 'australiaeast', 'australiasoutheast',  'southindia', 'centralindia', 'westindia', 'canadacentral', 'canadaeast', 'uksouth', 'ukwest', 'westcentralus',  'westus2', 'koreacentral', 'koreasouth', 'francecentral', 'francesouth', 'australiacentral', 'australiacentral2', 'uaecentral', 'uaenorth', 'southafricanorth', 'southafricawest', 'switzerlandnorth', 'switzerlandwest', 'germanynorth', 'germanywestcentral', 'norwaywest', 'norwayeast', 'brazilsoutheast', 'westus3')
option = "productName eq 'General Block Blob v2' and skuName eq 'Cool LRS'"
result_prices = {}

for location in locations:
    api_endpoint = f"https://prices.azure.com/api/retail/prices?$filter=armRegionName eq '{location}' and {option}"
    r = requests.get(api_endpoint)
    data = r.json()
    data_items = data['Items']
    sumRetail = 0
    for offer in data_items:
        sumRetail += offer['retailPrice']
    result_prices[location] = sumRetail
    location_results = result_prices.keys()
    retailPrices_results = result_prices.values()

    with open(RP_result, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([location_results, retailPrices_results])

minretailPrices = min(result_prices.values())
maxretailPrices = max(result_prices.values())
sumretailPrices = sum(result_prices.values())
lengthretailPrices = len(result_prices.values())
avgretailPrices = sumretailPrices/lengthretailPrices

additional_result = {'minPrice': minretailPrices, 'maxPrices': maxretailPrices, 'avgPrice': avgretailPrices}
additional_result_keys = additional_result.keys()
additional_result_values = additional_result.values()
with open(RP_result, "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([additional_result_keys, additional_result_values])





