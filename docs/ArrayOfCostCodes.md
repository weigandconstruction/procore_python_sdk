# ArrayOfCostCodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[ArrayOfCostCodesErrorsInner]**](ArrayOfCostCodesErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_cost_codes import ArrayOfCostCodes

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCostCodes from a JSON string
array_of_cost_codes_instance = ArrayOfCostCodes.from_json(json)
# print the JSON string representation of the object
print(ArrayOfCostCodes.to_json())

# convert the object into a dict
array_of_cost_codes_dict = array_of_cost_codes_instance.to_dict()
# create an instance of ArrayOfCostCodes from a dict
array_of_cost_codes_from_dict = ArrayOfCostCodes.from_dict(array_of_cost_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


