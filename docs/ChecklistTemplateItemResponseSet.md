# ChecklistTemplateItemResponseSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the response set | [optional] 
**name** | **str** | Name of the response set | [optional] 
**responses** | [**List[ChecklistResponse]**](ChecklistResponse.md) |  | [optional] 

## Example

```python
from procore_sdk.models.checklist_template_item_response_set import ChecklistTemplateItemResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistTemplateItemResponseSet from a JSON string
checklist_template_item_response_set_instance = ChecklistTemplateItemResponseSet.from_json(json)
# print the JSON string representation of the object
print(ChecklistTemplateItemResponseSet.to_json())

# convert the object into a dict
checklist_template_item_response_set_dict = checklist_template_item_response_set_instance.to_dict()
# create an instance of ChecklistTemplateItemResponseSet from a dict
checklist_template_item_response_set_from_dict = ChecklistTemplateItemResponseSet.from_dict(checklist_template_item_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


