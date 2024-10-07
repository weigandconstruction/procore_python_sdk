# RestV10ChecklistListsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Checklist template name | [optional] 
**template_id** | **int** | Checklist template ID | [optional] 
**response_set** | [**ChecklistDefaultResponseSet**](ChecklistDefaultResponseSet.md) |  | [optional] 
**lists** | [**List[Checklist1]**](Checklist1.md) | Array of Checklists | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_checklist_lists_get200_response_inner import RestV10ChecklistListsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChecklistListsGet200ResponseInner from a JSON string
rest_v10_checklist_lists_get200_response_inner_instance = RestV10ChecklistListsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChecklistListsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_checklist_lists_get200_response_inner_dict = rest_v10_checklist_lists_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChecklistListsGet200ResponseInner from a dict
rest_v10_checklist_lists_get200_response_inner_from_dict = RestV10ChecklistListsGet200ResponseInner.from_dict(rest_v10_checklist_lists_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


