# ProcoreItemDetails1

Details of Procore item to be linked to a BimViewpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Id of the Procore item to be associated | 
**item_type** | **str** | Type of the Procore item to be associated | 
**primary** | **bool** | Set as primary viewpoint for the procore item. Only applicable for BimModelRevision | [optional] 

## Example

```python
from procore_sdk.models.procore_item_details1 import ProcoreItemDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of ProcoreItemDetails1 from a JSON string
procore_item_details1_instance = ProcoreItemDetails1.from_json(json)
# print the JSON string representation of the object
print(ProcoreItemDetails1.to_json())

# convert the object into a dict
procore_item_details1_dict = procore_item_details1_instance.to_dict()
# create an instance of ProcoreItemDetails1 from a dict
procore_item_details1_from_dict = ProcoreItemDetails1.from_dict(procore_item_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


