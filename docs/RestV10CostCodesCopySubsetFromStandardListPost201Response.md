# RestV10CostCodesCopySubsetFromStandardListPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md) | Array of successfully created Cost Codes | [optional] 
**failures** | **List[str]** | An empty array | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post201_response import RestV10CostCodesCopySubsetFromStandardListPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CostCodesCopySubsetFromStandardListPost201Response from a JSON string
rest_v10_cost_codes_copy_subset_from_standard_list_post201_response_instance = RestV10CostCodesCopySubsetFromStandardListPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CostCodesCopySubsetFromStandardListPost201Response.to_json())

# convert the object into a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post201_response_dict = rest_v10_cost_codes_copy_subset_from_standard_list_post201_response_instance.to_dict()
# create an instance of RestV10CostCodesCopySubsetFromStandardListPost201Response from a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post201_response_from_dict = RestV10CostCodesCopySubsetFromStandardListPost201Response.from_dict(rest_v10_cost_codes_copy_subset_from_standard_list_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


