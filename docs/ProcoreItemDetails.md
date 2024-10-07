# ProcoreItemDetails

Details of Procore item to be linked to a CoordinationIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Id of the Procore item to be associated | 
**item_type** | **str** | Type of the Procore item to be associated | 

## Example

```python
from procore_sdk.models.procore_item_details import ProcoreItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProcoreItemDetails from a JSON string
procore_item_details_instance = ProcoreItemDetails.from_json(json)
# print the JSON string representation of the object
print(ProcoreItemDetails.to_json())

# convert the object into a dict
procore_item_details_dict = procore_item_details_instance.to_dict()
# create an instance of ProcoreItemDetails from a dict
procore_item_details_from_dict = ProcoreItemDetails.from_dict(procore_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


