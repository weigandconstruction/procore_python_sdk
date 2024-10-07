# RestV10CostCodesCopySubsetFromStandardListPost207Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md) | Array of successfully created Cost Codes | [optional] 
**failures** | [**List[RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner]**](RestV10ProjectsProjectIdTimesheetsScopedCostCodesGet200ResponseInner.md) | Array of biller-created duplicates of Standard Cost Codes | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post207_response import RestV10CostCodesCopySubsetFromStandardListPost207Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CostCodesCopySubsetFromStandardListPost207Response from a JSON string
rest_v10_cost_codes_copy_subset_from_standard_list_post207_response_instance = RestV10CostCodesCopySubsetFromStandardListPost207Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CostCodesCopySubsetFromStandardListPost207Response.to_json())

# convert the object into a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post207_response_dict = rest_v10_cost_codes_copy_subset_from_standard_list_post207_response_instance.to_dict()
# create an instance of RestV10CostCodesCopySubsetFromStandardListPost207Response from a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post207_response_from_dict = RestV10CostCodesCopySubsetFromStandardListPost207Response.from_dict(rest_v10_cost_codes_copy_subset_from_standard_list_post207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


