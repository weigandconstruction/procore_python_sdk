# Project6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project ID | [optional] 
**name** | **str** | Project name | [optional] 
**address** | [**Project6Address**](Project6Address.md) |  | [optional] 
**stage_name** | **str** | Project stage | [optional] 
**status_name** | **str** | Project status | [optional] 
**type_name** | **str** | Project type | [optional] 
**open_items** | [**List[Project6OpenItemsInner]**](Project6OpenItemsInner.md) |  | [optional] 
**created_by** | [**Project6CreatedBy**](Project6CreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project6 import Project6

# TODO update the JSON string below
json = "{}"
# create an instance of Project6 from a JSON string
project6_instance = Project6.from_json(json)
# print the JSON string representation of the object
print(Project6.to_json())

# convert the object into a dict
project6_dict = project6_instance.to_dict()
# create an instance of Project6 from a dict
project6_from_dict = Project6.from_dict(project6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


