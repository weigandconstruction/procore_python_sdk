# RestV10BimLevelsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**elevation** | **float** | Level elevation | [optional] 
**name** | **str** | Level name | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_file_id** | **int** | ID of the BIM Model revision linked to the Level | [optional] 
**location_id** | **int** | ID of location linked to the Level | [optional] 
**created_by_id** | **int** | ID of user that created the level | [optional] 
**bim_file** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile**](RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile.md) |  | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**created_by** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee**](RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_levels_get200_response_inner import RestV10BimLevelsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimLevelsGet200ResponseInner from a JSON string
rest_v10_bim_levels_get200_response_inner_instance = RestV10BimLevelsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BimLevelsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_bim_levels_get200_response_inner_dict = rest_v10_bim_levels_get200_response_inner_instance.to_dict()
# create an instance of RestV10BimLevelsGet200ResponseInner from a dict
rest_v10_bim_levels_get200_response_inner_from_dict = RestV10BimLevelsGet200ResponseInner.from_dict(rest_v10_bim_levels_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


