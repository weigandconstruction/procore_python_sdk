# RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel


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

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level import RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel from a JSON string
rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level_instance = RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel.to_json())

# convert the object into a dict
rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level_dict = rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level_instance.to_dict()
# create an instance of RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel from a dict
rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level_from_dict = RestV10BimModelRevisionPlansGet200ResponseInnerOneOf1BimLevel.from_dict(rest_v10_bim_model_revision_plans_get200_response_inner_one_of1_bim_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


