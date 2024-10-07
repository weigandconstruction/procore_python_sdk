# Project6OpenItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**details** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.project6_open_items_inner import Project6OpenItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Project6OpenItemsInner from a JSON string
project6_open_items_inner_instance = Project6OpenItemsInner.from_json(json)
# print the JSON string representation of the object
print(Project6OpenItemsInner.to_json())

# convert the object into a dict
project6_open_items_inner_dict = project6_open_items_inner_instance.to_dict()
# create an instance of Project6OpenItemsInner from a dict
project6_open_items_inner_from_dict = Project6OpenItemsInner.from_dict(project6_open_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


