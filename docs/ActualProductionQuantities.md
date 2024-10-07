# ActualProductionQuantities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Amount installed | 
**wbs_code_id** | **int** | The Production Quantity Code for the Actual Production Quantity. This is necessary if your project is configured for Task Codes. DO NOT provide if your project is not configured for Task Codes. | [optional] 
**cost_code_id** | **int** | The Cost Code ID for the Actual Production Quantity. DO NOT provide if your project is configured for Task Codes. | 
**crew_id** | **int** | The Crew ID for the Actual Production Quantity | [optional] 
**location_id** | **int** | The Location ID for the Actual Production Quantity | [optional] 
**timesheet_id** | **int** | The Timesheet ID for the Actual Production Quantity. If the &#39;timesheet_id&#39; is provided in the request, then the date for the timesheet will be associated with the production quantity, regardless of whether an additional date is sent in the request. | [optional] 
**sub_job_id** | **int** | The Sub Job ID for the Actual Production Quantity. DO NOT provide if your project is configured for Task Codes. | [optional] 

## Example

```python
from procore_sdk.models.actual_production_quantities import ActualProductionQuantities

# TODO update the JSON string below
json = "{}"
# create an instance of ActualProductionQuantities from a JSON string
actual_production_quantities_instance = ActualProductionQuantities.from_json(json)
# print the JSON string representation of the object
print(ActualProductionQuantities.to_json())

# convert the object into a dict
actual_production_quantities_dict = actual_production_quantities_instance.to_dict()
# create an instance of ActualProductionQuantities from a dict
actual_production_quantities_from_dict = ActualProductionQuantities.from_dict(actual_production_quantities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


