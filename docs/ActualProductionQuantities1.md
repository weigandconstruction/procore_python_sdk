# ActualProductionQuantities1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for the Actual Production Quantity | 
**quantity** | **float** | Amount installed | [optional] 
**crew_id** | **int** | The Crew ID for the Actual Production Quantity | [optional] 
**location_id** | **int** | The Location ID for the Actual Production Quantity | [optional] 

## Example

```python
from procore_sdk.models.actual_production_quantities1 import ActualProductionQuantities1

# TODO update the JSON string below
json = "{}"
# create an instance of ActualProductionQuantities1 from a JSON string
actual_production_quantities1_instance = ActualProductionQuantities1.from_json(json)
# print the JSON string representation of the object
print(ActualProductionQuantities1.to_json())

# convert the object into a dict
actual_production_quantities1_dict = actual_production_quantities1_instance.to_dict()
# create an instance of ActualProductionQuantities1 from a dict
actual_production_quantities1_from_dict = ActualProductionQuantities1.from_dict(actual_production_quantities1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


