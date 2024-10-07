# RestV10BimLevelsGet200ResponseInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**elevation** | **float** | Level elevation | [optional] 
**name** | **str** | Level name | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_file** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile**](RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile.md) |  | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**created_by** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee**](RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner_one_of import RestV10BimLevelsGet200ResponseInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimLevelsGet200ResponseInnerOneOf from a JSON string
rest_v10_bim_levels_get200_response_inner_one_of_instance = RestV10BimLevelsGet200ResponseInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimLevelsGet200ResponseInnerOneOf.to_json())

# convert the object into a dict
rest_v10_bim_levels_get200_response_inner_one_of_dict = rest_v10_bim_levels_get200_response_inner_one_of_instance.to_dict()
# create an instance of RestV10BimLevelsGet200ResponseInnerOneOf from a dict
rest_v10_bim_levels_get200_response_inner_one_of_from_dict = RestV10BimLevelsGet200ResponseInnerOneOf.from_dict(rest_v10_bim_levels_get200_response_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


