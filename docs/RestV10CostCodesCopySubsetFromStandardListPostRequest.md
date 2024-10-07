# RestV10CostCodesCopySubsetFromStandardListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard_cost_code_list_id** | **int** | The ID of the standard cost code list id | 
**standard_cost_code_ids** | **List[int]** | A list of the standard cost code ids to add to biller | 
**sub_job_id** | **int** | The ID of the subjob biller | [optional] 
**project_id** | **int** | The ID of the project biller | 

## Example

```python
from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post_request import RestV10CostCodesCopySubsetFromStandardListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CostCodesCopySubsetFromStandardListPostRequest from a JSON string
rest_v10_cost_codes_copy_subset_from_standard_list_post_request_instance = RestV10CostCodesCopySubsetFromStandardListPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CostCodesCopySubsetFromStandardListPostRequest.to_json())

# convert the object into a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post_request_dict = rest_v10_cost_codes_copy_subset_from_standard_list_post_request_instance.to_dict()
# create an instance of RestV10CostCodesCopySubsetFromStandardListPostRequest from a dict
rest_v10_cost_codes_copy_subset_from_standard_list_post_request_from_dict = RestV10CostCodesCopySubsetFromStandardListPostRequest.from_dict(rest_v10_cost_codes_copy_subset_from_standard_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


